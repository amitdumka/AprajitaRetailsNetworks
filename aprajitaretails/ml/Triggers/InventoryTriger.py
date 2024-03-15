#Inventory Triggers

#list of Triggers
#1. Stock Update on Sale of Item or Purchase of Item
#2. Stock Creation on Purchase Of New Item 
#3  Invoice Printing on Sale Invoice. 
#4 Purchase Inward Summary on Purchase Invoice.

from django.db.models import F
from inventory.models import Stock
from inventory.models import ProductItem
class InventoryTrigger:
    def __init__(self):
        pass
    def StockUpdate(storeid, barcode , qty ,isSale=True):
        if isSale:
            Stock.objects.filter(StoreId=storeid, Barcode=barcode).update(SoldQty=F('SoldQty')+qty)
        else:
            Stock.objects.filter(StoreId=storeid, Barcode=barcode).update(PurchaseQty=F('PurchaseQty')+qty)
        pass
    def InvoicePrinting(self):
        pass
    def PurchaseInwardSummary(self):
        pass
    def StockCreation(productItem,storeid, qty,isSale=False,isSave=False):
        stock= Stock()
        stock.Barcode=productItem.Barcode
        stock.CostPrice=productItem.CostPrice
        stock.MRP=productItem.MRP
        stock.Unit=productItem.Unit
        if isSale:
            stock.PurchaseQty=0
            stock.SoldQty=qty
        else:
            stock.PurchaseQty=qty
            stock.SoldQty=0
        stock.HoldQty=0
        stock.MultiPrice=False

        stock.StoreId=storeid
        stock.Product=productItem
        if isSave:
            stock.save()
        return stock


#Note Tempeted Function for futher help
    def generate_pdf(request):
        response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='book_catalog.pdf')
        return response

    # Generate PDF file this generic function to create pdf and can be use for item catalog
    def generate_pdf_file():
        from io import BytesIO
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
    
        # Create a PDF document
        books = Stock.objects.all()
        p.drawString(100, 750, "Book Catalog")
    
        y = 700
        for book in books:
            p.drawString(100, y, f"Title: {book.title}")
            p.drawString(100, y - 20, f"Author: {book.author}")
            p.drawString(100, y - 40, f"Year: {book.publication_year}")
            y -= 60
    
        p.showPage()
        p.save()
    
        buffer.seek(0)
        return buffer
        