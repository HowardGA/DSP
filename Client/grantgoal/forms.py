from django import forms

CHOICES_STATE = {
    ("NS", "NOT STARTED"),
    ("IP", "IN PROCESS"),
    ("DN", "DONE")
}

CHOICES_PRIORITY = {
    ("HIGH", "HG"),
    ("MIDDLE", "MD"),
    ("LOW", "LW")
}


class CreateGrantGoalClientForm(forms.Form):
    ggname = forms.CharField(max_length=32, widget= forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}))
    description = forms.CharField(max_length=128, widget= forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}))
    days_duration = forms.IntegerField(widget= forms.NumberInput(attrs={"type":"number", "class":"form-control"}))
    state = forms.CharField(max_length=16, widget=forms.Select(choices=CHOICES_STATE, attrs={"type":"select", "class":"form-select form-control"}))
    priority = forms.CharField(max_length=16, widget=forms.Select(choices=CHOICES_PRIORITY, attrs={"type":"select", "class":"form-select form-control"}))
    status = forms.BooleanField(widget = forms.CheckboxInput(attrs={"type":"checkbox"}))
    slug = forms.SlugField(widget= forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}))


