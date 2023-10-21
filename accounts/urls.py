from django.urls import path , include
from . import views

urlpatterns = [
    path( 'signin/', views.signin ,name = 'signin' ),
    path( 'logout/', views.logout ,name = 'logout' ),
    path( 'signup/', views.signup ,name = 'signup' ),
    path( 'profile/', views.profile ,name = 'profile' ),
    path( 'fav_product/<int:id>', views.fav_product ,name = 'fav_product' ),
    path( 'show_fav_product', views.show_fav_product ,name = 'show_fav_product' ),
]
