from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:produto_id>', views.ver_produto, name='ver_produto'),
    path('signin', views.signin, name='signin'),
]
