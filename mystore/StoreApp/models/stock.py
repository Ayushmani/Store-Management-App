from django.db import models
from rawmaterial import RawMaterial


class Stock(models.Model):
    raw_materials = models.ForeignKey(RawMaterial)
    quantity = models.IntegerField("Quantity", default=None, blank=False)
    expire_on = models.DateField("Expiry", default=None, blank=False)

    class Meta:
        app_label = "StoreApp"
        db_table = "Stock"

    def __unicode__(self):
        return self.quantity