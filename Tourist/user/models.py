from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=100,null=True)
    Address=models.CharField(max_length=400,null=True)
    Subject=models.CharField(max_length=100,null=True)
    Message=models.TextField(null=True)

    def __str__(self):
        return self.Name

class tbl_gallery(models.Model):
    picture=models.ImageField(upload_to='static/picture/',null=True)

class tbl_register(models.Model):
    name=models.CharField(max_length=58,null=True)
    email=models.EmailField(primary_key=True)
    mobile=models.CharField(max_length=12,null=True)
    password=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=20,null=True)
    city=models.CharField(max_length=60,null=True)
    address=models.TextField(null=True)
