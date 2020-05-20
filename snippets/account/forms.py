from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions

from .widgets import ImagePreviewWidget


class ProfileForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Field('bio', rows=6),
        'website',
        'avatar',
        HTML("""{% if profile_form.avatar.value %}<img src="/media/{{ profile_form.avatar.value }}" class="img-responsive rounded" style="width: 256px; max-width: 100%;">{% endif %}""", ),
        FormActions(
            Submit("save", "Enregistrer"),
            HTML("<input type=\"reset\" value=\"Annuler\" class=\"btn btn-secondary\">"),
            css_class="mt-3 mb-3",
        )
    )

    class Meta:
        model = Profile
        fields = [
            "bio",
            "website",
            "avatar",
        ]
        widgets = {
            # 'image': ImagePreviewWidget
        }


class UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        "username",
        "first_name",
        "last_name",
        Field("email", readonly=True),
        FormActions(
            Submit("save", "Enregistrer"),
            HTML("<input type=\"reset\" value=\"Annuler\" class=\"btn btn-secondary\">")
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
        widgets = {
            'image': ImagePreviewWidget,

        }
