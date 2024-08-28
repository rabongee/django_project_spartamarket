from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    hashtags = forms.CharField(max_length=20, required=False)
    
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("author", "like_users", "tag_hashtags", "views")

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

        self.fields['title'].label = '제목'
        self.fields['content'].label = '내용'
        self.fields['price'].label = '가격'
        self.fields['image'].label = '사진 (미첨부가능)'
        self.fields['hashtags'].label = '#해시태그 #여러개가능'
        
        self.fields['title'].widget.attrs.update({'placeholder': '필수입력란입니다! 최대 20자'})
        self.fields['content'].widget.attrs.update({'placeholder': '필수입력란입니다! 글자수 제한 없음'})
        self.fields['price'].widget.attrs.update({'placeholder': '필수입력. 10억이하'})
        self.fields['hashtags'].widget.attrs.update({'placeholder': 'ex) 공룡,키링,인형'})