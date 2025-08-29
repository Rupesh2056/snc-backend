from django import forms
from django.forms.fields import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    TypedChoiceField,
)
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.forms.widgets import DateInput, PasswordInput,TimeInput


class BaseForm:
    def __init__(self, *args, **kwargs):
        if kwargs.get("request"):
            self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        for field in self.fields:

            if type(self.fields[field]) != BooleanField:
                self.fields[field].widget.attrs[
                    "class"
                ] = "form-control form-control-solid"

          
            if (
                type(self.fields[field]) == TypedChoiceField
                or type(self.fields[field]) == ModelChoiceField
            ):
                self.fields[field].widget.attrs["data-control"] = "select2"

                self.fields[field].widget.attrs["data-placeholder"] = "Select an option"

                self.fields[field].widget.attrs[
                    "class"
                ] = "form-control form-control-solid"

            if type(self.fields[field]) == ModelMultipleChoiceField:
                self.fields[field].widget.attrs["data-control"] = "select2"
                self.fields[field].widget.attrs["data-placeholder"] = "Select an option"
                self.fields[field].widget.attrs[
                    "class"
                ] = "form-control form-control-sm"


