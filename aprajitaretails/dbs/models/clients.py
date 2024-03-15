#Aprajita Retails - Network
# Date: 14/03/2024
# Author: Amit Kumar (AKS Labs(India))

#clients.py
# It is model for clients like Client , StoreGroup and Store.

import uuid
from django.db import models 
from django.utils import timezone


#Client model
class Client(models.Model):
            
    ClientId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    ClientName = models.CharField(max_length=100)
    ClientAddress = models.CharField(max_length=100)
    ClientCity=models.CharField(max_length=100)
    ClientEmail = models.EmailField()
    ClientPhone = models.CharField(max_length=14)
    ClientContactPerson = models.CharField(max_length=100)
    ClientStatus = models.CharField(max_length=100)
    StartDate = models.DateTimeField(default= timezone.now)
    EndDate = models.DateTimeField(null=True, blank=True)
    Remarks = models.CharField(max_length=100)
    PAN_Number=models.CharField(max_length=100)
    GST_Number=models.CharField(max_length=100)
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    def __str__(self):
        return self.ClientName+", "+self.ClientAddress

    

#StoreGroup model
class StoreGroup(models.Model):
    class Meta:
        verbose_name = "StoreGroup"
        verbose_name_plural = "StoreGroups"

    StoreGroupId = models.CharField(max_length=15, primary_key=True, db_index=True, unique=True, null=False, editable=True)
    GroupName = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    
    PAN_Number=models.CharField(max_length=100)
    GST_Number=models.CharField(max_length=100)
    PhoneNumber=models.CharField(max_length=100)
    ContactPerson=models.CharField(max_length=100)
    Email=models.EmailField()
    Remarks=models.CharField(max_length=100)
   
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.GroupName
    def save(self, *args, **kwargs):       
        super(StoreGroup, self).save(*args, **kwargs)


#Store model
class Store(models.Model):
        StoreId = models.CharField(primary_key=True, db_index=True, unique=True, null=False, editable=True, max_length=15)
        StoreCode= models.CharField(max_length=15,unique=True)
        StoreName = models.CharField(max_length=100)
        IsActive = models.BooleanField()
        BeginDate = models.DateTimeField(default= timezone.now)
        EndDate = models.DateTimeField(null=True, blank=True)
       
        PAN_Number=models.CharField(max_length=100)
        GST_Number=models.CharField(max_length=100)
        VatNo =models.CharField(max_length=100)

        StoreAddress=models.CharField(max_length=100)
        City=models.CharField(max_length=100)
        State=models.CharField(max_length=100)
        Country=models.CharField(max_length=100)
        ZipCode=models.CharField(max_length=100)
        StoreEmailId=models.EmailField()
        StorePhoneNumber=models.CharField(max_length=100)
        
        StoreManager=models.CharField(max_length=100)
        StoreManegerContactNo=models.CharField(max_length=100)
        
        StoreGroup=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
        Client=models.ForeignKey(Client, on_delete=models.CASCADE)
        
        class Meta:
            verbose_name = "Store"
            verbose_name_plural = "Stores"

        def __str__(self):
            return self.StoreName+", "+self.StoreAddress
