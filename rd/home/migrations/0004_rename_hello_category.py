# Generated by Django 4.1.7 on 2023-04-07 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_hello_delete_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hello',
            new_name='Category',
        ),
    ]