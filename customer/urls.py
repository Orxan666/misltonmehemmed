from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('portfolio/<int:id>/',views.portfolio_details, name='portfolio'),
]
