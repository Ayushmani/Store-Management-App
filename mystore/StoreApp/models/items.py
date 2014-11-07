from django.db import models
from customers import Customers
from orders import Orders
from products import Products


class Item(models.Model):
    order_id = models.ForeignKey(Orders)
    customer = models.ForeignKey(Customers)
    product_id = models.ForeignKey(Products)
    quantity = models.IntegerField(blank=False, default=True)

    class Meta:
        app_label = "StoreApp"
        db_table = "Item"

    def __unicode__(self):
        return self.quantity