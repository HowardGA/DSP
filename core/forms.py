from django import forms 
from core import models

class NewGrantGoalForm(forms.forms.ModelForm):
    
    class Meta:
        model = models.GrantGoal
        fields = (
            "ggname",
            "user",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug")

    widgets = {
        "ggname": forms.TextInput(attrs={"type":"text" , "class":"form-control" , "placeholder":"Escribe el grant goal name"}),
        "description": forms.TextArea(attrs={"type":"text" , "class":"form-control" , "row":3 , "placeholder":""}),
        "user": forms.Select(attrs={"type":"text" , "class":"form-control"}),
        "days_duration": forms.TextInput(attrs={"type":"number" , "class":"form-control"}),
        "user": forms.Select(attrs={"type":"select" , "class":"form-control"}),
    }