from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.forms import CartAddProductForm
from .forms import *
from .models import *
from .serializers import ProductSerializer
from .utils import *


class onlineshopHome(DataMixin, ListView):
    model = Product
    template_name = 'onlineshop/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(available=True).select_related('cat')

class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'onlineshop/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(name=context['product'])
        return dict(list(context.items()) + list(c_def.items()))

class ProductCategory(DataMixin, ListView):
    model = Product
    template_name = 'onlineshop/index.html'
    context_object_name = 'posts'
    allow_empty = True

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'], available=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(name='Категория - ' + str(c.name),
                                    cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostFrom
    template_name = 'onlineshop/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'onlineshop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'onlineshop/login.html'
    #success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')



menu = [{'title': "Блог", 'url_name': 'blog'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

def about(request):
    context = {'menu': menu,
                'title': 'О сайте'
               }
    return render(request, 'onlineshop/about.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, что то пошло не так(</h1>')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'onlineshop/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(name="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'onlineshop/product.html', {'product': product, 'cart_product_form': cart_product_form})

##################### API

class ProductAPIView(APIView):
    def get(self, request):
        w = Product.objects.all()
        return Response({'posts': ProductSerializer(w, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Product.objects.create(
            firm=request.data["firm"],
            name=request.data["name"],
            slug=request.data["slug"],
            image=request.data["image"],
            description=request.data["description"],
            price=request.data["price"],
            stock=request.data["stock"],
            cat_id=request.data['cat_id'],
        )

        return Response({'post': ProductSerializer(post_new).data})


        # serializer = ProductSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        #
        # return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not allowed"})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return  Response({"post": serializer.data})