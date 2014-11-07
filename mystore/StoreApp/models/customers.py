from django.db import models


class Customers(models.Model):
    name = models.CharField("Customer Name", max_length=70, default=None, blank=False)
    phone_number = models.IntegerField("Phone Number", max_length=10, blank=True)
    dob = models.DateField("Date of Birth", blank=True)
    address = models.CharField("Delivery Address", max_length=255, blank=False)

    class Meta:
        app_label = "StoreApp"
        db_table = "Customer"

    def __unicode__(self):
        return self.name