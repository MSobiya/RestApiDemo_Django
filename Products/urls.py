from django.urls import path
from . import views

urlpatterns = [
	#localhost:8000/products/
    path('', views.products_list),
    path('<int:prod_id>/', views.product_details),
]
