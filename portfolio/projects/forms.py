from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
            "link",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": _("Title")}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Description"),
                    "rows": 3,
                }
            ),
            "link": forms.URLInput(
                attrs={"class": "form-control", "placeholder": _("Link")}
            ),
            "image": forms.FileInput(attrs={"class": "form-control-file"}),
        }
