from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()  # amader router 


router.register('list', views.BlogViewset,) 
router.register('reviews', views.ReviewViewset,) 
router.register('categorie', views.CategorieViewset,) 


urlpatterns = [
    path('', include(router.urls)),
]