from django.urls import path
from .views import cat_sort, details, startpage_shop


app_name = 'shop_app'

urlpatterns = [
    path('', startpage_shop, name='shopstartpage'),
    path('cat_sorted/<int:pk>/', cat_sort, name='catsort'),
    path('details/<int:pk>/', details, name='details'),
    # path('', AllItemsView.as_view(), name='shopstartpage'),

]











