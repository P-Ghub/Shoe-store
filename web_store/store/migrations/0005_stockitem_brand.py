# Generated by Django 4.2.3 on 2023-07-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_storeitem_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='brand',
            field=models.CharField(default='brand', max_length=200),
        ),
    ]
