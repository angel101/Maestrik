from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('clusterUser', views.clusterUser, name='clusterUser'),
    path('upSellRecomnedations', views.upSellingProduct, name='upSellRecomnedations')
]