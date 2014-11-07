from django.db import models
from customers import Customers


class Orders(models.Model):
    customer = models.ForeignKey(Customers)
    date_and_time = models.DateTimeField("Delivery Time and Date", default=None, blank=False)
    location = models.CharField("Location", default=None, blank=False)

    class Meta:
        app_label = "StoreApp"
        db_table = "Orders"

    def __unicode__(self):
        return self.date_and_time