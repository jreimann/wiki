from django.urls import path

from . import views

urlpatterns = [
    path("wiki/<str:page>",views.wiki,name="wikipage"),
    path("", views.index, name="index")
]
