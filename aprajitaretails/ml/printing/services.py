import io
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas

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
        
        page.setFont("Helvetica", 24)
        page.drawString(100,750,f'{model.ClientId.Name}')
        page.setFont("Helvetica", 16)
        page.drawString(100,725, f'{model.Client.Address}, {model.Client.City}')
        page.setFont("Helvetica",11)
        page.drawString(100,700,f'{model.Client.Phone}')

        return page
    
    def print_voucher(self, request, model_name, model):
        # Create a file-like buffer to receive PDF data
        #buffer = io.BytesIO() alternate methord

        # Create the PDF object, using the buffer as its "file"
        #p = canvas.Canvas(buffer)
        print(f'model={model_name}')
        os.makedirs(f'./printedfile/{model_name._meta.verbose_name}', exist_ok=True)

        #Create a pdf file 
        fileName=f'{model_name._meta.verbose_name}_{model.pk}.pdf'
        page=canvas.Canvas(fileName)
        print(f'filename={fileName}')
        
        page.setFont("Helvetica",11)
        page.drawString(100, 675, f"Voucher No: {model.pk}")
        page.drawString(100,650, f'Vouher :{model.VoucherType}')
        page.drawString(100,625, f'Date: {model.OnDate}')
        page.drawString(100,600,f'--------------------------------------------------')
        page.drawString(100,575,f'Party: {model.PartyName}')
        page.drawString(100,550, f'Address:_____________________________')
        page.drawString(100,525,f'Particulars: {model.Particulars}')
        page.drawString(100, 500,f'Amount: {model.Amount}')
        page.drawString(100, 475,f'In words:')
        page.drawString(100,450,f'Mode: {model.PaymentMode}')

        page.drawString(100,425,f'Issued By: {str(model.Employee.FirstName)} {str(model.Employee.LastName)}')
        page.drawString(100,375,f'Sign: ________________________________')

        page.drawString(100,300,f'Party Sign:________________________________')



        page.drawString(100,275,f'This is pre-printed voucher, Issuer sign is not requried.')
        page.drawString(100,250,f'All dispute are subject to Jurdiction of {model.Client.ClientCity}')
        
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
    
    def print_salarypayment(self, request, model_name, model):
        # Create a file-like buffer to receive PDF data
        #buffer = io.BytesIO() alternate methord

        # Create the PDF object, using the buffer as its "file"
        #p = canvas.Canvas(buffer)

        #Create a pdf file 
        fileName=f'/printedfile/{model_name.meta_verbose_name}/{model_name.meta.verbose_name}_{model.pk}.pdf'
        page=canvas.Canvas(fileName)
        
        page.setFont("Helvetica",11)
        page.drawString(100, 675, f"Voucher No: {model.pk}")
        page.drawString(100,650, f'Vouher :{model.Component}')
        page.drawString(100,625, f'Date: {model.OnDate}')
        page.drawString(100,600,f'-----------------------------------------')
        page.drawString(100,575,f'Staff: {model.EmployeeId.StaffName}')
        page.drawString(100,550, f'Address:_____________________________')
        page.drawString(100,525,f'Month: {model.SalaryMonth}')
        page.drawString(100, 500,f'Amount: {model.Amount}')
        page.drawString(100, 475,f'In words:')
        page.drawString(100,450,f'Mode: {model.PayMode}')

        page.drawString(100,425,f'Paid To: {model.EmployeeId.StaffName}')
        page.drawString(100,375,f'Sign: ________________________________')

        page.drawString(100,300,f'Issuer Sign:________________________________')



        page.drawString(100,275,f'This is pre-printed voucher, Issuer sign is not requried\nAll dispute are subject to Jurdiction of {model.Client.City}')
        
        # Close the PDF object cleanly, and ensure we're at the end of the buffer
        page.showPage()
        page.save()

        pdf= page.getpdfdata()
        # Get the value of the BytesIO buffer and write it to the response
        #pdf = buffer.getvalue()
        #buffer.close()
        response = FileResponse(pdf, as_attachment=True, filename=fileName)
        return response






# def print_voucher(request, model_name, model_obj):
#     # Create a file-like buffer to receive PDF data
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file"
#     p = canvas.Canvas(buffer)

#     # Get the voucher data from the database
#     voucher = model_name.objects.get(id=1)  # replace with your own query
    
#     #It Can be used to name a pdf file 
#     # filename=f'/printedfiles/{model_name.meta.verbose}/{model_name.meta.versbose}_{model_obj.pk}.pdf'
#     c = canvas.Canvas("voucher.pdf")

#     # Draw the company name and address
#     c.setFont("Helvetica", 24)
#     c.drawString(100, 750, "Aprajita Retail")
#     c.setFont("Helvetica", 16)
#     c.drawString(100, 725, "Bhagalpur Road Dumka")
#     # Draw your PDF
#     # Here's where the PDF generation happens
#     # See the ReportLab documentation for the full list of functionality
#     p.drawString(100, 750, "Aprajita Retails")
#     p.drawString(100, 735, "Bhagalpur Road, Dumka")
#     p.drawString(100, 720, f"Voucher ID: {voucher.id}")
#     p.drawString(100, 705, f"Amount: {voucher.amount}")
#     p.drawString(100, 690, f"Date: {voucher.date}")

#     # Close the PDF object cleanly, and ensure we're at the end of the buffer
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response
#     pdf = buffer.getvalue()
#     buffer.close()
#     response = FileResponse(pdf, as_attachment=True, filename='voucher.pdf')
#     return 

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     #buffer.seek(0)
#     #return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

    