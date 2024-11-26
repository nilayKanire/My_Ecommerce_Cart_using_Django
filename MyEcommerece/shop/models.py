from django.db import models

# Create your models here.
# Models me database create kar raha hai product naam ka.
class Product(models.Model):        #Created new class and applied inheritance here
    product_id = models.AutoField  # AutoField - An IntegerField that automatically increments according to available IDs.
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="0")
    desc = models.CharField(max_length=300 )
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    # Creating method below. no migration is need when we created "Method". it need only when we create a model or update it.
    def __str__(self):
        return self.product_name    # over-writes the product name in admin page.

''' Note :- 1] Whatever the changes we make in our created database/model , after that we need to migrate changes using the command 'python manage.py makemigrations'.
            2] If we create any table in models.py then we have to register our model in "admin.py" file'''



