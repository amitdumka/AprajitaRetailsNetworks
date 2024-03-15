#Aprajita Retails - Networks
#View Handler
#               Mainly for Create and Update view for aprajitaretails app


from django import forms
from django.forms import ValidationError, modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from dbs.models.clients import Store, StoreGroup,Client
from home.site_settings import SiteSetting
from ml.printing.printerservice import PrinterService
from django.core.exceptions import FieldDoesNotExist

from utils.autoidgenerator import Auto_Id_DuplicateChecker, Auto_Id

from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget

from home.modelmapping import ModelMapping
from .models import *
from django_renderpdf.views import PDFView


class ViewHandler:
    def __init__(self ):
        pass
    def handler_update_view(self,form,ModelForm, request,model_class, instance, Model,create_url=None, return_url=None):
        pass
        
    def handle_create_view(self, form,ModelForm, request,model_class, instance,create_url=None, return_url=None):
        if request.method=='POST':
            form = ModelForm(request.POST, instance=instance)
            if form.is_valid():
                try:
                    form.instance=form.save(commit=False)
                    autopk = Auto_Id().get_auto_id(model_class,  form.instance)
                    if autopk != 'NOTSUPPORTED':
                        form.instance.pk = autopk  # Setting auto Generated primary key
                        # Checking for Duplicate View
                        is_duplicate = Auto_Id_DuplicateChecker().check_for_duplicate(model_class, form.instance)
                        print(f"Duplicate Check: {is_duplicate}")
                        if is_duplicate:
                            messages.error(request, "Duplicate record, Data already exist!")
                            print("Duplicate record, Data already exist!")
                            return redirect(return_url)
                    else:
                        if autopk == '_ERR_':
                            messages.error(request, "Error occured, Data was not saved!")
                            return redirect(return_url)
                    form.instance.save()
                    messages.success(request, f'{form.instance.pk}, Record saved successfully.')
                    #TODO: insert Handler for Printer function.
                    return redirect(create_url, model_id=form.instance.pk)
                except ValidationError:
                    messages.error(
                        request, ' Data was not saved due to validation error')
                    return redirect(return_url)
                except ValueError:
                    messages.error(
                        request, ' Data was not saved due to error in data')
                    return redirect(return_url)
        else :  #TODO: Make this in some other function so it can be reused in create and update
            try:
                    model_class._meta.get_field('Location')
                    st = Store.objects.get(pk=request.session.get(SiteSetting.StoreId,"MBO"))
                    sg= StoreGroup.objects.get(pk=request.session.get(SiteSetting.GroupId,"MBO"))        
                    instance= model_class(Location=st, StoreGroup=sg , Client=Client.objects.all().first())
                    form = ModelForm(instance=instance)
            except FieldDoesNotExist:
                    try :                    
                        model_class._meta.get_field('StoreGroup')
                        sg= StoreGroup.objects.get(pk=request.session.get(SiteSetting.GroupId,"MBO"))        
                        instance= model_class( StoreGroup=sg , Client=Client.objects.all().first())
                        form = ModelForm(instance=instance)                
                    except FieldDoesNotExist:
                        try:
                            model_class._meta.get_field('Client')                            
                            instance= model_class(Client=Client.objects.all().first())
                            form = ModelForm(instance=instance)
                        except FieldDoesNotExist:
                            form = ModelForm(instance=instance)
        return render(request, 'crud/create.html', {'form': form, 'model': model_class._meta.verbose_name, 'new_record': True, 'create_url': create_url, 'return_url': return_url})    
         
         
         
         
        