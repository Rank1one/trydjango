from django.shortcuts import render ,get_object_or_404,redirect
from django.http import Http404
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

def product_view2(*args,**kwargs):
  obj = Product.objects.get(id=2)
  context={
    'title':obj.Title,
    'price':obj.Price
  }
  return render(args[0],'product_detail.html',context)

from .forms import ProductFrom , RawProductFrom ,ProductretFrom

# def product_form_view(*args,**kwargs):
#   form = ProductFrom(args[0].POST or None)
#   if form.is_valid():
#     form.save()
#     form = ProductFrom()

#   context = {
#     'form': form
#   }
#   return render(args[0],'products_create.html',context)



# def product_form_view(*args,**kwargs):
#   # print(args[0].GET)
#   # print(args[0].POST)
#   if args[0].method == 'POST':
#     p_data = args[0].POST.get('Title')
#     print(p_data)
#   context = {}
#   # Product.objects.create(Title=P_data)
#   return render(args[0],'products_create1.html',context)

# def product_form_view(*args,**kwargs):
#   my_form = RawProductFrom()
#   if args[0].method == "POST":
#     my_form = RawProductFrom(args[0].POST)
#   if my_form.is_valid():
#     print(my_form.cleaned_data)
#     Product.objects.create(**my_form.cleaned_data)
#   else:
#     print(my_form.errors)
#   context = {
#     'form' : my_form
#   }
#   return render(args[0],'products_create2.html',context)


def product_upd_view(request):
  # i_d = None
  # print(request.POST)
  print(request)
  if (request.method == 'POST' and "Retrive" in request.POST):
    i_d = request.POST.get('pid')
    obj = get_object_or_404(Product,id=i_d)
    my_form = ProductFrom(instance = obj)
  else:
    i_d = None
    my_form = ProductretFrom(request.POST or None)
  if (request.method == 'POST' and "Update" in request.POST):
    # i_d = request.POST.get('pid')
    i_d = request.POST.get('chk')
    obj = get_object_or_404(Product,id=i_d)
    my_form = ProductFrom(request.POST or None,instance = obj)
    if my_form.is_valid():
      # print(my_form.cleaned_data) 
      my_form.save()
      print('form saved')
  print("Form validation :",my_form.is_valid())
  if my_form.is_valid():
    print(my_form.cleaned_data,'------------>check this out')
  context = {
    'i_d': i_d,
    'form' : my_form
  }
  return render(request,'products_update.html',context)
  


def product_form_view(*args,**kwargs):
  initial_data = {
    'Title' : 'My default title'
  }
  
  obj = Product.objects.get(id=3)
  # print(obj)
  my_form = ProductFrom(args[0].POST or None,initial = initial_data,instance=obj)
  my_form = ProductFrom(args[0].POST or None,instance=obj)
  # print(my_form)
  if my_form.is_valid():
    my_form.save()
  context = {
    'form' : my_form
  }
  return render(args[0],'products_create2.html',context)


def dynamic_product_view(request,my_id):
  # obj = Product.objects.get(id=my_id)
  # obj = get_object_or_404(Product,id = my_id)
  #another way
  print(request)
  try:
    obj = Product.objects.get(id=my_id)
  except Product.DoesNotExist:
    raise Http404
  my_form = ProductFrom(request.POST or None,instance=obj)
  context = {
    'form' : my_form
  }
  return render(request,'products_create2.html',context)

  

def dynamic_product_delete(request,my_id):
  
  obj = get_object_or_404(Product,id = my_id)
  if request.method == "POST":
    obj.delete()
    return redirect('../../')
  # my_form = ProductFrom(request.POST or None)
  my_form = ProductFrom(request.POST or None,instance=obj)
  context = {
    'form' : my_form
  }

  return render(request,'products_delete.html',context)

def product_list_link(request):
  queryset = Product.objects.all()
  print(request)

  context = {
    'object_list' : queryset
  }

  return render(request,'product_list_link.html',context)