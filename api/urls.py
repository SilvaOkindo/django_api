from django.urls import path
from . import views

urlpatterns = [
    path('advocates/', views.advocates_list),
    path('advocates/<str:username>/', views.advocate_details)
]
