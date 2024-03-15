#Aprajita Retail banking URLS
#Date: 15/02/2024
#Author: Amit Kumar (AKS Lab(India))

import uuid
from django.urls import path
 
from dbs.models.banking import Bank, BankAccount, VendorBankAccount, BankTransaction, BankAccountList, ChequeBook, ChequeIssued, ChequeLog, BankStatement
#from . import views
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
app_name='banking'

urlpatterns = [
    path("", index, name="index"),
    #Bank
    path('bank/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': Bank, 'create_url':'banking:bank_create','model_name':'bank'},name='bank_list'),
    path('bank/update/<str:model_id>/', global_model_update, {'model_class': Bank, 'create_url':'banking:bank_create' ,'return_url':'banking:bank_list'}, name='bank_create'),
    path('bank/create/', global_model_create, {'model_class': Bank, 'create_url':'banking:bank_create' ,'return_url':'banking:bank_list'}, name='bank_create'),
    path('bank/detail/<str:model_id>/', global_model_display, {'model_name': Bank, 'return_url':'banking:bank_list'}, name='bank_detail'),
    
    #BankAccount
    path('bankaccount/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': BankAccount, 'create_url':'banking:bankaccount_create','model_name':'bankaccount'},name='bankaccount_list'),
    path('bankaccount/update/<str:model_id>/', global_model_update, {'model_class': BankAccount, 'create_url':'banking:bankaccount_create' ,'return_url':'banking:bankaccount_list'}, name='bankaccount_create'),
    path('bankaccount/create/', global_model_create, {'model_class': BankAccount, 'create_url':'banking:bankaccount_create' ,'return_url':'banking:bankaccount_list'}, name='bankaccount_create'),
    path('bankaccount/detail/<str:model_id>/', global_model_display, {'model_name': BankAccount, 'return_url':'banking:bankaccount_list'}, name='bankaccount_detail'),
    
    #VendorBankAccount
    path('vendorbankaccount/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': VendorBankAccount, 'create_url':'banking:vendorbankaccount_create','model_name':'vendorbankaccount'},name='vendorbankaccount_list'),
    path('vendorbankaccount/update/<str:model_id>/', global_model_update, {'model_class': VendorBankAccount, 'create_url':'banking:vendorbankaccount_create' ,'return_url':'banking:vendorbankaccount_list'}, name='vendorbankaccount_create'),
    path('vendorbankaccount/create/', global_model_create, {'model_class': VendorBankAccount, 'create_url':'banking:vendorbankaccount_create' ,'return_url':'banking:vendorbankaccount_list'}, name='vendorbankaccount_create'),
    path('vendorbankaccount/detail/<str:model_id>/', global_model_display, {'model_name': VendorBankAccount, 'return_url':'banking:vendorbankaccount_list'}, name='vendorbankaccount_detail'),
    
    #BankTransaction
    path('banktransaction/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': BankTransaction, 'create_url':'banking:banktransaction_create','model_name':'banktransaction'},name='banktransaction_list'),
    path('banktransaction/update/<str:model_id>/', global_model_update, {'model_class': BankTransaction, 'create_url':'banking:banktransaction_create' ,'return_url':'banking:banktransaction_list'}, name='banktransaction_create'),
    path('banktransaction/create/', global_model_create, {'model_class': BankTransaction, 'create_url':'banking:banktransaction_create' ,'return_url':'banking:banktransaction_list'}, name='banktransaction_create'),
    path('banktransaction/detail/<str:model_id>/', global_model_display, {'model_name': BankTransaction, 'return_url':'banking:banktransaction_list'}, name='banktransaction_detail'),
    
    #BankAccountList
    path('bankaccountlist/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': BankAccountList, 'create_url':'banking:bankaccountlist_create','model_name':'bankaccountlist'},name='bankaccountlist_list'),
    path('bankaccountlist/update/<str:model_id>/', global_model_update, {'model_class': BankAccountList, 'create_url':'banking:bankaccountlist_create' ,'return_url':'banking:bankaccountlist_list'}, name='bankaccountlist_create'),
    path('bankaccountlist/create/', global_model_create, {'model_class': BankAccountList, 'create_url':'banking:bankaccountlist_create' ,'return_url':'banking:bankaccountlist_list'}, name='bankaccountlist_create'),
    path('bankaccountlist/detail/<str:model_id>/', global_model_display, {'model_name': BankAccountList, 'return_url':'banking:bankaccountlist_list'}, name='bankaccountlist_detail'),
    
    #ChequeBook
    path('chequebook/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': ChequeBook, 'create_url':'banking:chequebook_create','model_name':'chequebook'},name='chequebook_list'),
    path('chequebook/update/<str:model_id>/', global_model_update, {'model_class': ChequeBook, 'create_url':'banking:chequebook_create' ,'return_url':'banking:chequebook_list'}, name='chequebook_create'),
    path('chequebook/create/', global_model_create, {'model_class': ChequeBook, 'create_url':'banking:chequebook_create' ,'return_url':'banking:chequebook_list'}, name='chequebook_create'),
    path('chequebook/detail/<str:model_id>/', global_model_display, {'model_name': ChequeBook, 'return_url':'banking:chequebook_list'}, name='chequebook_detail'),
    
    #ChequeIssued
    path('chequeissued/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': ChequeIssued, 'create_url':'banking:chequeissued_create','model_name':'chequeissued'},name='chequeissued_list'),
    path('chequeissued/update/<str:model_id>/', global_model_update, {'model_class': ChequeIssued, 'create_url':'banking:chequeissued_create' ,'return_url':'banking:chequeissued_list'}, name='chequeissued_create'),
    path('chequeissued/create/', global_model_create, {'model_class': ChequeIssued, 'create_url':'banking:chequeissued_create' ,'return_url':'banking:chequeissued_list'}, name='chequeissued_create'),
    path('chequeissued/detail/<str:model_id>/', global_model_display, {'model_name': ChequeIssued, 'return_url':'banking:chequeissued_list'}, name='chequeissued_detail'),
    
    #ChequeLog
    path('chequelog/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': ChequeLog, 'create_url':'banking:chequelog_create','model_name':'chequelog'},name='chequelog_list'),
    path('chequelog/update/<str:model_id>/', global_model_update, {'model_class': ChequeLog, 'create_url':'banking:chequelog_create' ,'return_url':'banking:chequelog_list'}, name='chequelog_create'),
    path('chequelog/create/', global_model_create, {'model_class': ChequeLog, 'create_url':'banking:chequelog_create' ,'return_url':'banking:chequelog_list'}, name='chequelog_create'),
    path('chequelog/detail/<str:model_id>/', global_model_display, {'model_name': ChequeLog, 'return_url':'banking:chequelog_list'}, name='chequelog_detail'),
    
    #BankStatement
    path('bankstatement/', Global_ListView.as_view(),  { 'app_name':'banking','model_class': BankStatement, 'create_url':'banking:bankstatement_create','model_name':'bankstatement'},name='bankstatement_list'),
    path('bankstatement/update/<str:model_id>/', global_model_update, {'model_class': BankStatement, 'create_url':'banking:bankstatement_create' ,'return_url':'banking:bankstatement_list'}, name='bankstatement_create'),
    path('bankstatement/create/', global_model_create, {'model_class': BankStatement, 'create_url':'banking:bankstatement_create' ,'return_url':'banking:bankstatement_list'}, name='bankstatement_create'),
    path('bankstatement/detail/<str:model_id>/', global_model_display, {'model_name': BankStatement, 'return_url':'banking:bankstatement_list'}, name='bankstatement_detail'),
    
    #Delete pages
    path('delete/<str:model_name>/<uuid:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<str:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    path('delete/<str:model_name>/<int:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
    
]
