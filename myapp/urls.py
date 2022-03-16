from django.urls import path
from . import views
urlpatterns = [
  path('',views.signup),
  path('dashboard/',views.dashboard),
  path('membership/',views.membership),
  path('bill/',views.bill),
  path('customer/', views.customer),
  path('signup/',views.signup),
  path('invoice/',views.invoice)
  
]