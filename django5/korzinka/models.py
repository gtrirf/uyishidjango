from django.db import models

# Create your models here.


class Product(models.Model):
    productname = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.productname