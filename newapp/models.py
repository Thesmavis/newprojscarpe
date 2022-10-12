from enum import auto
from django.db import models


class url_list_de(models.Model):
    url= models.URLField()
    date_added = models.DateField(auto_now_add= True)
    

    
    def __str__(self):
         return self.url

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
        
class Product(models.Model):
    sku = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    description=models.TextField(null=True,blank=True)
    mobile_number=models.IntegerField(null=True,blank=True)
    imageUrl=models.URLField(null=True,blank=True) 
    date=models.DateField(auto_now=True)
    end_date=models.DateField()
    # if it is multiple image use another table create FK.

    
    def __str__(self):
        return self.name
     
     
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    mail_Id = models.CharField(max_length=100)
    Phone = models.IntegerField()
    
    def __str__(self):
        return self.name

