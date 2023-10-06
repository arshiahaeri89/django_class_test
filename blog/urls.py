from django.urls import path
from .views import index, all_posts, single_post, karbaran_list, product_list, product_details

urlpatterns = [
    path('', index, name='home'),
    path('posts/', all_posts, name='posts'),
    path('posts/<slug:slug>', single_post, name='post_details'),
    path('k/', karbaran_list),
    path('products/', product_list, name='product-list'),
    path('products/<slug:slug>', product_details, name='product-details'),
]
