# Generated by Django 4.2.4 on 2023-08-30 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_rename_item_color_iteminfo_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iteminfo',
            old_name='color',
            new_name='item_color',
        ),
        migrations.RenameField(
            model_name='iteminfo',
            old_name='image',
            new_name='item_image',
        ),
        migrations.RenameField(
            model_name='iteminfo',
            old_name='description',
            new_name='item_name',
        ),
    ]
