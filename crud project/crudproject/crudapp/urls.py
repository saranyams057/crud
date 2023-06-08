from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:crudid>/',views.delete,name="delete"),
    path('cbvindex/',views.Itemlistview.as_view(),name='cbvhome'),
]