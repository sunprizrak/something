# Generated by Django 4.1.4 on 2022-12-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contacts_field1_contacts_field2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]