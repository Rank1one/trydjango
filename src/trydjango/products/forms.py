from django import forms

from .models import Product

class ProductFrom(forms.ModelForm):
    Title = forms.CharField(label = '',widget=forms.Textarea(attrs={'placeholder':'Title',
                                                                    'rows' : 1
                                                                    }))
    Price = forms.DecimalField(initial = 0.0)
    Summary = forms.CharField(widget= forms.Textarea(
                                        attrs={
                                            'class' : 'new class name 1',
                                            'id':'my-id-summary',
                                            'rows' : 5,
                                            'cols':50
                                        }
                                     ))
    Soldout = forms.BooleanField(initial=False,required=False)

    Description = forms.CharField(required = False,widget=forms.Textarea(attrs={
                                                                         "rows" : 4       
                                                                }))
    class Meta:
        model = Product
        fields = [
              'Title',
              'Price',
              'Description',
              'Summary',
              'Soldout'
        ]

    # def clean_<my_field>(self,*args,**kwargs):
    def clean_Title(self,*args,**kwargs):
        Title = self.cleaned_data.get('Title')
        if Title.isalpha() :
            return Title
        else:
            raise forms.ValidationError("This should be all alphabate")

class RawProductFrom(forms.Form):
    Title = forms.CharField(label = '',widget=forms.Textarea(attrs={'placeholder':'Title',
                                                                    'rows' : 1
                                                                    }))
    Price = forms.DecimalField(initial = 0.0)
    Summary = forms.CharField(widget= forms.Textarea(
                                        attrs={
                                            'class' : 'new class name 1',
                                            'id':'my-id-summary',
                                            'rows' : 20,
                                            'cols':100
                                        }
                                     ))
    Soldout = forms.BooleanField(initial=False,required=False)

    #data extract
class ProductretFrom(forms.ModelForm):
    Title = forms.CharField(required=False, label = '',widget=forms.Textarea(attrs={'placeholder':'Title',
                                                                    'rows' : 1
                                                                    }))
    Price = forms.DecimalField(required=False, initial = 0.0)
    Summary = forms.CharField(required=False,widget= forms.Textarea(
                                        attrs={
                                            'class' : 'new class name 1',
                                            'id':'my-id-summary',
                                            'rows' : 5,
                                            'cols':50
                                        }
                                     ))
    Soldout = forms.BooleanField(initial=False,required=False)

    Description = forms.CharField(required = False,widget=forms.Textarea(attrs={
                                                                         "rows" : 4       
                                                                }))
    class Meta:
        model = Product
        fields = [
              'Title',
              'Price',
              'Description',
              'Summary',
              'Soldout'
        ]