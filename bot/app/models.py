from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    phone = PhoneNumberField(null=False, blank=False)
    messages = models.TextField(null=True, blank=True,default="message")

    # def __str__(self):
    #     return self.first_name