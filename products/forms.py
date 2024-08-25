from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    hashtags = forms.CharField(max_length=20, required=False)
    
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("author", "like_users", "tag_hashtags")

    def clean_hashtags(self):
        hashtags_str = self.cleaned_data.get('hashtags', '').strip()
        hashtags = [tag.strip() for tag in hashtags_str.split(',')]
        for hashtag in hashtags:
            if ' ' in hashtag or not hashtag.isalnum():
                raise forms.ValidationError("띄어쓰기나 특수문자는 안됨!")
        return hashtags
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            initial_tags = ','.join([tag.keyword for tag in self.instance.tag_hashtags.all()])
            self.fields['hashtags'].initial = initial_tags
