from django import forms

class FormContacto(forms.Form):
    OPCIONES_DEPTO=(('venta','Venta'),('soporte','Soporte'),)
    
    asunto=forms.CharField()
    nombre=forms.CharField()
    email=forms.EmailField()
    departamento=forms.ChoiceField(choices=OPCIONES_DEPTO)
    numerodecliente=forms.IntegerField(required=False)
    consulta=forms.CharField(widget=forms.Textarea)

    def clean_consulta(self):
        consulta = self.cleaned_data['consulta']
        if len(consulta) < 20:
            raise forms.ValidationError('El mensaje es demasiado corto')
        elif len(consulta) > 50:
            raise forms.ValidationError('No escribas tanto che culiao')
        return consulta
