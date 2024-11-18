from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('mymodels/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodels/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodels/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodels/<int:pk>/update/', views.MyModelUpdateView.as_view(), name='mymodel_update'),
    path('mymodels/<int:pk>/delete/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),
]
