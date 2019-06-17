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