

from django import forms
from dbs.models.pos import CardPaymentDetail, ProductSale, SaleItem, SalePaymentDetail
from django.contrib.auth.decorators import login_required

from django.forms import ValidationError, modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse

from django.contrib import messages
from utils.autoidgenerator import Auto_Id, Auto_Id_DuplicateChecker
from .models import *

class CheckboxInput(forms.CheckboxInput):
    template_name = 'cbbox.html'
    input_type = 'checkbox'

# enabling datetime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    
    
def SaleInvoice_Update_View(request,title='Sale Invoice',invType='Sale', create_url=None, return_url=None):
    pass


@login_required
def SaleInvoice_Create_View(request,title='Sale Invoice',invType='Sale', create_url=None, return_url=None):
    widgets = {}
    for field in ProductSale._meta.fields:
        if isinstance(field, models.DateTimeField):
            widgets[field.name] = DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        elif isinstance(field, models.BooleanField):
            widgets[field.name] = CheckboxInput()
            
    ModelForm = modelform_factory( ProductSale, fields='__all__', exclude=('IsReadOnly',), widgets=widgets)
    widgets_item={}
    for field in ProductSale._meta.fields:
        if isinstance(field, models.DateTimeField):
            widgets_item[field.name] = DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        elif isinstance(field, models.BooleanField):
            widgets_item[field.name] = CheckboxInput()
            
    ModelForm_Item = modelform_factory( SaleItem, fields='__all__', exclude=('IsReadOnly',), widgets=widgets_item)
    widgets_payment={}
    for field in SalePaymentDetail._meta.fields:
        if isinstance(field, models.DateTimeField):
            widgets_payment[field.name] = DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        elif isinstance(field, models.BooleanField):
            widgets_payment[field.name] = CheckboxInput()
            
    ModelForm_Payment = modelform_factory( SalePaymentDetail, fields='__all__', exclude=('IsReadOnly',), widgets=widgets_payment)
    
    widgets_card_payment={}
    for field in CardPaymentDetail._meta.fields:
        if isinstance(field, models.DateTimeField):
            widgets_card_payment[field.name] = DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        elif isinstance(field, models.BooleanField):
            widgets_card_payment[field.name] = CheckboxInput()
            
    ModelForm_Card_Payment = modelform_factory( CardPaymentDetail, fields='__all__', exclude=('IsReadOnly',), widgets=widgets_card_payment)
    
    instance_invoice=None
    instance_payment=None
    instance_card_payment=None
    instance_saleItem=None
    
    if request.method == 'POST':
        form = ModelForm(request.POST, instance=instance_invoice)
        form_item = ModelForm_Item(request.POST, instance=instance_saleItem)
        form_payment = ModelForm_Payment(request.POST, instance=instance_payment)
        form_card_payment = ModelForm_Card_Payment(request.POST, instance=instance_card_payment)
        if form.is_valid() and form_item.is_valid() and form_payment.is_valid() and form_card_payment.is_valid():
            try:
                form.instance = form.save(commit=False)
                form_item.instance = form_item.save(commit=False)
                form_payment.instance = form_payment.save(commit=False)
                form_card_payment.instance = form_card_payment.save(commit=False)
                
                #Generating Invoice Number
                autopk = Auto_Id().get_auto_id(ProductSale,  form.instance)
                
                form.instance.SaleDate = form_item.instance.SaleDate
                form_item.instance.Sale = form.instance
                form_payment.instance.Sale = form.instance
                form_card_payment.instance.Sale = form.instance
                
                form.save()
                form_item.save()
                form_payment.save()
                form_card_payment.save()
                return redirect(return_url) 
            except Exception as e:
                print(e)
                return HttpResponse(e)
    else:
        form = ModelForm()
        form_item = ModelForm_Item()
        form_payment = ModelForm_Payment()
        form_card_payment = ModelForm_Card_Payment()

        
        

def handle_invoice_create(request,invform, itemform, paymentform, cardpaymentform, return_url):
    #Generating Invoice Number
    autopk = Auto_Id().get_auto_id(ProductSale,  invform.instance)
    if autopk != "NOTSUPPORTED":
        invform.instance.InvoiceNumber = autopk  # Setting auto Generated primary key i.e. Invoice Number
        
        # Checking for Duplicate View
        is_duplicate = Auto_Id_DuplicateChecker(
        ).check_for_duplicate(ProductSale, invform.instance)
        print(f"Duplicate Check: {is_duplicate}")
        
        if is_duplicate:
            messages.error(
                request, "Duplicate record, Data already exist!")
            print("Duplicate record, Data already exist!")
            return redirect(return_url)
    else:
        if autopk == "_ERR_":
            messages.error(
                request, "Error occured, Data was not saved!")
            return redirect(return_url)
        
    pass        
    


