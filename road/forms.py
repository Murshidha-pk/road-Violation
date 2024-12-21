from django import forms

from django.contrib.auth.forms import UserCreationForm

from road.models import User,RoadViolation

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password1":forms.TextInput(attrs={"class":"form-control"}),
            "password2":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
        }

class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class RoadViolationForm(forms.ModelForm):

    class Meta:

        model=RoadViolation

        fields=["name","violation_type","description","fine_amount","location","image","timestamp"]

        widgets={

            "name":forms.TextInput(attrs={"class":"form-control"}),
            "violation_type":forms.Select(attrs={"class":"form-control form-select"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "fine_amount":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "timestamp":forms.DateInput(attrs={"class":"form-control","type":"date"}),


        }