from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('env/', views.env, name='env'),
    path('', views.product_list, name='product_list'),
    path('show/', views.show_sql, name='show'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('create/<str:name>/', views.create_new_categ, name='category_creation'),

]
