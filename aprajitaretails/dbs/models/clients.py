#Aprajita Retails - Network
# Date: 14/03/2024
# Author: Amit Kumar (AKS Labs(India))

#clients.py
# It is model for clients like Client , StoreGroup and Store.

import uuid
from django.db import models 
from django.utils import timezone

class ClientBase(models.Model):
  #  Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=100)
    Address= models.CharField(max_length=100, default="Dumka")
    City=models.CharField(max_length=100, default="Dumka")
    State=models.CharField(max_length=100, default="Jharkhand")
    Country=models.CharField(max_length=100, default="India")
    ZipCode=models.CharField(max_length=100, default="814101")
    Email = models.EmailField()
    Phone = models.CharField(max_length=14)
    PANNumber=models.CharField(max_length=100)
    GSTIN=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)
    Remarks=models.CharField(max_length=200, null=True, blank=True)
    ContactPerson=models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.Name+", "+self.Address

#Client model
class Client(ClientBase):
            
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    # ClientName = models.CharField(max_length=100)
    # ClientAddress = models.CharField(max_length=100)
    # ClientCity=models.CharField(max_length=100)
    # ClientEmail = models.EmailField()
    # ClientPhone = models.CharField(max_length=14)
    # ClientContactPerson = models.CharField(max_length=100)
    # ClientStatus = models.BooleanField(default=True)
    StartDate = models.DateTimeField(default= timezone.now)
    EndDate = models.DateTimeField(null=True, blank=True)
    # Remarks = models.CharField(max_length=100)
    # PAN_Number=models.CharField(max_length=100)
    # GST_Number=models.CharField(max_length=100)
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    # def __str__(self):
    #     return self.ClientName+", "+self.ClientAddress

    

#StoreGroup model
class StoreGroup(ClientBase):
    class Meta:
        verbose_name = "StoreGroup"
        verbose_name_plural = "StoreGroups"

    Id = models.CharField(max_length=15, primary_key=True, db_index=True, unique=True, null=False, editable=True)
    # GroupName = models.CharField(max_length=100)
    # Status = models.CharField(max_length=100)
    
    # PAN_Number=models.CharField(max_length=100)
    # GST_Number=models.CharField(max_length=100)
    # PhoneNumber=models.CharField(max_length=100)
    # ContactPerson=models.CharField(max_length=100)
    # Email=models.EmailField()
    # Remarks=models.CharField(max_length=100)
   
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.GroupName
    def save(self, *args, **kwargs):       
        super(StoreGroup, self).save(*args, **kwargs)


#Store model
class Store(ClientBase):
        Id = models.CharField(primary_key=True, db_index=True, unique=True, null=False, editable=True, max_length=15)
        StoreCode= models.CharField(max_length=15,unique=True)
        # StoreName = models.CharField(max_length=100)
        # Active = models.BooleanField(default=True)
        BeginDate = models.DateTimeField(default= timezone.now)
        EndDate = models.DateTimeField(null=True, blank=True)
       
        # PAN_Number=models.CharField(max_length=100)
        # GST_Number=models.CharField(max_length=100)
        #VatNo =models.CharField(max_length=100)

        # StoreAddress=models.CharField(max_length=100)
        # City=models.CharField(max_length=100, default="Dumka")
        # State=models.CharField(max_length=100, default="Jharkhand")
        # Country=models.CharField(max_length=100, default="India")
        # ZipCode=models.CharField(max_length=100, default="814101")
        # StoreEmailId=models.EmailField()
        # StorePhoneNumber=models.CharField(max_length=100)
        
        StoreManager=models.CharField(max_length=100)
        StoreManegerContactNo=models.CharField(max_length=100)
        
        StoreGroup=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
        Client=models.ForeignKey(Client, on_delete=models.CASCADE)
        
        class Meta:
            verbose_name = "Store"
            verbose_name_plural = "Stores"

        # def __str__(self):
        #     return self.StoreName+", "+self.StoreAddress
