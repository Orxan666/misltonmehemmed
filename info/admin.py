from django.contrib import admin
from .models import *

# Register your models here.  

class PortfolioItemAdmin(admin.ModelAdmin):
    list_display =('title',)
    search_fields =('title',)
admin.site.register(PortfolioItem,PortfolioItemAdmin)
admin.site.register(About)
admin.site.register(AboutImage)
admin.site.register(Service)
admin.site.register(Contact) 
admin.site.register(Question2)
admin.site.register(Client)
admin.site.register(Home)
