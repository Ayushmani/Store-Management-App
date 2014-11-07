from django.db import models


class Products(models.Model):
    product_name = models.CharField("Product Name", max_length=70)
    description = models.CharField("Description", max_length=250)

    class Meta:
        app_label = "StoreApp"
        db_table = "Products"

    def __unicode__(self):
        return self.product_name

