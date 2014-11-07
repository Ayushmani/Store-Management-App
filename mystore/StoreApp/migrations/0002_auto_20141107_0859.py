# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=70, verbose_name=b'Customer Name')),
                ('phone_number', models.IntegerField(max_length=10, verbose_name=b'Phone Number', blank=True)),
                ('dob', models.DateField(verbose_name=b'Date of Birth', blank=True)),
                ('address', models.CharField(max_length=255, verbose_name=b'Delivery Address')),
            ],
            options={
                'db_table': 'Customer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=True)),
                ('customer', models.ForeignKey(to='StoreApp.Customers')),
            ],
            options={
                'db_table': 'Item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_and_time', models.DateTimeField(default=None, verbose_name=b'Delivery Time and Date')),
                ('location', models.CharField(default=None, max_length=255, verbose_name=b'Location')),
                ('customer', models.ForeignKey(to='StoreApp.Customers')),
            ],
            options={
                'db_table': 'Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=70, verbose_name=b'Product Name')),
                ('description', models.CharField(max_length=250, verbose_name=b'Description')),
            ],
            options={
                'db_table': 'Products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'Name')),
            ],
            options={
                'db_table': 'raw_materials',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=None, verbose_name=b'Quantity')),
                ('products', models.ForeignKey(to='StoreApp.Products')),
                ('raw_materials', models.ForeignKey(to='StoreApp.RawMaterial')),
            ],
            options={
                'db_table': 'Recipe',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=None, verbose_name=b'Quantity')),
                ('expire_on', models.DateField(default=None, verbose_name=b'Expiry')),
                ('raw_materials', models.ForeignKey(to='StoreApp.RawMaterial')),
            ],
            options={
                'db_table': 'Stock',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='item',
            name='order_id',
            field=models.ForeignKey(to='StoreApp.Orders'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='product_id',
            field=models.ForeignKey(to='StoreApp.Products'),
            preserve_default=True,
        ),
    ]
