# Aprajita Retails - Network
# Author: Amit Kumar (AKS Labs(India))
# Date: 4/03/2024

# printerservice.py
# import modules
from PIL import Image, ImageDraw
from django.http import HttpResponse
# Assuming models.py is in the same directory
from dbs.models.accounting import Voucher
import inflect


# You'll need to install this library to convert numbers to words
from dbs.models.clients import Client

# PrinterService Class

class PrinterService:
    # Setting
    # Making Store /Store Group/Client Refernce here.
    # image = Image.new('RGB', (283, 600), (255, 255, 255))  # Adjust the width to fit the 3-inch printer
    # image = Image.new('RGB', (600, 600), (255, 255, 255))
    # image = Image.new('RGB', (189, 600), (255, 255, 255))  # Adjust the width to fit the 2-inch printer
    # Default
    # default setting
    page_length = 600
    page_width = 283  # Adjust the width to fit the 3-inch printer
    page_2inch_width = 189  # Adjust the width to fit the 2-inch printer
    page_3inch_width = 283  # Adjust the width to fit the 3-inch printer
    page_size = "3inch"
    left_margin = 10  # for 3inch and 5 for 2inch

    def __init__(self) -> None:
        pass

    # Handler for service
    # Note: It will be print voucher or other if printing is enabled for entry type.
    def handle_service(self, model_name, model, request):

        optionName = model_name._meta.verbose_name.lower()
        print(optionName)
        match optionName:
            case "voucher":
                return self.voucher_printer(model_name, model, request)
            case "cashvoucher":
                return self.cash_voucher_printer(model_name, model, request)
            case "salarypayment":
                return self.salary_payment_printer(model, request)
            case "productsale":
                return self.invoice_printer(model_name, model, request)
            case "payslip":
                return self.salary_slip_printer(model_name, model, request)
            case _:
                return "NOTSUPPORTED"
    def salary_payment_printer(self, model, request):
        print(model)  # for debugging purpose

        image = Image.new(
            'RGB', (self.page_width, self.page_length), (255, 255, 255))
        draw = self.default_page(image, model.ClientId.pk)

        # Salary Payment  details
        draw.text((self.left_margin, 70), f'Slip Number: {model.SlipNo}', (0, 0, 0))
        draw.text((self.left_margin, 90), f'Month: {model.SalaryMonth}', (0, 0, 0))
        draw.text((self.left_margin, 110), f'Date: {model.OnDate}', (0, 0, 0))
        draw.text((self.left_margin, 130), f'Type: {
                  model.get_SalaryComponet_display()}', (0, 0, 0))
        draw.text((self.left_margin, 150), f'Name: {model.EmployeeId.StaffName}', (0, 0, 0))
        #draw.text((self.left_margin, 170), f'Particulars: {model.Particulars}', (0, 0, 0))

        # Convert the amount to words
        p = inflect.engine()
        amount_in_words = p.number_to_words(model.Amount)
        draw.text((self.left_margin, 190), f'Amount: {model.Amount} ({
                  amount_in_words} rupees)', (0, 0, 0))

        draw.text((self.left_margin, 210), f'Mode: {model.get_PayMode_display()}', (0, 0, 0))
        draw.text((self.left_margin, 230), f'Remarks: {model.Details}', (0, 0, 0))
        draw.text((self.left_margin, 250), f'Company: {model.ClientId}', (0, 0, 0))
        draw.text((self.left_margin, 290), f'Store: {model.StoreId}', (0, 0, 0))

        # Save the image
        print("Saving Image")
        # Render the PDF file to the printer
        response = HttpResponse(content_type='application/pdf')
        pdf_renderer = PDFRenderer()
        pdf_renderer.render(image, response)
        print("Done")
        return response
    

    def cash_voucher_printer(self, model_name, model, request):

        image = Image.new(
            'RGB', (self.page_width, self.page_length), (255, 255, 255))
        draw = self.default_page(image, model.Client.Pk)
        # Voucher details
        draw.text((self.left_margin, 70), f'Voucher Number: {
                  model.VoucherNumber}', (0, 0, 0))
        draw.text((self.left_margin, 90), f'Voucher Type: {
                  model.get_VoucherType_display()}', (0, 0, 0))
        draw.text((self.left_margin, 110), f'Date: {model.OnDate}', (0, 0, 0))
        draw.text((self.left_margin, 130), f'Slip Number: {
                  model.SlipNumber}', (0, 0, 0))
        draw.text((self.left_margin, 150), f'Party Name: {
                  model.PartyName}', (0, 0, 0))
        draw.text((self.left_margin, 170), f'Particulars: {
                  model.Particulars}', (0, 0, 0))

        # Convert the amount to words
        p = inflect.engine()
        amount_in_words = p.number_to_words(model.Amount)
        draw.text((self.left_margin, 190), f'Amount: {model.Amount} ({
                  amount_in_words} rupees)', (0, 0, 0))

        draw.text((self.left_margin, 210), f'Remarks: {
                  model.Remarks}', (0, 0, 0))
        draw.text((self.left_margin, 230), f'Issued By: {
                  model.EmployeeId}', (0, 0, 0))
        draw.text((self.left_margin, 250), f'Ledger: {
                  model.PartyId}', (0, 0, 0))
        draw.text((self.left_margin, 290), f'Payment Mode: Cash', (0, 0, 0))
        draw.text((self.left_margin, 330), f'Company: {
                  model.ClientId}', (0, 0, 0))

        # Render the PDF file to the printer
        response = HttpResponse(content_type='application/pdf')
        pdf_renderer = PDFRenderer()
        pdf_renderer.render(image, response)
        return response

    def voucher_printer(self, model_name, model, request):
        image = Image.new(
            'RGB', (self.page_width, self.page_length), (255, 255, 255))
        draw = self.default_page(image, model.Client.Pk)

        # Voucher details
        draw.text((self.left_margin, 70), f'Voucher Number: {
                  model.VoucherNumber}', (0, 0, 0))
        draw.text((self.left_margin, 90), f'Voucher Type: {
                  model.get_VoucherType_display()}', (0, 0, 0))
        draw.text((self.left_margin, 110), f'Date: {model.OnDate}', (0, 0, 0))
        draw.text((self.left_margin, 130), f'Slip Number: {
                  model.SlipNumber}', (0, 0, 0))
        draw.text((self.left_margin, 150), f'Party Name: {
                  model.PartyName}', (0, 0, 0))
        draw.text((self.left_margin, 170), f'Particulars: {
                  model.Particulars}', (0, 0, 0))

        # Convert the amount to words
        p = inflect.engine()
        amount_in_words = p.number_to_words(model.Amount)
        draw.text((self.left_margin, 190), f'Amount: {
                  model.Amount} ({amount_in_words} rupees)', (0, 0, 0))

        draw.text((self.left_margin, 210), f'Remarks: {model.Remarks}', (0, 0, 0))
        draw.text((self.left_margin, 230), f'Issued By: {
                  model.EmployeeId}', (0, 0, 0))
        draw.text((self.left_margin, 250), f'Ledger: {model.PartyId}', (0, 0, 0))
        draw.text((self.left_margin, 270), f'Account Number: {
                  model.AccountNumber}', (0, 0, 0))
        draw.text((self.left_margin, 290), f'Payment Mode: {
                  model.get_PaymentMode_display()}', (0, 0, 0))
        draw.text((self.left_margin, 310), f'Payment Details: {
                  model.PaymentDetails}', (0, 0, 0))
        draw.text((self.left_margin, 330), f'Company: {
                  model.ClientId}', (0, 0, 0))

        # Render the PDF file to the printer
        response = HttpResponse(content_type='application/pdf')
        pdf_renderer = PDFRenderer()
        pdf_renderer.render(image, response)
        return response
    

    
    def invoice_printer(self, model_name, model, request):
        pass

    def salary_slip_printer(self, model, request):
        pass

   
    def default_page(self,image, appclinetid):
        if image is None:
            image = Image.new(
                'RGB', (self.page_width, self.page_length), (255, 255, 255))

        draw = ImageDraw.Draw(image)

        client = Client.objects.get(pk=appclinetid)

        # Company details
        company_name = client.ClientName
        company_address = f'{client.ClientAddress}, {client.ClientCity}'
        company_contact = f'Ph: {client.ClientPhone}'
        draw.text((self.left_margin, 10), f'Company Name: {company_name}', (0, 0, 0))
        draw.text((self.left_margin, 30), f'Address: {company_address}', (0, 0, 0))
        draw.text((self.left_margin, 50), f'Phone: {company_contact}', (0, 0, 0))

        return draw



# from reportlab.pdfgen import canvas

# def print_to_printer(instance):
#     # Create a new PDF file
#     c = canvas.Canvas("voucher.pdf")

#     # Draw the company name and address
#     c.setFont("Helvetica", 24)
#     c.drawString(100, 750, "Aprajita Retail")
#     c.setFont("Helvetica", 16)
#     c.drawString(100, 725, "Bhagalpur Road Dumka")

#     # Here you would draw the rest of your voucher data.
#     # This is highly dependent on what 'instance' is.
#     # data = str(instance)
#     # c.drawString(100, 700, data)

#     # Save the PDF file
#     c.save()

#     # Now you can send the PDF to the printer.
#     # This is highly dependent on your specific printer and network setup.
#     # You might use the 'lp' command on Unix-like systems, for example.
#     os.system('lp voucher.pdf')