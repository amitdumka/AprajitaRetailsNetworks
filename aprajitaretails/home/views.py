
# Create your views here.
# Aprajita Retails - A Complete E-SRP Solution
# Author: Amit Kumar (AKS Labs(India))
# Date : 03/03/2024
# Copyright(C) 2024
# All rights reserved

# globalviews.py
# A CRUD View for all Modules
# It will be included in all Modules
# It will used as default for all modules and global view.
# Import  and Required modules
from django.views.decorators.clickjacking import xframe_options_exempt
from django import forms
from django.forms import ValidationError, modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from .viewhanlder import ViewHandler
from dbs.models.clients import Store, StoreGroup,Client
from home.site_settings import SiteSetting
from ml.printing.services import PrinterService
from django.core.exceptions import FieldDoesNotExist

from utils.autoidgenerator import Auto_Id_DuplicateChecker, Auto_Id

#from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget

from home.modelmapping import ModelMapping
from .models import *
#from django_renderpdf.views import PDFView
# Constants and Settings


# Helper Functions
 
 
# CheckInput as Switch
class CheckboxInput(forms.CheckboxInput):
    template_name = 'cbbox.html'
    input_type = 'checkbox'

# enabling datetime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


# Create your views here.

# Create View
# Create record/Data view [Default for all and convert to class view so can be used any where]
@login_required
@xframe_options_exempt
def global_model_create(request, model_class, create_url=None, return_url=None):
    # Add option to enable pk for string type and not visible is not enabled if pk is not string
    widgets = {}
    for field in model_class._meta.fields:
        if isinstance(field, models.DateTimeField):
            widgets[field.name] = DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        elif isinstance(field, models.BooleanField):
            widgets[field.name] = CheckboxInput()

    ModelForm = modelform_factory(
        model_class, fields='__all__', exclude=('IsReadOnly',), widgets=widgets)

    # Now Create function or line to init new data object with default init values. do it here or in model
    instance = None

    if request.method == 'POST':
        form = ModelForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.instance = form.save(commit=False)
                autopk = Auto_Id().get_auto_id(model_class,  form.instance)
                 

                if autopk != "NOTSUPPORTED":
                    form.instance.pk = autopk  # Setting auto Generated primary key
                    # Checking for Duplicate View
                    is_duplicate = Auto_Id_DuplicateChecker(
                    ).check_for_duplicate(model_class, form.instance)
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
                model_data=form.instance
                form.instance.save()
                messages.success(request, f'{form.instance.pk}, Record saved successfully.')
                
                #Handling Printing Service
                pdfFile=PrinterService().print_hanlder(request,model_class, model_data)
                if pdfFile == 'Error Occured':
                    print("Error Occured")
                                    
                elif pdfFile is not None:
                    print("pdfFile is not None")
                    print(pdfFile)
                    return  render(request,'printer.html',{'return_url':create_url,'model_id':form.instance.pk, 'model':form.instance,'pdffile':pdfFile,'title':'Voucher'}) 
                else:
                    print("pdfFile is None")
                    return redirect(create_url, model_id=form.instance.pk)
                
                
            except ValidationError:
                messages.error(
                    request, ' Data was not saved due to validation error')
                return redirect(return_url)
            except ValueError:
                messages.error(
                    request, ' Data was not saved due to error in data')
                return redirect(return_url)
    else:
        try:
            model_class._meta.get_field('Location')
            st = Store.objects.get(pk=request.session.get(SiteSetting.StoreId,"AFMBO"))
            sg= StoreGroup.objects.get(pk=request.session.get(SiteSetting.GroupId,"AFMBO"))        
            instance= model_class(Location=st, StoreGroup=sg , Client=Client.objects.all().first())
            form = ModelForm(instance=instance)
        except FieldDoesNotExist:
            try :
            
                model_class._meta.get_field('StoreGroup')
                sg= StoreGroup.objects.get(pk=request.session.get(SiteSetting.GroupId,"AFMBO"))        
                instance= model_class( StoreGroup=sg , Client=Client.objects.all().first())
                form = ModelForm(instance=instance)
        
            except FieldDoesNotExist:
                try:
                    model_class._meta.get_field('Client')
                    
                    instance= model_class(Client=Client.objects.all().first())
                    form = ModelForm(instance=instance)
                except FieldDoesNotExist:
                     form = ModelForm(instance=instance)
        
        # st = Store.objects.get(pk=request.session.get(SiteSetting.StoreId,"MBO"))
        # sg= StoreGroup.objects.get(pk=request.session.get(SiteSetting.GroupId,"MBO"))        
        # instance= model_class(StoreId=st, StoreGroupId=sg , ClientId=Client.objects.all().first())
        # form = ModelForm(instance=instance)
        
        #form.instance.StoreGroupId=sg
        #form.instance.StoreId=st
        #form.instance.ClientId=request.session.get(SiteSetting.ClientId,None)

    return render(request, 'crud/create.html', {'form': form, 'model': model_class._meta.verbose_name, 'new_record': True, 'create_url': create_url, 'return_url': return_url})


# Update View
# Create record/Data view [Default for all and convert to class view so can be used any where]
@login_required
def global_model_update(request, model_class, model_id, create_url=None, return_url=None):
    # Add option to enable pk for string type and not visible is not enabled if pk is not string
    widgets = {}
    for field in model_class._meta.fields:
        if isinstance(field, models.DateTimeField):
            widgets[field.name] = DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        elif isinstance(field, models.BooleanField):
            widgets[field.name] = CheckboxInput()

    ModelForm = modelform_factory(
        model_class, fields='__all__', exclude=('IsReadOnly',), widgets=widgets)

    if model_id:
        instance = model_class.objects.get(pk=model_id)
        is_new_record = False
    else:
        instance = None
        is_new_record = True
        messages.error("Record id is missing, recheck and try again")
        return redirect(return_url)

    if request.method == 'POST':
        form = ModelForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.instance = form.save(commit=False)
                if model_id:
                    form.instance.save()
                else:
                    form.instance.save(
                        update_fields=[f.name for f in model_class._meta.fields if f.name != 'id'])
                messages.success(request, f'{form.instance.pk}, Record updated successfully.')

                #TODO: ask if you want to print the, or not
                #Handling Printing Service
                PrinterService().handle_service(model_class,form.instance,request)


                return redirect(create_url, model_id=form.instance.pk)
            except ValidationError:
                messages.error(
                    request, ' Data was not updated due to validation error')
                return redirect(return_url)
            except ValueError:
                messages.error(
                    request, ' Data was not update due to error in data')
                return redirect(return_url)
    else:
        form = ModelForm(instance=instance)

    return render(request, 'crud/create.html', {'form': form, 'model': model_class._meta.verbose_name, 'new_record': False, 'create_url': create_url, 'return_url': return_url})


# Delete View
# Delete View : Note: Update this so can handle global delete
class Global_DeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'crud/delete.html'

    def get(self, request, model_name, model_id):
        model_class = ModelMapping.get_model_class(model_name)
        obj = get_object_or_404(model_class, pk=model_id)
        return render(request, self.template_name, {'object': obj, 'model_name': model_name})

    def post(self, request, model_name, model_id):
        model_class = ModelMapping.get_model_class(model_name)
        obj = get_object_or_404(model_class, pk=model_id)
        obj.delete()
        return_url = '/hr/' + model_name + 's'
        return redirect(return_url)


# List View
# Record/Data View for Listing Record


class Global_ListView(LoginRequiredMixin, ListView):
    template_name = 'crud/listpage.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        model_name = kwargs.get('model_class')
        objects = model_name.objects.all()
        #field_names = [field.name for field in model_name._meta.fields]
        field_names=ViewHandler().get_fields(model_name)
        appname = kwargs.get('app_name')
        model = model_name._meta.verbose_name_plural

        paginator = Paginator(objects, 10)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'app_name': appname, 'model_name': kwargs.get('model_name'),   'model': model, 'model_list': page_obj, 'field_names': field_names, 'create_url': kwargs.get('create_url')})

# Detail View
# Default Record/Data Detail View. [Note: Convert to Class based view so code is same]


@login_required
def global_model_display(request, model_name, model_id, return_url=None):
    model = model_name.objects.get(pk=model_id)
    field_names = [field.name for field in model_name._meta.fields]
    return render(request, 'crud/details.html', {'field_names': field_names, 'model': model, 'model_name': model._meta.verbose_name, 'return_url': return_url})

#Printing Redirect Function 

@login_required
def printPdf(request, redirecturl,fromfunc,model_name, model, pdfile):
    pass

def print_redirect(request,redirecturl,model_name,model_obj,fromfunc,pdfile=None):
    optionName=model_name.meta.verbose_name
    is_printing_enabled=False
    
    match optionName:
        case "Voucher":                
            is_printing_enabled=False                
        case "CashVoucher":
                is_printing_enabled=False    
        case "Invoice":
                is_printing_enabled=False 
        case "SalaryPayment":
                is_printing_enabled=False    
        case "AdvanceReceipt": # In Future Merge Salary Payment and Salary Advance Receipt to one as Salary Ledger. 
                is_printing_enabled=False

    if is_printing_enabled :
        #Do Some Things
        #Redirect to HTML Page to print, Trying with render , if not possible then redirect. 
        return render(request,'printer.html',{'redirecturl':redirecturl, 'title':model_name.meta.verbose_name, 'fromfunc':fromfunc, 'model':model_obj,'pdffile':PrinterService().print_model(model_name, model_obj)}) 
        # PrinterService().print_model(model_class, form.instance)
                
        
    else:
         # Simply Redirect to it return page.
        return redirect(redirecturl, model_id=model_obj.pk)
    

    
        
        


# Default View [App module root page]
# Default Dashboard for app


# def index(request):
#     return HttpResponse(f"{app_name}: {app_name}- dashboard is coming soon.")


def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')


def imports(request):
    return render(request, 'apps/imports.html')


def reports(request):
    return render(request, 'apps/reports.html')


def settings(request):
    return render(request, 'apps/settings.html')


# class HelloPDFView(PDFTemplateView):
#     template_name = 'printer.html'

#     base_url = 'file://' + settings.STATIC_ROOT
#     download_filename = 'das.pdf'

#     def get_context_data(self, **kwargs):
#         return super(HelloPDFView, self).get_context_data(
#             pagesize='A4',
#             title='Hi there!',
#             **kwargs
#         )


# class Pdf_View(LoginRequiredMixin, PDFView):
#     template_name = 'printer.html'

#     def get_context_data(self, *args, **kwargs):
#         """Pass some extra context to the template."""
#         context = super().get_context_data(*args, **kwargs)

#         context['shipments'] = Shipment.objects.filter(
#             batch_id=kwargs['pk'],
#         )

#         return context
    
    
@xframe_options_exempt
def pdf_view(request,path):
    try:
        with open(path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
    except FileNotFoundError:
        raise Http404()