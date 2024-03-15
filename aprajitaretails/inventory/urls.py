#Aprajita Retail inventory URLS
#Date: 15/02/2024
#Author: Amit Kumar (AKS Lab(India))

import uuid
from django.urls import path
 
from dbs.models.inventory import ProductItem, Brand, ProductSubCategory, ProductType, Supplier, Vendor, ProductPurchase, PurchaseItem, Stock
 
from home.views import *
from django.urls import  re_path, register_converter


# Register the UUIDConverter
class UUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        return uuid.UUID(value)

    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

#Pos is also not added EDC
app_name='inventory'

urlpatterns = [
    path("", index, name="index"),
    
#ProductItem
    path('productitem/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': ProductItem, 'create_url':'inventory:productitem_create','model_name':'productitem'},name='productitem_list'),
    path('productitem/update/<str:model_id>/', global_model_update, {'model_class': ProductItem, 'create_url':'inventory:productitem_create' ,'return_url':'inventory:productitem_list'}, name='productitem_create'),
    path('productitem/create/', global_model_create, {'model_class': ProductItem, 'create_url':'inventory:productitem_create' ,'return_url':'inventory:productitem_list'}, name='productitem_create'),
    path('productitem/detail/<str:model_id>/', global_model_display, {'model_name': ProductItem, 'return_url':'inventory:productitem_list'}, name='productitem_detail'),
    
    #Brand
    path('brand/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': Brand, 'create_url':'inventory:brand_create','model_name':'brand'},name='brand_list'),
    path('brand/update/<str:model_id>/', global_model_update, {'model_class': Brand, 'create_url':'inventory:brand_create' ,'return_url':'inventory:brand_list'}, name='brand_create'),
    path('brand/create/', global_model_create, {'model_class': Brand, 'create_url':'inventory:brand_create' ,'return_url':'inventory:brand_list'}, name='brand_create'),
    path('brand/detail/<str:model_id>/', global_model_display, {'model_name': Brand, 'return_url':'inventory:brand_list'}, name='brand_detail'),
    
    #ProductSubCategory
    path('productsubcategory/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': ProductSubCategory, 'create_url':'inventory:productsubcategory_create','model_name':'productsubcategory'},name='productsubcategory_list'),
    path('productsubcategory/update/<str:model_id>/', global_model_update, {'model_class': ProductSubCategory, 'create_url':'inventory:productsubcategory_create' ,'return_url':'inventory:productsubcategory_list'}, name='productsubcategory_create'),
    path('productsubcategory/create/', global_model_create, {'model_class': ProductSubCategory, 'create_url':'inventory:productsubcategory_create' ,'return_url':'inventory:productsubcategory_list'}, name='productsubcategory_create'),
    path('productsubcategory/detail/<str:model_id>/', global_model_display, {'model_name': ProductSubCategory, 'return_url':'inventory:productsubcategory_list'}, name='productsubcategory_detail'),
    
    #ProductType
    path('producttype/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': ProductType, 'create_url':'inventory:producttype_create','model_name':'producttype'},name='producttype_list'),
    path('producttype/update/<str:model_id>/', global_model_update, {'model_class': ProductType, 'create_url':'inventory:producttype_create' ,'return_url':'inventory:producttype_list'}, name='producttype_create'),
    path('producttype/create/', global_model_create, {'model_class': ProductType, 'create_url':'inventory:producttype_create' ,'return_url':'inventory:producttype_list'}, name='producttype_create'),
    path('producttype/detail/<str:model_id>/', global_model_display, {'model_name': ProductType, 'return_url':'inventory:producttype_list'}, name='producttype_detail'),
    
    #Supplier
    path('supplier/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': Supplier, 'create_url':'inventory:supplier_create','model_name':'supplier'},name='supplier_list'),
    path('supplier/update/<str:model_id>/', global_model_update, {'model_class': Supplier, 'create_url':'inventory:supplier_create' ,'return_url':'inventory:supplier_list'}, name='supplier_create'),
    path('supplier/create/', global_model_create, {'model_class': Supplier, 'create_url':'inventory:supplier_create' ,'return_url':'inventory:supplier_list'}, name='supplier_create'),
    path('supplier/detail/<str:model_id>/', global_model_display, {'model_name': Supplier, 'return_url':'inventory:supplier_list'}, name='supplier_detail'),
    
    #Vendor
    path('vendor/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': Vendor, 'create_url':'inventory:vendor_create','model_name':'vendor'},name='vendor_list'),
    path('vendor/update/<str:model_id>/', global_model_update, {'model_class': Vendor, 'create_url':'inventory:vendor_create' ,'return_url':'inventory:vendor_list'}, name='vendor_create'),
    path('vendor/create/', global_model_create, {'model_class': Vendor, 'create_url':'inventory:vendor_create' ,'return_url':'inventory:vendor_list'}, name='vendor_create'),
    path('vendor/detail/<str:model_id>/', global_model_display, {'model_name': Vendor, 'return_url':'inventory:vendor_list'}, name='vendor_detail'),
    
    #ProductPurchase
    path('productpurchase/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': ProductPurchase, 'create_url':'inventory:productpurchase_create','model_name':'productpurchase'},name='productpurchase_list'),
    path('productpurchase/update/<str:model_id>/', global_model_update, {'model_class': ProductPurchase, 'create_url':'inventory:productpurchase_create' ,'return_url':'inventory:productpurchase_list'}, name='productpurchase_create'),
    path('productpurchase/create/', global_model_create, {'model_class': ProductPurchase, 'create_url':'inventory:productpurchase_create' ,'return_url':'inventory:productpurchase_list'}, name='productpurchase_create'),
    path('productpurchase/detail/<str:model_id>/', global_model_display, {'model_name': ProductPurchase, 'return_url':'inventory:productpurchase_list'}, name='productpurchase_detail'),
    
    #PurchaseItem
    path('purchaseitem/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': PurchaseItem, 'create_url':'inventory:purchaseitem_create','model_name':'purchaseitem'},name='purchaseitem_list'),
    path('purchaseitem/update/<str:model_id>/', global_model_update, {'model_class': PurchaseItem, 'create_url':'inventory:purchaseitem_create' ,'return_url':'inventory:purchaseitem_list'}, name='purchaseitem_create'),
    path('purchaseitem/create/', global_model_create, {'model_class': PurchaseItem, 'create_url':'inventory:purchaseitem_create' ,'return_url':'inventory:purchaseitem_list'}, name='purchaseitem_create'),
    path('purchaseitem/detail/<str:model_id>/', global_model_display, {'model_name': PurchaseItem, 'return_url':'inventory:purchaseitem_list'}, name='purchaseitem_detail'),
    
    #Stock
    path('stock/', Global_ListView.as_view(),  { 'app_name':'inventory','model_class': Stock, 'create_url':'inventory:stock_create','model_name':'stock'},name='stock_list'),
    path('stock/update/<str:model_id>/', global_model_update, {'model_class': Stock, 'create_url':'inventory:stock_create' ,'return_url':'inventory:stock_list'}, name='stock_create'),
    path('stock/create/', global_model_create, {'model_class': Stock, 'create_url':'inventory:stock_create' ,'return_url':'inventory:stock_list'}, name='stock_create'),
    path('stock/detail/<str:model_id>/', global_model_display, {'model_name': Stock, 'return_url':'inventory:stock_list'}, name='stock_detail'),
    
    
#Delete pages
    path('delete/<str:model_name>/<uuid:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<str:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<int:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    
]
