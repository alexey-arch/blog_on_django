from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy 
from .forms import LoginForms, RegistrationForms
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForms(request.POST or None)
        context = {'form': form}
        return render(request,'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForms(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'login.html', {'form': form})


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForms(request.POST or None)
        context = {'form': form}
        return render(request,'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForms(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login = (request, user)
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {'form': form})


    


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetalView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'autor', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')