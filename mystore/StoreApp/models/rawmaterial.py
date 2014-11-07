from django.db import models


class RawMaterial(models.Model):
    name = models.CharField("Name", max_length=70)

    class Meta:
        app_label = "StoreApp"
        db_table = "raw_materials"

    def __unicode__(self):
        return self.name
