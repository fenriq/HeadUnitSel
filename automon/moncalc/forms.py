from django import forms


class Params(forms.Form):
    width = forms.IntegerField(
        label="Ширина, мм",
        initial=0,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput",
                "type": "text",
            },
        )
    )
    height = forms.IntegerField(
        label="Высота, мм",
        initial=0,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput",
                "type": "text",
            },
        )
    )
    diag = forms.IntegerField(
        label="Диагональ, дюйм",
        initial=0,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput",
                "type": "text",
            },
        )
    )

