import requests
from django.http import HttpResponse

class DataImported:
    def __init__(self, model_name, model, request):
        self.model_name = model_name
        self.model = model
        self.request = request
     
    def import_brand(response, url, model_name):
        
        listofbrands=response.json()
        for brand in listofbrands:
            if not model_name.objects.filter(BrandName=brand['BrandName']).exists():
                model_name.objects.create(BrandName=brand['BrandName'], BrandCode=brand['BrandCode'])
                
        return HttpResponse('Data fetched and stored successfully.')
        
    def import_productType(response, url, model_name):
        
        listofproductType=response.json()
        for productType in listofproductType:
            if not model_name.objects.filter(ProductTypeName=productType['ProductTypeName']).exists():
                model_name.objects.create(
                    ProductTypeName=productType['ProductTypeName'])
        
        return HttpResponse('Data fetched and stored successfully.')    
    
    def import_productSubCategory(response, url, model_name):
        
        listofproductSubCategory=response.json()
        for productSubCategory in listofproductSubCategory:
            if not model_name.objects.filter(SubCategory=productSubCategory['SubCategory']).exists():
                model_name.objects.create(
                    SubCategory=productSubCategory['SubCategory'],
                    ProductCategory=productSubCategory['ProductCategory'],                    
                )
        
        return HttpResponse('Data fetched and stored successfully.')
                

    def fetch_and_store(request, url, model_name):
        # Send a GET request to the API
        # Replace with your API URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            return model_class_handler(response, model_name)
        else:
            return HttpResponse('Failed to fetch data.', status=400)
     
     def model_class_handler(response, model_name):
         
         optName=model_name.meta.verbose_name
         match optName:
             case "Brand":
                 return import_brand(response, url, model_name)
             case "ProductType":
                 return import_productType(response, url, model_name)
             case "ProductSubCategory":
                 return import_productSubCategory(response, url, model_name)
             case _:
                 return HttpResponse('Failed to process as model not found.', status=400)
         pass
        
    def fetch_and_store_temp(request, url, model_name):
        # Send a GET request to the API
        # Replace with your API URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Create a new instance of your model with the data
            # Replace with your fields
            instance = YourModel(field1=data['field1'], field2=data['field2'])
            instance.save()

            return HttpResponse('Data fetched and stored successfully.')
        else:
            return HttpResponse('Failed to fetch data.', status=400)

    
    #Need to make mapping for almost all model. 
    #Then handle for Client, StoreGroup and StoreId. 
    
    # try with brand, productType and productsubcategory
    
    
    
    
