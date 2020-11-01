from django.urls import path , include
from .views import index , signin , signup , signout


urlpatterns = [
    path('', index ,name='index'),
    path('signin', signin , name='signin'),
    path('signup',signup, name='signup'),
    path('signout',signout,name='signout'),
]
