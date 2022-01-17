from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Footballer, Position, Club, Country
from .forms import AddPostForm, RegisterUserForm, LoginUserForm, ContactForm
from .utils import DataMixin, menu


class FootballerHome(DataMixin, ListView):
    model = Footballer
    template_name = 'footballer/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Footballer.objects.filter(is_published=True).select_related('position', 'club', 'country')


def about(request):
    context = {'title': 'О сайте',
               'menu': menu,
               'position': Position.objects.all(),
               'position_selected': 0}
    return render(request, 'footballer/about.html', context=context)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'footballer/add_page.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context | c_def


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'footballer/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class ShowPost(DataMixin, DetailView):
    model = Footballer
    template_name = 'footballer/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


class FootballerPosition(DataMixin, ListView):
    model = Footballer
    template_name = 'footballer/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Position.objects.get(slug=self.kwargs['position_slug'])
        c_def = self.get_user_context(
            title='Категория - ' + str(p.name),
            position_selected=p.pk)
        return context | c_def

    def get_queryset(self):
        return Footballer.objects.filter(position__slug=self.kwargs['position_slug'], is_published=True) \
            .select_related('position', 'club', 'country')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'footballer/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'footballer/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class FootballerClub(DataMixin, ListView):
    model = Footballer
    template_name = 'footballer/club.html'
    context_object_name = 'footballer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        club = Club.objects.get(slug=self.kwargs['club_slug'])
        context['club'] = club
        c_def = self.get_user_context(
            title=str(club.name))
        return context | c_def

    def get_queryset(self):
        return Footballer.objects.filter(club__slug=self.kwargs['club_slug'], is_published=True) \
            .select_related('position', 'club', 'country')


class FootballerCountry(DataMixin, ListView):
    model = Footballer
    template_name = 'footballer/country.html'
    context_object_name = 'footballer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        country = Country.objects.get(slug=self.kwargs['country_slug'])
        context['country'] = country
        c_def = self.get_user_context(
            title=str(country.name))
        return context | c_def

    def get_queryset(self):
        return Footballer.objects.filter(country__slug=self.kwargs['country_slug'], is_published=True) \
            .select_related('position', 'club', 'country')
