from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('costume/<slug:slug>/', views.costume_detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('order/success/', views.order_success, name='order_success'),
]
