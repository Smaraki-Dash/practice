from django import forms

class CustomerForm(forms.Form):
    name=forms.CharField(max_length=50, required=True)
    email=forms.EmailField(max_length=50, required=False)
    pno=forms.CharField(max_length=50, required=True)
    un=forms.CharField(max_length=50, required=True)
    pw=forms.CharField(max_length=50, required=True)

    def __str__(self):
        return self.name