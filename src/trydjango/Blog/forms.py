from django import forms

from .models import Article

class ArticleFrom(forms.ModelForm):
    title = forms.CharField(label = '',widget=forms.Textarea(attrs={'placeholder':'Title',
                                                                    'rows' : 1
                                                                    }))
    content = forms.CharField(widget= forms.Textarea(
                                        attrs={
                                            'class' : 'new class content',
                                            'id':'my-id-content',
                                            'rows' : 5,
                                            'cols':50
                                        }
                                     ))
    active = forms.BooleanField(initial=True ,required = False,)
    class Meta:
        model = Article
        fields = [
              'title',
              'content',
              'active'
        ]
# def clean_<my_field>(self,*args,**kwargs):