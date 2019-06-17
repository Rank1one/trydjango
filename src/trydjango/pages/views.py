from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(*args,**kwargs):
    return HttpResponse('<h1>Hello World</h1>')

def contact_view(*args,**kwargs):
    return HttpResponse('''<style>table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}</style>
    <table><tr><th>Name</th><th>Mobile</th></tr>
        <tr><td>Bibhu</td><td>9999999999</td></tr>
        <tr><td>Libha</td><td>8888899665</td></tr></table>''')

#render
def test_tem_view(*args,**kwargs):
  return render(args[0],'home.html',{})

def my_tem_view(*args,**kwargs):
  return render(args[0],'startbootstrap-creative-gh-pages/index.html', )


def use_context(*args,**kwargs):
  my_context ={
    "my_text":"This homepage",
    "my_number":12543,
    'my_list':['Bibhu.Rank','Battle_angel',"ArcAngel"],
    'my_list2':[62,80,95,34]
  }

  return render(args[0],'home.html',my_context)
          







