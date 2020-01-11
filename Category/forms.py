from django import forms
from Category import models

class FormCategory(forms.ModelForm):
    category_name = forms.CharField(max_length = 100, required = True)
    category_image = forms.ImageField(required = False)
    status = forms.BooleanField()

    class Meta:
        model = models.Category
        fields = ["category_name", "category_image", "status"]
        #fields = "__all__"

