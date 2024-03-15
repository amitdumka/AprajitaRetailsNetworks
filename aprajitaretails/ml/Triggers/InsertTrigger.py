#Aprajita Retails - NetWork
#Date: 14/03/2024
#Author: Amit Kumar (AKS Labs(India))

#InsertTrigger.py
# Handle Insert Operation, It will be handling extra functions to help in maintaing database

import datetime
from aprajitaretails.core.globalEnums import EmpType
from aprajitaretails.dbs.models.accounting import CustomerDue, DailySale, Salesman

"""
    _description_
    This only create/new operation, it will not be used in update operation    
    _summary_
    Insert Trigger , same as database has trigger function
"""
#TODO: Need to implement messages here so that it can be displayed or have notification some where. 
#TODO: This will handle also for Email creation for events

class InsertTrigger:

    def __init__(self):
        pass
    
    def handle_create(self, model_name, model, request):
        
        match model_name._meta.verbose_name:
            case "SalaryPayment":
                if model.Componet=="Salary":
                    model.Amount=0-model.Amount
                    model.Save()
                
                pass
            case "ProductSale":
                self.handle_dailySale(request, model)
                pass
            case "Employee":
                self.handle_salesman(model, request)
                pass
            case "DueRecovery":
                self.handle_customer_recovery(model, request)
            case "DailySale":
                self.handle_customerdues(model, request)
            case _:
                pass                
        pass
    
    def handle_salesman(self, employee, request):        
        if employee.Category==EmpType.Salesman:
            count=Salesman.objects.filter(ClientId=employee.ClientId).count()+1
            id= f"{employee.StoreId.pk}-{datetime.now().year}-SM-{count}"
            sm= Salesman.Salesman( EmployeeId=employee, IsActive=True, StoreId=employee.StoreId,
                        StoreGroupId=employee.StoreGroupId, Name=employee.SaffName,
                        SalesmanId=id,
                        ClientId=employee.ClientId)          
        else: 
            pass
    
    def handle_dailySale(self, request,productSale):
        
        dailySale= DailySale.DailySale()
        dailySale.InvoiceNumber=productSale.InvoiceNumber
        dailySale.OnDate=productSale.OnDate
        dailySale.Amount=productSale.TotalPrice
        if productSale.PayMode.name=='Cash':
            dailySale.CashAmount=productSale.TotalPrice
        else:
            dailySale.NonCashAmount=productSale.TotalPrice
        dailySale.PayMode=productSale.PayMode
        dailySale.SalesmanId=productSale.SalesmanId
        dailySale.IsDue=False
        dailySale.ManualBill=False
        dailySale.SalesReturn=False
        dailySale.TailoringBill=False
        dailySale.Remarks="Auto Generated"
        if productSale.EDCTerminalId :
            dailySale.EDCTerminalId=productSale.EDCTerminalId
        dailySale.IsReadOnly=False
        dailySale.save()        
        self.handle_customerdues(request,dailySale)
        pass
    
    def handle_customerdues(self,request, dailySale):
        
        if dailySale.IsDue:
            customerDue=CustomerDue.CustomerDue()
            customerDue.InvoiceNumber=dailySale.InvoiceNumber
            customerDue.OnDate=dailySale.OnDate
            customerDue.Amount=dailySale.Amount-dailySale.CashAmount-dailySale.NonCashAmount
            customerDue.Paid=False
            customerDue.ClearingDate=None
            customerDue.save()
        else:
            pass
        
    
    def handle_customer_recovery(self, request, dueRecovery):
        
        if not dueRecovery.PartialPayment:                
            dailysale= DailySale.objects.get(InvoiceNumber=dueRecovery.InvoiceNumber)
            dailysale.IsDue=False
            dailysale.save()
            dues=CustomerDue.objects.get(InvoiceNumber=dueRecovery.InvoiceNumber)
            dues.Paid=True
            dues.ClearingDate=dueRecovery.OnDate
            dues.save()
        else:        
            pass