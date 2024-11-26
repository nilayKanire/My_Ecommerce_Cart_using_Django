from django.db import models

# Create your models here.
# Models me database create kar raha hai product naam ka.
class Product(models.Model):        #Created new class and applied inheritance here
    product_id = models.AutoField  # AutoField - An IntegerField that automatically increments according to available IDs.
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

''' Note :- If we create any table in models.py then we have to register our model in "admin.py" file'''