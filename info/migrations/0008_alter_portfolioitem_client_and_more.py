# Generated by Django 5.1.2 on 2024-11-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_portfolioitem_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='client',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='second_cat',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
