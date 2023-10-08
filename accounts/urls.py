from django.urls import path , include
from . import views

urlpatterns = [
    path( 'signin/', views.signin ,name = 'signin' ),
    path( 'signup/', views.signup ,name = 'signup' ),
    path( 'profile/', views.profile ,name = 'profile' ),
]
