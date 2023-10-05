from django import forms    

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comisión = forms.IntegerField()
    turno = forms.CharField()
    
class BuscaCursoForm(forms.Form):
    curso = forms.CharField()