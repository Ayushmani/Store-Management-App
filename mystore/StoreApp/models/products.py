from django.db import models


class Products(models.Model):
    product_name = models.CharField("Product name", max_length=70)
    description = models.CharField("Description", max_length=250)

    class Meta:
        app_label = "StoreApp"
        db_table = "Products"

