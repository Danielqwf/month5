# Generated by Django 4.2.2 on 2023-07-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
