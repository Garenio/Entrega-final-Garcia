from django import forms
from blog.models import Review 

class ReviewFormulario(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(ReviewFormulario, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget = HiddenInput()

    class Meta:
        model = Review
        fields = ['usuario','titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen']