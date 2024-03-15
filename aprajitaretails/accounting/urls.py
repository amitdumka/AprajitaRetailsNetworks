#Aprajita Retail accounting URLS
#Date: 15/02/2024
#Author: Amit Kumar (AKS Lab(India))

import uuid
from django.urls import path
from dbs.models.accounting import Voucher, CashVoucher, CashDetail, CustomerDue, DueRecovery, DailySale, TransactionMode, Salesman, Party, LedgerGroup
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
app_name='accounting'

urlpatterns = [
    path("", index, name="index"),
    
#Voucher
    path('voucher/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': Voucher, 'create_url':'accounting:voucher_create','model_name':'voucher'},name='voucher_list'),
    path('voucher/update/<str:model_id>/', global_model_update, {'model_class': Voucher, 'create_url':'accounting:voucher_create' ,'return_url':'accounting:voucher_list'}, name='voucher_create'),
    path('voucher/create/', global_model_create, {'model_class': Voucher, 'create_url':'accounting:voucher_create' ,'return_url':'accounting:voucher_list'}, name='voucher_create'),
    path('voucher/detail/<str:model_id>/', global_model_display, {'model_name': Voucher, 'return_url':'accounting:voucher_list'}, name='voucher_detail'),
    
#CashVoucher
    path('cashvoucher/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': CashVoucher, 'create_url':'accounting:cashvoucher_create','model_name':'cashvoucher'},name='cashvoucher_list'),
    path('cashvoucher/update/<str:model_id>/', global_model_update, {'model_class': CashVoucher, 'create_url':'accounting:cashvoucher_create' ,'return_url':'accounting:cashvoucher_list'}, name='cashvoucher_create'),
    path('cashvoucher/create/', global_model_create, {'model_class': CashVoucher, 'create_url':'accounting:cashvoucher_create' ,'return_url':'accounting:cashvoucher_list'}, name='cashvoucher_create'),
    path('cashvoucher/detail/<str:model_id>/', global_model_display, {'model_name': CashVoucher, 'return_url':'accounting:cashvoucher_list'}, name='cashvoucher_detail'),
    
#CashDetail
    path('cashdetail/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': CashDetail, 'create_url':'accounting:cashdetail_create','model_name':'cashdetail'},name='cashdetail_list'),
    path('cashdetail/update/<str:model_id>/', global_model_update, {'model_class': CashDetail, 'create_url':'accounting:cashdetail_create' ,'return_url':'accounting:cashdetail_list'}, name='cashdetail_create'),
    path('cashdetail/create/', global_model_create, {'model_class': CashDetail, 'create_url':'accounting:cashdetail_create' ,'return_url':'accounting:cashdetail_list'}, name='cashdetail_create'),
    path('cashdetail/detail/<str:model_id>/', global_model_display, {'model_name': CashDetail, 'return_url':'accounting:cashdetail_list'}, name='cashdetail_detail'),
    
#CustomerDue
    path('customerdue/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': CustomerDue, 'create_url':'accounting:customerdue_create','model_name':'customerdue'},name='customerdue_list'),
    path('customerdue/update/<str:model_id>/', global_model_update, {'model_class': CustomerDue, 'create_url':'accounting:customerdue_create' ,'return_url':'accounting:customerdue_list'}, name='customerdue_create'),
    path('customerdue/create/', global_model_create, {'model_class': CustomerDue, 'create_url':'accounting:customerdue_create' ,'return_url':'accounting:customerdue_list'}, name='customerdue_create'),
    path('customerdue/detail/<str:model_id>/', global_model_display, {'model_name': CustomerDue, 'return_url':'accounting:customerdue_list'}, name='customerdue_detail'),
    
#DueRecovery
    path('due_recovery/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': DueRecovery, 'create_url':'accounting:due_recovery_create','model_name':'due_recovery'},name='due_recovery_list'),
    path('due_recovery/update/<str:model_id>/', global_model_update, {'model_class': DueRecovery, 'create_url':'accounting:due_recovery_create' ,'return_url':'accounting:due_recovery_list'}, name='due_recovery_create'),
    path('due_recovery/create/', global_model_create, {'model_class': DueRecovery, 'create_url':'accounting:due_recovery_create' ,'return_url':'accounting:due_recovery_list'}, name='due_recovery_create'),
    path('due_recovery/detail/<str:model_id>/', global_model_display, {'model_name': DueRecovery, 'return_url':'accounting:due_recovery_list'}, name='due_recovery_detail'),
    
#DailySale
    path('daily_sale/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': DailySale, 'create_url':'accounting:daily_sale_create','model_name':'daily_sale'},name='daily_sale_list'),
    path('daily_sale/update/<str:model_id>/', global_model_update, {'model_class': DailySale, 'create_url':'accounting:daily_sale_create' ,'return_url':'accounting:daily_sale_list'}, name='daily_sale_create'),
    path('daily_sale/create/', global_model_create, {'model_class': DailySale, 'create_url':'accounting:daily_sale_create' ,'return_url':'accounting:daily_sale_list'}, name='daily_sale_create'),
    path('daily_sale/detail/<str:model_id>/', global_model_display, {'model_name': DailySale, 'return_url':'accounting:daily_sale_list'}, name='daily_sale_detail'),
    
#TransactionMode
    path('transactionmode/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': TransactionMode, 'create_url':'accounting:transactionmode_create','model_name':'transactionmode'},name='transactionmode_list'),
    path('transactionmode/update/<str:model_id>/', global_model_update, {'model_class': TransactionMode, 'create_url':'accounting:transactionmode_create' ,'return_url':'accounting:transactionmode_list'}, name='transactionmode_create'),
    path('transactionmode/create/', global_model_create, {'model_class': TransactionMode, 'create_url':'accounting:transactionmode_create' ,'return_url':'accounting:transactionmode_list'}, name='transactionmode_create'),
    path('transactionmode/detail/<str:model_id>/', global_model_display, {'model_name': TransactionMode, 'return_url':'accounting:transactionmode_list'}, name='transactionmode_detail'),
    
#Salesman
    path('salesman/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': Salesman, 'create_url':'accounting:salesman_create','model_name':'salesman'},name='salesman_list'),
    path('salesman/update/<str:model_id>/', global_model_update, {'model_class': Salesman, 'create_url':'accounting:salesman_create' ,'return_url':'accounting:salesman_list'}, name='salesman_create'),
    path('salesman/create/', global_model_create, {'model_class': Salesman, 'create_url':'accounting:salesman_create' ,'return_url':'accounting:salesman_list'}, name='salesman_create'),
    path('salesman/detail/<str:model_id>/', global_model_display, {'model_name': Salesman, 'return_url':'accounting:salesman_list'}, name='salesman_detail'),
    
#Party
    path('party/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': Party, 'create_url':'accounting:party_create','model_name':'party'},name='party_list'),
    path('party/update/<str:model_id>/', global_model_update, {'model_class': Party, 'create_url':'accounting:party_create' ,'return_url':'accounting:party_list'}, name='party_create'),
    path('party/create/', global_model_create, {'model_class': Party, 'create_url':'accounting:party_create' ,'return_url':'accounting:party_list'}, name='party_create'),
    path('party/detail/<str:model_id>/', global_model_display, {'model_name': Party, 'return_url':'accounting:party_list'}, name='party_detail'),
    
#LedgerGroup
    path('ledgergroup/', Global_ListView.as_view(),  { 'app_name':'accounting','model_class': LedgerGroup, 'create_url':'accounting:ledgergroup_create','model_name':'ledgergroup'},name='ledgergroup_list'),
    path('ledgergroup/update/<str:model_id>/', global_model_update, {'model_class': LedgerGroup, 'create_url':'accounting:ledgergroup_create' ,'return_url':'accounting:ledgergroup_list'}, name='ledgergroup_create'),
    path('ledgergroup/create/', global_model_create, {'model_class': LedgerGroup, 'create_url':'accounting:ledgergroup_create' ,'return_url':'accounting:ledgergroup_list'}, name='ledgergroup_create'),
    path('ledgergroup/detail/<str:model_id>/', global_model_display, {'model_name': LedgerGroup, 'return_url':'accounting:ledgergroup_list'}, name='ledgergroup_detail'),
    


#Delete pages
    path('delete/<str:model_name>/<uuid:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<str:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<int:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    
]
