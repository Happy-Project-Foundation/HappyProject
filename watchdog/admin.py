from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import HappyPerson

class HappyPersonCreationForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput
    )

    class Meta:
        model = HappyPerson
        fields = ('email', 'first_name', 'last_name')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Passwords given, don't match"
            )
        
        return password2
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("passwrod1"))
        if commit:
            user.save()
        
        return user

class HapyPersonChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = HappyPerson
        fields = (
            "password",
            "first_name",
            "last_name"
        )


class HappyPersonAdmin(BaseUserAdmin):
    form = HapyPersonChangeForm
    add_form = HappyPersonCreationForm

    list_display = ("email", "first_name", "last_name")
    list_filter = ("is_active",)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'last_name',)
    ordering = ('first_name','last_name', 'email')
    filter_horizontal = ()


admin.site.register(HappyPerson, HappyPersonAdmin)
admin.site.unregister(Group)