from django.shortcuts import render ,get_object_or_404,redirect
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.
from .models import Article
from .forms import ArticleFrom

class ArticleCreateView(CreateView):
    template_name="article_create.html"
    form_class = ArticleFrom
    queryset = Article.objects.all() #<appname>/<modelname>_list.html
    # success_url = '/'
    def form_valid(self,form):
        print(form.cleaned_data,'---------> cleaned data')
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return '/'

class ArticleListView(ListView):
    template_name="article_list.html"
    queryset = Article.objects.all() #<appname>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name="article_detail.html"
    # queryset = Article.objects.all() #<appname>/<modelname>_detail.html
    # queryset = Article.objects.filter(id__gt=1) # filter condtion
    def get_object(self): # this is over ride for gh instead of pk in urls
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

class ArticleUpdateView(UpdateView):
    template_name="article_create.html"
    form_class = ArticleFrom
    queryset = Article.objects.all() #<appname>/<modelname>_list.html
    # success_url = ("/Blog/artcllist/")
    def form_valid(self,form):
        print(form.cleaned_data,'---------> cleaned data')
        return super().form_valid(form)
    
    def get_object(self): # this is over ride for id instead of pk in urls
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)
    
    def get_success_url(self):#override get_absolute_url
        return reverse('Blog:article-list')


class ArticleDeleteView(DeleteView):
    template_name="article_delete.html"
    # queryset = Article.objects.all() #<appname>/<modelname>_detail.html
    # queryset = Article.objects.filter(id__gt=1) # filter condtion
    def get_object(self): # this is over ride for id instead of pk in urls
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)
    
    def get_success_url(self):#override get_absolute_url
        return reverse('Blog:article-list')