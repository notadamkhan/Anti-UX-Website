from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('1/', views.page1, name='page1'),
    path('2/', views.page2, name='page2'),
    path('3/', views.page3, name='page3'),
    path('4/', views.page4, name='page4'),
    path('5/', views.page5, name='page5'),
]