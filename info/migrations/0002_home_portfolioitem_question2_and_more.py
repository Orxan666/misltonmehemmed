# Generated by Django 5.1.3 on 2024-11-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('app', 'App'), ('product', 'Product'), ('branding', 'Branding')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='PortfolioImage',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='image',
            new_name='photo',
        ),
    ]
