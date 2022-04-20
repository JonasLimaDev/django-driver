from django import forms

class FormUpload(forms.Form):
    autor = forms.CharField(label='Autor', max_length=75)
    autor.widget.attrs = {'class':'form-control','placeholder':autor.label}

    arquivo = forms.FileField(label='Arquivo',required=False)
    arquivo.widget.attrs={'class':'form-control','placeholder':arquivo.label,'accept':'.pdf'}


class FormUploadConf(forms.Form):
    arquivo_config = forms.FileField(label='Arquivo',required=False)
    arquivo_config.widget.attrs={'class':'form-control'}
