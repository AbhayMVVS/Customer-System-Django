# Generated by Django 3.2.23 on 2024-04-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20240416_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
