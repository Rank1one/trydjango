from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
def product_view(*args,**kwargs):
    user = args[0].user
    print(args)
    print(user)
    l=f'<h1>{user}</h1>'
    x = Product.objects.all()
    s =''
    for i in x:
        s+= f'<tr><td>{i.Title}</td><td>{i.Price}</td></tr>'

    return HttpResponse(l+'''<style>table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}</style>'''+'''<table><tr><th>Name</th><th>Price</th></tr>''' + s
)