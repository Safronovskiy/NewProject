from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserCreationForm,EditProfile
from .models import CustomUser,Profile
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView,LogoutView


def registration(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            CustomUser.objects.create_user(username=username,
                                           password=password)
            return redirect('accounts:login')
        else:
            return redirect('accounts:register')
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/registration.html', context={'form':form})

class CustomUserLogin(LoginView):
    template_name = 'accounts/login.html'



class CustomUserLogout(LogoutView):
    next_page = 'main_app:startpage'

@login_required
def profile(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        profile = Profile.objects.filter(user=request.user)
        context = {'profile':profile}
        return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    userprofile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get('avatar'):
                userprofile.avatar = form.cleaned_data.get('avatar')
            userprofile.user_name = form.cleaned_data.get('user_name')
            userprofile.user_lastname = form.cleaned_data.get('user_lastname')
            userprofile.email = form.cleaned_data.get('email')
            userprofile.gender = form.cleaned_data.get('gender')
            userprofile.phone = form.cleaned_data.get('phone')
            userprofile.birthday = form.cleaned_data.get('birthday')
            userprofile.save()
            return redirect('accounts:profile')
        else:
            form = EditProfile(request.POST)
            return render(request, 'accounts/editprofile.html', {'form':form})
    else:
        profile = Profile.objects.get(user=request.user)
        data={'user_name':profile.user_name,'user_lastname':profile.user_lastname,'gender':profile.gender,
              'phone':profile.phone,'birthday':profile.birthday,'email':profile.email}
        form = EditProfile(data=data)
        return render(request, 'accounts/editprofile.html', {'form':form,'profile':profile})






