from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label ="Пароль",strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder':'Enter your password..'}))

    password2 = forms.CharField(label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','placeholder':'Confirm your password..'}), strip=False)

    class Meta:
        model = CustomUser
        fields = ['username']
        help_texts = {'username':'',}
        widgets = {'username': forms.TextInput(attrs={'placeholder':'Enter your login..',
                                                      'label':'Username:'})}


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','user_name','user_lastname','email','gender','phone','birthday']
        widgets = {
                    'user_name': forms.TextInput(attrs={'placeholder':'введите имя..',}),
                   'user_lastname': forms.TextInput(attrs={'placeholder':'введите фамилию..',}),
                   'email':forms.EmailInput(attrs={'placeholder':'введите мэйл..',}),
                   'gender':forms.Select(choices=[(None,'выберите пол'),('Мужской','Мужской'),('Женский','Женский')]),
                   'phone':forms.TextInput(attrs={'placeholder':'номер телефона..'}),
                   'birthday':forms.DateInput(attrs={'type':''}),
                   }


