# Generated by Django 3.0 on 2020-06-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firewall', '0002_auto_20190406_2145'),
        ('server', '0008_auto_20200507_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='firewalls',
            field=models.ManyToManyField(related_name='server_relations', to='firewall.Firewall'),
        ),
    ]
