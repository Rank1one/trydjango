from django.urls import path
from .views import (product_view,product_view2,
                                product_form_view,
                                dynamic_product_view,
                                dynamic_product_delete,
                                product_upd_view,
                                product_list_link)

app_name = 'products'
urlpatterns = [

    path('product/', product_view),
    path('product2/', product_view2),
    path('create/', product_form_view),
    path('product/<int:my_id>/',dynamic_product_view,name='dynamic_pview'),
    path('delproduct/<int:my_id>/',dynamic_product_delete),
    path('update/',product_upd_view),
    path('plist/',product_list_link)
]
