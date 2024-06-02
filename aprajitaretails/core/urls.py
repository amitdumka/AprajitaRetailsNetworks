#Aprajita Retail Core URLS
#Date: 15/02/2024
#Author: Amit Kumar (AKS Lab(India))

import uuid
from django.urls import path
 
from dbs.models.clients import Client,  Store, StoreGroup
from dbs.models.core import Contact, Customer
from dbs.models.inventory import Tax
from dbs.models.accounting import EDCTerminal 
from home.views import *
from django.urls import  register_converter


# Register the UUIDConverter
class UUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        return uuid.UUID(value)

    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

#Pos is also not added EDC
app_name='core'
urlpatterns = [
    path("", index, name="index"), # It will be dashboard for app or landing page for app or index page
    #Generic Templating 
    
    #Client
    path('clients/', Global_ListView.as_view(),  { 'app_name':'core','model_class': Client,  'model_name':'client',  'create_url':'core:client_create'},name='client_list'),
    path('clients/update/<uuid:model_id>/', global_model_update, {'model_class': Client, 'create_url':'core:client_create' ,'return_url':'core:client_list'}, name='client_create'),
    path('clients/create/', global_model_create, {'model_class': Client, 'create_url':'core:client_create' ,'return_url':'core:client_list'}, name='client_create'),
    path('clients/detail/<uuid:model_id>/', global_model_display, {'model_name': Client, 'return_url':'core:client_list'}, name='client_detail'),
    
    #StoreGroup
    path('storegroups/', Global_ListView.as_view(),  { 'app_name':'core','model_class': StoreGroup, 'create_url':'core:storegroup_create','model_name':'storegroup'},name='storegroup_list'),
    path('storegroups/update/<str:model_id>/', global_model_update, {'model_class': StoreGroup, 'create_url':'core:storegroup_create' ,'return_url':'core:storegroup_list'}, name='storegroup_create'),
    path('storegroups/create/', global_model_create, {'model_class': StoreGroup, 'create_url':'core:storegroup_create' ,'return_url':'core:storegroup_list'}, name='storegroup_create'),
    path('storegroups/detail/<str:model_id>/', global_model_display, {'model_name': StoreGroup, 'return_url':'core:storegroup_list'}, name='storegroup_detail'),

    #Store
    path('stores/', Global_ListView.as_view(),  { 'app_name':'core','model_class': Store, 'create_url':'core:store_create','model_name':'store',},name='store_list'),
    path('stores/update/<str:model_id>/', global_model_update, {'model_class': Store, 'create_url':'core:store_create' ,'return_url':'core:store_list'}, name='store_create'),
    path('store/create/', global_model_create, {'model_class': Store, 'create_url':'core:store_create' ,'return_url':'core:store_list'}, name='store_create'),
    path('stores/detail/<str:model_id>/', global_model_display, {'model_name': Store, 'return_url':'core:store_list'}, name='store_detail'),
    
    #Customer
    path('customers/', Global_ListView.as_view(),  { 'app_name':'core','model_class': Customer, 'create_url':'core:customer_create','model_name':'customer'},name='customer_list'),
    path('customers/update/<str:model_id>/', global_model_update, {'model_class': Customer, 'create_url':'core:customer_create' ,'return_url':'core:customer_list'}, name='customer_create'),
    path('customers/create/', global_model_create, {'model_class': Customer,'create_url':'core:customer_create', 'return_url':'core:customer_list'}, name='customer_create'),
    path('customers/detail/<str:model_id>/', global_model_display, {'model_name': Customer, 'return_url':'core:customer_list'}, name='customer_detail'),
 

    #Tax
    path('taxes/', Global_ListView.as_view(),  { 'app_name':'core','model_class': Tax, 'create_url':'core:tax_create','model_name':'tax'},name='tax_list'),
    path('taxes/update/<uuid:model_id>/', global_model_update, {'model_class': Tax, 'create_url':'core:tax_create' ,'return_url':'core:tax_list'}, name='tax_create'),
    path('taxes/create/', global_model_create, {'model_class': Tax,'create_url':'core:tax_create', 'return_url':'core:tax_list'}, name='tax_create'),
    path('taxes/detail/<int:model_id>/', global_model_display, {'model_name': Tax, 'return_url':'core:tax_list'}, name='tax_detail'),

    #Contact
    path('contacts/', Global_ListView.as_view(),  { 'app_name':'core','model_class': Contact, 'create_url':'core:contact_create','model_name':'contact'},name='contact_list'),
    path('contacts/detail/<int:model_id>/', global_model_display, {'model_name': Contact, 'return_url':'core:contact_list'}, name='contact_detail'),
    path('contacts/update/<int:model_id>/', global_model_update, {'model_class': Contact, 'create_url':'core:contact_create' ,'return_url':'core:contact_list'}, name='contact_create'),
    path('contacts/create/', global_model_create, {'model_class': Contact, 'create_url':'core:contact_create' ,'return_url':'core:contact_list'}, name='contact_create'),
    
    #EDC
    path('pos/', Global_ListView.as_view(),  { 'app_name':'core','model_class': EDCTerminal, 'create_url':'core:edc_create','model_name':'edc'},name='edc_list'),
    path('pos/update/<uuid:model_id>/', global_model_update, {'model_class': EDCTerminal, 'create_url':'core:edc_create' ,'return_url':'core:edc_list'}, name='edc_create'),
    path('pos/create/', global_model_create, {'model_class': EDCTerminal, 'create_url':'core:edc_create' ,'return_url':'core:edc_list'}, name='edc_create'),
    path('pos/detail/<str:model_id>/', global_model_display, {'model_name': EDCTerminal, 'return_url':'core:edc_list'}, name='edc_detail'),

    

    #D
    #Delete pages
    path('delete/<str:model_name>/<str:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<uuid:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<int:model_id>/', Global_DeleteView.as_view(), name='core_delete'),


]

