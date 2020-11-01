from django.urls import path , include
from .views import add_statement

urlpatterns = [
    path('add_statement', add_statement ,name='add_statement'),

]
