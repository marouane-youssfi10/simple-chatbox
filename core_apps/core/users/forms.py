from django import forms

from core_apps.core.users.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", "class": "form-control"}
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

        # this function wil be add css to fields

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "Enter first name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter last name"
        self.fields["username"].widget.attrs["placeholder"] = "Enter username"
        self.fields["email"].widget.attrs["placeholder"] = "Enter email address"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    # use this function to check password is equal confirm_password
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")
