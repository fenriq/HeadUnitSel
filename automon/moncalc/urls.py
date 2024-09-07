from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result),
    path('result.negative', views.result_negative),
]