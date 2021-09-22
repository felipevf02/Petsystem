from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('busca/', views.busca, name='busca'),
    path('cad_user', views.form_user, name='form_user'),
    path('cad_product', views.form_product, name='form_product'),
    path('cad_forn', views.form_forn, name='form_forn'),
    path('cad_entrada', views.form_entrada, name='form_entrada'),
    path('cad_saida', views.form_saida, name='form_saida'),
    path('cons_user', views.table_user, name='table_user'),
    path('cons_product', views.table_product, name='table_product'),
    path('cons_forn', views.table_forn, name='table_forn'),
    path('cons_entrada', views.table_entrada, name='table_entrada'),
    path('cons_saida', views.table_saida, name='table_saida'),
    path('signin', views.signin, name='signin'),
]
