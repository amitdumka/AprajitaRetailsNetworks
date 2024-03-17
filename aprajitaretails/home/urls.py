#Aprajita Retail Home URLS
#Date: 15/02/2024
#Author: Amit Kumar (AKS Lab(India))
# Home URLS : It all url for Home Module

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('/pdf/test/<int:pk>/', views.Pdf_View.as_view(),name='pdf_view'), #for test
    path('/pdf_view/<str:path>', views.pdf_view, name='pdf_view'),

]

