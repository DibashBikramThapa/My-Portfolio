from portfolioApp import forms
from portfolioApp.models import Profile,AboutMe

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView,TemplateView,View


def logme(request):
    return render(request,'portfolioApp/login.html')


class PortfolioView(ListView):
    model = Profile
    template_name='portfolioApp/portfolioview.html'
    extra_context={'homecheck':True}


class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model=Profile
    form_class=forms.ProfileForm
    template_name='portfolioApp/portfolioform.html'
    extra_context={'profile_list':Profile.objects.all()}


class AboutMeView(ListView):
    model = AboutMe
    template_name='portfolioApp/aboutme.html'
    extra_context={'profile_list':Profile.objects.all()}


class AboutMeForm(LoginRequiredMixin, UpdateView):
    model=AboutMe
    form_class=forms.AboutMeForm
    template_name='portfolioApp/aboutmeform.html'
    extra_context={'profile_list':Profile.objects.all()}



class Projects(ListView):
    model = Profile
    template_name='portfolioApp/projectlist.html'
