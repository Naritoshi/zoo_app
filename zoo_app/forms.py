from django import forms
   
class UploadFileForm(forms.Form):
    file = forms.FileField(label="動物の画像を選択してください")
    file.attrs={'class': 'waves-effect waves-light btn'}
