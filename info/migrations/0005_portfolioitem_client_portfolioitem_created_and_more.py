# Generated by Django 5.1.2 on 2024-11-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_portfolioitem_delete_portfolioimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='client',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='second_cat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='category',
            field=models.CharField(choices=[('app', 'App'), ('product', 'Product'), ('branding', 'Branding')], max_length=30),
        ),
    ]
