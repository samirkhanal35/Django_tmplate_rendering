from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class detail(models.Model):
        #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        name = models.CharField('Name',blank=True,null=True, max_length=50)
        address = models.CharField('Address', blank=True,null=True,max_length=80)
        mobile_num_1 = models.CharField('Mobile number 1',blank=True,null=True,max_length=12)
        mobile_num_2 = models.CharField('Mobile number 2',blank=True,null=True,max_length=12)
        personal_email = models.CharField('Personal mail',blank=True,null=True,max_length=50)
        email_address = models.CharField('Office Email',blank=True,null=True,max_length=50)
        #email_address = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
        emergency_contact_name = models.CharField('Emergency contact person name',blank=True,null=True, max_length=50)
        emergency_contact_number = models.CharField('Emergency contact person number',blank=True,null=True,max_length=12)
        joined_date = models.CharField('Joined date',blank=True,null=True,max_length=12)
        joining_position = models.CharField('Joining position',blank=True,null=True, max_length=50)
        bank_acc = models.CharField('Bank account number',blank=True,null=True, max_length=50)
        #user_type = models.CharField('user_type',blank=True,null=True,max_length=15)
        #activated = models.BooleanField(default=True)



        def __str__(self):
            return self.name
