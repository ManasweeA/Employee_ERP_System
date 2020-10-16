from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from friday.forms import UserProfileInfoForm, UserCreateForm
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import UserProfileInfo
from .decorators import group_required

# Create your views here.
def dashboard(request):
    user = request.user
    if request.user.is_staff:
        return HttpResponseRedirect('/admin')
    profile = UserProfileInfo.objects.filter(user=user)[0]
    print(profile.passport_pic)
    return render(request,'dashboard.html',{'profile': profile, })

def index(request):
    if request.user.is_authenticated:
        return redirect('friday:dashboard')
    return redirect('login')

# class HomePage(TemplateView):
#     template_name = 'login.html'

@group_required('HR')
def sign_up(request):
    admin_positions = ["Human Resources"]

    if request.method == 'POST':
        # Process SignUp Form
        user_form = UserCreateForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            designation = profile_form.cleaned_data.get('designation')
            group = Group.objects.get(name='employee')
            if designation in admin_positions :
                group = Group.objects.get(name='HR')
            user.groups.add(group)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Registered successfully')
            return redirect('login')
        else:
            print("Invalid form")
    else:
        user_form = UserCreateForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'sign_up.html', {'user_form': user_form, 'profile_form': profile_form})


class UserProfilePage(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    login_url = 'login'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile'] = UserProfileInfo.objects.get(user=self.request.user)
        return context

class CalendarPage(TemplateView):
    template_name = "calendar.html"

class ProjectsPage(TemplateView):
    template_name = "projects.html"