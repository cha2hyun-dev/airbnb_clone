# Generated by Django 2.2.5 on 2019-09-26 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20190925_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name': 'House Rule'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room Type'},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='houserule',
            new_name='house_rule',
        ),
    ]
