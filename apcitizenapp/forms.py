from django import forms
from apcitizenapp.models import *


class aadharform(forms.ModelForm):
    class Meta:
        model = aadhar
        fields = ['full_name','date_of_birth','father_name','phone_number','address']
        widgets = {'full_name':forms.TextInput(attrs={'placeholder':'Enter your full name'}),'date_of_birth': forms.DateInput(attrs={'type':'date'}), 'address':forms.TextInput(attrs={'placeholder':'Enter full address with '}),'phone_number':forms.NumberInput(attrs={'class':'no-spinner'})}
        
# class loginform(forms.Form):
#     user_name = forms.CharField(max_length=20)
#     password = forms.CharField(max_length=30, widget=forms.PasswordInput())

class GetAadharForm(forms.Form):
    mobile_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'no-spinner'}))
    
class VoterRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = voterregister
        fields = ['user_name','password','confirm_password']
        widgets = {'user_name':forms.NumberInput(attrs={'placeholder':'Use your aadhar number as user name.','class':'no-spinner'}),'password':forms.PasswordInput()}
        
class AssemblySelectionForm(forms.Form):
    constituency = [
        ('Kurnool','Kurnool'),
        ('Srisailam','Srisailam'),
        ('Nandyal','Nandyal'),
        ('Nandikotkur','Nandikotkur'),
        ('Allagadda','Allagadda'),
        ('Kadapa','Kadapa'),
        ('Pulivendla','Pulivendla'),
        ('Kodur','Kodur'),
        ('Kuppam','Kuppam'),
        ('Tirupati','Tirupati'),
        ('Srikakulam','Srikakulam'),
        ('Kadiri','Kadiri'),
        ('Hindupur','Hindupur'),
        ('Adoni','Adoni'),
        ('Dhone','Dhone'),
        ('Pattikonda','Pattikonda'),
        ('Kodumur','Kodumur'),
        ('Gajuwaka','Gajuwaka'),
        ('Vishakapatnam','Vishakapatnam'),
        ('Vizianagaram','Vizianagaram'),
        ('Guntur','Guntur'),
    ]
    aadhar_number=forms.IntegerField(label="Enter your aadhar number :", widget=forms.NumberInput(attrs={'class':'no-spinner'}))
    options = forms.ChoiceField(choices=constituency, label= 'Select Your Constituency :')
    
class ParlimentSelectionForm(forms.Form):
    constituency =[
        ('Kurnool','Kurnool'),
        ('Nandyal','Nandyal'),
        ('Kadapa','Kadapa'),
        ('Thirupati','Thirupati'),
        ('Vijayawada','Vijayawada')
    ]
    aadhar_number = forms.IntegerField(label="Enter your Aadhar number :", widget=forms.NumberInput(attrs={'class':'no-spinner'}))
    options = forms.ChoiceField(choices=constituency, label="Select Your Constituency :")