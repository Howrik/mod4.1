# Generated by Django 4.2.2 on 2023-07-29 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]