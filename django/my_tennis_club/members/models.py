from django.db import models
from django import forms
from django.core.exceptions import ValidationError

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=False, blank=False)
  joined_date = models.DateField(null=False, blank=False)
  slug = models.SlugField(default="", blank=False, null=False, unique=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone', 'joined_date']
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and len(str(phone)) < 5:
            raise forms.ValidationError("Phone number must be at least 5 digits.")
        return phone