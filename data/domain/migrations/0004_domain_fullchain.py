# Generated by Django 2.2 on 2019-04-05 01:21

from django.db import migrations
import systems.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_domain_certificate_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='fullchain',
            field=systems.models.fields.EncryptedDataField(null=True),
        ),
    ]