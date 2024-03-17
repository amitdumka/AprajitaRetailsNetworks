import io
import os
from django.http import FileResponse
import inflect
from reportlab.pdfgen import canvas
from django.contrib import messages

from core.globalEnums import PaymentMode, VoucherType

class  PrinterService:
    
    def __init__(self):
        pass
    
    def print_hanlder(self,request, model_name, model_obj):
        
        className=model_name._meta.verbose_name
        print(f'model_name={model_name}')
        print(f'model_obj={model_obj}')
        print(f'className={className}')

        match className:
            case "Voucher":
                print('voucher is seleted')
                return self.print_voucher(request,model_name,model_obj)
            case "CashVoucher":
                return self.print_voucher(request,model_name,model_obj)
            case "SalaryPayment":
                return self.print_salarypayment(request,model_name,model_obj)
            case _:
                return None
        pass

    def pdf_header(self, page, model):
        
        page.setFont("Helvetica", 16)
        page.drawString(100,800,f'{model.Client.ClientName}')
        page.setFont("Helvetica", 12)
        page.drawString(50,775, f'{model.Client.ClientAddress}, {model.Client.ClientCity}')
        page.setFont("Helvetica",11)
        page.drawString(100,750,f'{model.Client.ClientPhone}')
        page.drawString(75,725,f'GSTIN: {model.Client.GST_Number}')
        page.drawString(10,700,f'---------------------------------------------------------------')
        
        return page
    
    def print_voucher(self, request, model_name, model):
        # Create a file-like buffer to receive PDF data
        #buffer = io.BytesIO() alternate methord

        # Create the PDF object, using the buffer as its "file"
        #p = canvas.Canvas(buffer)
        try:
            os.makedirs(f'./printedfile/{model_name._meta.verbose_name}', exist_ok=True)
            #Create a pdf file 
            fileName=f'{model_name._meta.verbose_name}_{model.pk}.pdf'
        
            #Setting Party Information
            ledgerName=model.Party.PartyName
            
            address=None
            if ledgerName is not None:
                print('ledgerName',ledgerName)    
                if model.Party.PartyName=='No Party':
                    address=None 
                else:
                    address=model.Party.Address
                    print('address',address)
         
        
           
            page=self.pdf_header(canvas.Canvas(fileName), model)
            page.setFont("Helvetica",14)            
            page.drawString(100, 675, f'{VoucherType(model.VoucherType).name} ')
            page.setFont("Helvetica",11)
            
            page.drawString(50, 650, f"Voucher No: {model.pk}")
            
            page.drawString(50, 625, f'Date: {model.OnDate.strftime("%B %d, %Y")}')
            page.drawString(10,600,f'--------------------------------------------------------------------')
            page.drawString(50,575,f'Party: {model.PartyName}')
            if address is not None:
                
                page.drawString(50,550, f'Phone:{model.Party.MobileNo}')
                page.drawString(50,525, f'Address: {address}')
                
            else:
                page.drawString(50,550, f'Address:')
                page.drawString(50,525, '_____________________________')
            
            page.drawString(10,515,f'---------------------------------------------------------------')
                
            page.drawString(50,500,f'Particulars: {model.Particulars}')
            page.drawString(50,480,f'Amount: {model.Amount}')
            p = inflect.engine()
            amount_in_words = p.number_to_words(model.Amount)
            
            page.drawString(50, 460,f'({amount_in_words}):')
            page.drawString(50,440,f'Mode: {PaymentMode(model.PaymentMode).name }')

            if model.PaymentMode!=0:
                 page.drawString(50,420,f'Details: {model.PaymentDetails }')                

            page.drawString(50,400,f'Issued By: {str(model.Employee.FirstName)} {str(model.Employee.LastName)}')
            page.drawString(50,350,f'Sign: ________________________________')

            page.drawString(50,275,f'Party Sign:________________________________')



            page.drawString(50,250,f'This is pre-printed voucher, Issuer sign is not requried.')
            page.drawString(50,225,f'All dispute are subject to Jurdiction of {model.Client.ClientCity}')
            
            print('saving file')
            # Close the PDF object cleanly, and ensure we're at the end of the buffer
            page.showPage()
            page.save()
            print('file is saved')

            pdf= page.getpdfdata()
            # Get the value of the BytesIO buffer and write it to the response
            #pdf = buffer.getvalue()
            #buffer.close()
            print('sending printed file')
            response = FileResponse(pdf, as_attachment=True, filename=fileName)
        
            return  fileName
        except Exception as e:
            print(e)
            messages.error(request, f'Error occured while creating pdf {e}')
            return "Error occured"
    
    def print_salarypayment(self, request, model_name, model):
        # Create a file-like buffer to receive PDF data
        #buffer = io.BytesIO() alternate methord

        # Create the PDF object, using the buffer as its "file"
        #p = canvas.Canvas(buffer)

        #Create a pdf file 
        fileName=f'/printedfile/{model_name.meta_verbose_name}/{model_name.meta.verbose_name}_{model.pk}.pdf'
        page=canvas.Canvas(fileName)
        
        page.setFont("Helvetica",11)
        page.drawString(50, 675, f"Voucher No: {model.pk}")
        page.drawString(50,650, f'Vouher :{model.Component}')
        page.drawString(50,625, f'Date: {model.OnDate}')
        page.drawString(50,600,f'-----------------------------------------')
        page.drawString(50,575,f'Staff: {model.EmployeeId.StaffName}')
        page.drawString(50,550, f'Address:_____________________________')
        page.drawString(50,525,f'Month: {model.SalaryMonth}')
        page.drawString(50, 500,f'Amount: {model.Amount}')
        page.drawString(50, 475,f'In words:')
        page.drawString(50,450,f'Mode: {model.PayMode}')

        page.drawString(50,425,f'Paid To: {model.EmployeeId.StaffName}')
        page.drawString(50,375,f'Sign: ________________________________')

        page.drawString(50,300,f'Issuer Sign:________________________________')



        page.drawString(50,275,f'This is pre-printed voucher, Issuer sign is not requried\nAll dispute are subject to Jurdiction of {model.Client.City}')
        
        # Close the PDF object cleanly, and ensure we're at the end of the buffer
        page.showPage()
        page.save()

        pdf= page.getpdfdata()
        # Get the value of the BytesIO buffer and write it to the response
        #pdf = buffer.getvalue()
        #buffer.close()
        response = FileResponse(pdf, as_attachment=True, filename=fileName)
        return response
