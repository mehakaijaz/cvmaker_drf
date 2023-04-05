from django.db import models


#STATE_CHOICE= (())
# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    #state=models.CharField(choices=STATE_CHOICE,max_length=50)
    gender=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images',blank=True)
    location=models.CharField(max_length=200)
    rdocs=models.FileField(upload_to='rdocs',blank=True)