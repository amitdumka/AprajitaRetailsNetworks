# from PIL import Image
# from django.http import HttpResponse

# def print_data_to_thermal_printer(request):
#     # Create a PDF file of the data
#     image = Image.new('RGB', (200, 200), (255, 255, 255))
#     draw = ImageDraw.Draw(image)
#     draw.text((10, 10), 'Hello, world!', (0, 0, 0))

#     # Render the PDF file to the printer
#     response = HttpResponse(content_type='application/pdf')
#     pdf_renderer = PDFRenderer()
#     pdf_renderer.render(image, response)

#     return response


# import escpos

# def print():
#     # Create an ESC/POS printer object
#     printer = escpos.printer.SerialPrinter('/dev/ttyUSB0')

# # Print the data to the printer
#     printer.text('Hello, world!')
#     printer.cut()


# from PIL import Image
# from django.http import HttpResponse
# from .models import Voucher  # Assuming models.py is in the same directory

# def print_voucher_to_thermal_printer(request, voucher_number):
#     # Get the voucher from the database
#     voucher = Voucher.objects.get(VoucherNumber=voucher_number)

#     # Create a PDF file of the voucher data
#     image = Image.new('RGB', (200, 200), (255, 255, 255))
#     draw = ImageDraw.Draw(image)
#     draw.text((10, 10), f'Voucher: {voucher.VoucherNumber}', (0, 0, 0))

#     # Render the PDF file to the printer
#     response = HttpResponse(content_type='application/pdf')
#     pdf_renderer = PDFRenderer()
#     pdf_renderer.render(image, response)

#     return response



# from PIL import Image, ImageDraw
# from django.http import HttpResponse
# from .models import Voucher  # Assuming models.py is in the same directory

# def print_voucher_to_thermal_printer(request, voucher_number):
#     # Get the voucher from the database
#     voucher = Voucher.objects.get(VoucherNumber=voucher_number)

#     # Create an image of the voucher data
#     image = Image.new('RGB', (600, 600), (255, 255, 255))
#     draw = ImageDraw.Draw(image)

#     # Company details
#     company_name = "Aprajita Retails"
#     company_address = "Bhagalpur Road, Dumka"
#     draw.text((10, 10), f'Company Name: {company_name}', (0, 0, 0))
#     draw.text((10, 30), f'Address: {company_address}', (0, 0, 0))

#     # Voucher details
#     draw.text((10, 60), f'Voucher Number: {voucher.VoucherNumber}', (0, 0, 0))
#     draw.text((10, 80), f'Voucher Type: {voucher.get_VoucherType_display()}', (0, 0, 0))
#     draw.text((10, 100), f'Date: {voucher.OnDate}', (0, 0, 0))
#     draw.text((10, 120), f'Slip Number: {voucher.SlipNumber}', (0, 0, 0))
#     draw.text((10, 140), f'Party Name: {voucher.PartyName}', (0, 0, 0))
#     draw.text((10, 160), f'Particulars: {voucher.Particulars}', (0, 0, 0))
#     draw.text((10, 180), f'Amount: {voucher.Amount}', (0, 0, 0))
#     draw.text((10, 200), f'Remarks: {voucher.Remarks}', (0, 0, 0))
#     draw.text((10, 220), f'Employee ID: {voucher.EmployeeId}', (0, 0, 0))
#     draw.text((10, 240), f'Party ID: {voucher.PartyId}', (0, 0, 0))
#     draw.text((10, 260), f'Account Number: {voucher.AccountNumber}', (0, 0, 0))
#     draw.text((10, 280), f'Payment Mode: {voucher.get_PaymentMode_display()}', (0, 0, 0))
#     draw.text((10, 300), f'Payment Details: {voucher.PaymentDetails}', (0, 0, 0))
#     draw.text((10, 320), f'Store ID: {voucher.StoreId}', (0, 0, 0))
#     draw.text((10, 340), f'Store Group ID: {voucher.StoreGroupId}', (0, 0, 0))
#     draw.text((10, 360), f'App Client ID: {voucher.ClientId}', (0, 0, 0))
#     draw.text((10, 380), f'Is Read Only: {voucher.IsReadOnly}', (0, 0, 0))

#     # Render the PDF file to the printer
#     response = HttpResponse(content_type='application/pdf')
#     pdf_renderer = PDFRenderer()
#     pdf_renderer.render(image, response)

#     return response
from PIL import Image, ImageDraw
from django.http import HttpResponse
from accounting.models import Voucher  # Assuming models.py is in the same directory
import inflect  # You'll need to install this library to convert numbers to words

def print_voucher_to_thermal_printer(request, voucher_number):
    # Get the voucher from the database
    voucher = Voucher.objects.get(VoucherNumber=voucher_number)

    # Create an image of the voucher data
    image = Image.new('RGB', (600, 600), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Company details
    company_name = "Aprajita Retails"
    company_address = "Bhagalpur Road, Dumka"
    draw.text((10, 10), f'Company Name: {company_name}', (0, 0, 0))
    draw.text((10, 30), f'Address: {company_address}', (0, 0, 0))

    # Voucher details
    draw.text((10, 60), f'Voucher Number: {voucher.VoucherNumber}', (0, 0, 0))
    draw.text((10, 80), f'Voucher Type: {voucher.get_VoucherType_display()}', (0, 0, 0))
    draw.text((10, 100), f'Date: {voucher.OnDate}', (0, 0, 0))
    draw.text((10, 120), f'Slip Number: {voucher.SlipNumber}', (0, 0, 0))
    draw.text((10, 140), f'Party Name: {voucher.PartyName}', (0, 0, 0))
    draw.text((10, 160), f'Particulars: {voucher.Particulars}', (0, 0, 0))

    # Convert the amount to words
    p = inflect.engine()
    amount_in_words = p.number_to_words(voucher.Amount)
    draw.text((10, 180), f'Amount: {voucher.Amount} ({amount_in_words} rupees)', (0, 0, 0))

    draw.text((10, 200), f'Remarks: {voucher.Remarks}', (0, 0, 0))
    draw.text((10, 220), f'Employee ID: {voucher.EmployeeId}', (0, 0, 0))
    draw.text((10, 240), f'Party ID: {voucher.PartyId}', (0, 0, 0))
    draw.text((10, 260), f'Account Number: {voucher.AccountNumber}', (0, 0, 0))
    draw.text((10, 280), f'Payment Mode: {voucher.get_PaymentMode_display()}', (0, 0, 0))
    draw.text((10, 300), f'Payment Details: {voucher.PaymentDetails}', (0, 0, 0))
    draw.text((10, 320), f'App Client ID: {voucher.ClientId}', (0, 0, 0))

    # Render the PDF file to the printer
    response = HttpResponse(content_type='application/pdf')
    pdf_renderer = PDFRenderer()
    pdf_renderer.render(image, response)

    return response
