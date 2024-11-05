from django.db import models

# Create your models here.

class Home(models.Model):
    description = models.TextField()

    def _str_(self):
        return self.description


class About(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()

    def _str_(self):
        return self.title


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')

    def get_image_display(self):
        return self.image.url if self.image else None


class Service(models.Model):
    icon = models.TextField()
    title = models.CharField(max_length=90)
    description = models.TextField()

    def _str_(self):
        return self.title


class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('product', 'Product'),
        ('branding', 'Branding'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    def _str_(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=40)
    message = models.TextField()

    def _str_(self):
        return self.name


class Client(models.Model):
    photo = models.ImageField(upload_to='images')

    def _str_(self):
        return self.photo.url if self.photo else 'No photo'


class Question(models.Model):
    title = models.TextField()
    description = models.TextField()

    def _str_(self):
        return self.title