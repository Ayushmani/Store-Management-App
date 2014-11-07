from django.db import models
from rawmaterial import RawMaterial
from products import Products


class Recipe(models.Model):
    raw_materials = models.ForeignKey(RawMaterial)
    products = models.ForeignKey(Products)
    quantity = models.IntegerField("Quantity", default=None, blank=False)

    class Meta:
        app_label = "StoreApp"
        db_table = "Recipe"

    def __unicode__(self):
        return self.products
