from django.db import models

# Create your models here.

class Register(models.Model):
    TYPE=[("", "Select Account Type"),("Installer ", "Installer "),('Reseller','Reseller')]
    full_name=models.CharField(max_length=255)
    email=models.EmailField()
    contact=models.CharField(max_length=255)
    account_type=models.CharField(choices=TYPE, max_length=10, default='')
    post_code=models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    about_company=models.TextField(max_length=255)

    def __str__(self):
        return f"{self.company_name} - {self.full_name}"