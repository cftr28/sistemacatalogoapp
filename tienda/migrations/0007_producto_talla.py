# Generated by Django 3.2.3 on 2022-08-06 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_auto_20220805_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]