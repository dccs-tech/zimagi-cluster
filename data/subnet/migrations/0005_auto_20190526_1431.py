# Generated by Django 2.2 on 2019-05-26 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subnet', '0004_auto_20190526_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subnet',
            name='subnets',
        ),
        migrations.AddField(
            model_name='subnet',
            name='nat_subnet',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subnet_relation', to='subnet.Subnet'),
        ),
    ]