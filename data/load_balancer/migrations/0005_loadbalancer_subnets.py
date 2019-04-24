# Generated by Django 2.2 on 2019-04-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subnet', '0002_auto_20190406_2145'),
        ('load_balancer', '0004_auto_20190411_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadbalancer',
            name='subnets',
            field=models.ManyToManyField(editable=False, related_name='loadbalancer_relations', to='subnet.Subnet'),
        ),
    ]
