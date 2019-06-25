from django.urls import path
from .views import (
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView
)

app_name = 'Blog'
urlpatterns = [
    path('<int:id>/delete/',ArticleDeleteView.as_view(),name="article-detele"),
    path('<int:id>/update/',ArticleUpdateView.as_view(),name="article-update"),
    path('create/',ArticleCreateView.as_view(),name="article-create"),
    path('artcllist/',ArticleListView.as_view(),name="article-list"),
    path('<int:id>/',ArticleDetailView.as_view(),name="article-details")
    # path('product/<int:my_id>/',dynamic_product_view,name='dynamic_pview'),
    
]
