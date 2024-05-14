from django import forms

from core import models

class NewGrantGoalForm(forms.ModelForm):
    class Meta:
        model = models.GrantGoal
        fields = [
            "ggname",
            "user",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "ggname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }


class UpdateGrantGoalForm(forms.ModelForm):
    class Meta:
        model = models.GrantGoal
        fields = [
            "ggname",
            "user",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "ggname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }