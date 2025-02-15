from django import forms
from .models import CreateNews,CryptoArticalModel,Comment

# class NewsPostForm(forms.ModelForm):
#     class Meta:
#         model = NewsPost
#         fields = ['title', 'content', 'image']


class CreateNewsForm(forms.Form):
    class Meta:
        model = CreateNews
        fields = ['title', 'content', 'image', 'created_at', 'category', 'author']

class CryptoArticleForm(forms.Form):
    class Meta:
        model = CryptoArticalModel
        # fields = ['title', 'content', 'image', 'news_section', 'category', 'author']
        fields = ['title', 'content', 'image', 'created_at', 'category', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }