#Invovice Trigger

from accounting.models import DailySale
from inventory.models import ProductSale
from accounting.models import CustomerDue


#class InvoiceTrigger:
class InvoiceTrigger:

    def __init__(self, invoice):
        self.invoice = invoice

    def getInvoice(self):
        return self.invoice
    
    #def generateDailySale(productSale, isSave=False):
    def generateDailySale(productSale, edicId, isSave=False):
        dailySale=DailySale.DailySale()
        dailySale.InvoiceNumber=productSale.InvoiceNumber
        dailySale.OnDate=productSale.OnDate
        dailySale.Amount=productSale.TotalPrice
        if productSale.PayMode.name=='Cash':
            dailySale.CashAmount=productSale.TotalPrice
        else:
            dailySale.CashAmount=0
            dailySale.NonCashAmount=productSale.TotalPrice
        dailySale.PayMode=productSale.PayMode
        dailySale.SalesmanId=productSale.SalesmanId
        dailySale.IsDue=False
        dailySale.ManualBill=False
        dailySale.SalesReturn=False
        dailySale.TailoringBill=False
        dailySale.Remarks="Auto Generated"
        dailySale.EDICId=edicId

        if isSave:
            dailySale.save() # consider and option to save to database
        return dailySale
    
    def generateCustomerDue(dailySale, isSave=False):
        customerDue=CustomerDue.CustomerDue()
        customerDue.InvoiceNumber=dailySale.InvoiceNumber
        customerDue.OnDate=dailySale.OnDate
        customerDue.Amount=dailySale.Amount
        customerDue.Paid=False
        customerDue.ClearingDate=None
        if isSave:
            customerDue.save() # consider and option to save to database
        return customerDue

    def updateDueClearing(dueRecover):
       result= CustomerDue.objects.filter(InvoiceNumber=dueRecover.InvoiceNumber).update(ClearingDate=dueRecover.OnDate, Paid=True)
       result=result + DailySale.objects.filter(InvoiceNumber=dueRecover.InvoiceNumber).update(IsDue=False)
       return result
        
#Note - we need to automated for Due Recovery and Customer due creation on DailySale data is updated, created or deleted. 
    #now only happing on create, and due is cleared. but other condition is not stafised. 
    #update this function and make is automated and remove this comment.