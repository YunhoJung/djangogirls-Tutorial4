from django import forms


class PostCreationForm(forms.Form):
    title = forms.CharField(label='제목', max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': '제목을 입력하세'})) # 빈값 허용 안됨
    text = forms.CharField(label='내용', max_length=300, required=True, widget=forms.TextInput(attrs={'placeholder': '내용을 입력하세요'}))