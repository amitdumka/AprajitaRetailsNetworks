# Aprajita Retail pos URLS
# Date: 15/02/2024
# Author: Amit Kumar (AKS Lab(India))

import uuid
from django.urls import path

from dbs.models.pos import ProductSale, SaleItem, SalePaymentDetail, CardPaymentDetail, CustomerSale, ProductItem

from home.views import *
from django.urls import re_path, register_converter

from pos.views import SaleInvoice_Create_View, SaleInvoice_Update_View


# Register the UUIDConverter
class UUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        return uuid.UUID(value)

    def to_url(self, value):
        return str(value)


register_converter(UUIDConverter, 'uuid')


app_name = 'pos'

urlpatterns = [
    path("", index, name="index"),
    # ProductSale
    path('productsale/', Global_ListView.as_view(),  {'app_name': 'pos', 'model_class': ProductSale,
         'create_url': 'pos:productsale_create', 'model_name': 'productsale'}, name='productsale_list'),
    path('productsale/update/<str:model_id>/', global_model_update,
         {'model_class': ProductSale, 'create_url': 'pos:productsale_create', 'return_url': 'pos:productsale_list'}, name='productsale_create'),
    path('productsale/create/', global_model_update,
         {'model_class': ProductSale, 'create_url': 'pos:productsale_create', 'return_url': 'pos:productsale_list'}, name='productsale_create'),
    path('productsale/detail/<str:model_id>/', global_model_display,
         {'model_name': ProductSale, 'return_url': 'pos:productsale_list'}, name='productsale_detail'),
    
    # ProductSale[Sale's Return]
    path('salereturn/', Global_ListView.as_view(),  {'app_name': 'pos', 'model_class': ProductSale,
         'create_url': 'pos:salereturn_create', 'model_name': 'productsale'}, name='salereturn_list'),
    path('salereturn/update/<str:model_id>/', global_model_update,
         {'model_class': ProductSale, 'create_url': 'pos:salereturn_create', 'return_url': 'pos:salereturn_list'}, name='salereturn_create'),
    path('salereturn/create/', global_model_update,
         {'model_class': ProductSale, 'create_url': 'pos:salereturn_create', 'return_url': 'pos:salereturn_list'}, name='salereturn_create'),
    path('salereturn/detail/<str:model_id>/', global_model_display,
         {'model_name': ProductSale, 'return_url': 'pos:salereturn_list'}, name='salereturn_detail'),


    # ProductItem
    path('productitem/', Global_ListView.as_view(),  {'app_name': 'pos', 'model_class': ProductItem,
         'create_url': 'pos:productitem_create', 'model_name': 'productitem'}, name='productitem_list'),
    path('productitem/update/<str:model_id>/', global_model_update,
         {'model_class': ProductItem, 'create_url': 'pos:productitem_create', 'return_url': 'pos:productitem_list'}, name='productitem_create'),
    path('productitem/create/', global_model_update,
         {'model_class': ProductItem, 'create_url': 'pos:productitem_create', 'return_url': 'pos:productitem_list'}, name='productitem_create'),
    path('productitem/detail/<str:model_id>/', global_model_display,
         {'model_name': ProductItem, 'return_url': 'pos:productitem_list'}, name='productitem_detail'),


    # SaleItem
    path('saleitem/', Global_ListView.as_view(),
         {'app_name': 'pos', 'model_class': SaleItem, 'create_url': 'pos:saleitem_create', 'model_name': 'saleitem'}, name='saleitem_list'),
    path('saleitem/update/<str:model_id>/', global_model_update,
         {'model_class': SaleItem, 'create_url': 'pos:saleitem_create', 'return_url': 'pos:saleitem_list'}, name='saleitem_create'),
    path('saleitem/create/', global_model_update,
         {'model_class': SaleItem, 'create_url': 'pos:saleitem_create', 'return_url': 'pos:saleitem_list'}, name='saleitem_create'),
    path('saleitem/detail/<str:model_id>/', global_model_display,
         {'model_name': SaleItem, 'return_url': 'pos:saleitem_list'}, name='saleitem_detail'),


    # SalePaymentDetail
    path('salepaymentdetail/', Global_ListView.as_view(),  {'app_name': 'pos', 'model_class': SalePaymentDetail,
         'create_url': 'pos:salepaymentdetail_create', 'model_name': 'salepaymentdetail'}, name='salepaymentdetail_list'),
    path('salepaymentdetail/update/<str:model_id>/', global_model_update,
         {'model_class': SalePaymentDetail, 'create_url': 'pos:salepaymentdetail_create', 'return_url': 'pos:salepaymentdetail_list'}, name='salepaymentdetail_create'),
    path('salepaymentdetail/create/', global_model_update,
         {'model_class': SalePaymentDetail, 'create_url': 'pos:salepaymentdetail_create', 'return_url': 'pos:salepaymentdetail_list'}, name='salepaymentdetail_create'),
    path('salepaymentdetail/detail/<str:model_id>/', global_model_display,
         {'model_name': SalePaymentDetail, 'return_url': 'pos:salepaymentdetail_list'}, name='salepaymentdetail_detail'),


    # CardPaymentDetail
    path('cardpaymentdetail/', Global_ListView.as_view(),  {'app_name': 'pos', 'model_class': CardPaymentDetail,
         'create_url': 'pos:cardpaymentdetail_create', 'model_name': 'cardpaymentdetail'}, name='cardpaymentdetail_list'),
    path('cardpaymentdetail/update/<str:model_id>/', global_model_update,
         {'model_class': CardPaymentDetail, 'create_url': 'pos:cardpaymentdetail_create', 'return_url': 'pos:cardpaymentdetail_list'}, name='cardpaymentdetail_create'),
    path('cardpaymentdetail/create/', global_model_update,
         {'model_class': CardPaymentDetail, 'create_url': 'pos:cardpaymentdetail_create', 'return_url': 'pos:cardpaymentdetail_list'}, name='cardpaymentdetail_create'),
    path('cardpaymentdetail/detail/<str:model_id>/', global_model_display,
         {'model_name': CardPaymentDetail, 'return_url': 'pos:cardpaymentdetail_list'}, name='cardpaymentdetail_detail'),


    # CustomerSale
    path('customersale/', Global_ListView.as_view(),  {'app_name': 'pos', 'model_class': CustomerSale,
         'create_url': 'pos:customersale_create', 'model_name': 'customersale'}, name='customersale_list'),
    path('customersale/update/<str:model_id>/', global_model_update,
         {'model_class': CustomerSale, 'create_url': 'pos:customersale_create', 'return_url': 'pos:customersale_list'}, name='customersale_create'),
    path('customersale/create/', global_model_update,
         {'model_class': CustomerSale, 'create_url': 'pos:customersale_create', 'return_url': 'pos:customersale_list'}, name='customersale_create'),
    path('customersale/detail/<str:model_id>/', global_model_display,
         {'model_name': CustomerSale, 'return_url': 'pos:customersale_list'}, name='customersale_detail'),



    # Delete pages
    path('delete/<str:model_name>/<uuid:model_id>/',
         Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<str:model_id>/',
         Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<int:model_id>/',
         Global_DeleteView.as_view(), name='core_delete'),
    
    # Disable due to error is shown
    path('saleinv', SaleInvoice_Create_View,{'title':'Sale Invoice','invType':'Sale','return_url':'pos:productsale_list'}, name='saleinv'),
    path('saleinv/<str:model_id>', SaleInvoice_Update_View,{'title':'Sale Invoice','invType':'sale','return_url':'pos:productsale_list'}, name='saleinv'),

]
