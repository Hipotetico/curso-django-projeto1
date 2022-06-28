from django.urls import include, path
from recipes.views import home, contato, sobre

urlpatterns = [
    
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
