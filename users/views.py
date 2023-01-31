from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from shop.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User

# Create your views here.


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.object)
    #     return context
        

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm


class EmailVerificationView(TemplateView):
    template_name = 'email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists():
            user.is_verified_emails = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))


# class register(View):
#
#     def get(self, request):
#         form = UserRegistrationForm()
#         context = {'form': form}
#         return render(request, 'register.html', context)
#
#     def post(self, request):
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Регистрация прошла успешно')
#             return HttpResponseRedirect(reverse('users:login'))
#         else:
#             print(form.errors)
#         return render(request, 'register.html', context={'form': form})
#
#
# class login(View):
#
#     def get(self, request):
#
#         form = UserLoginForm()
#         context = {'form': form}
#         return render(request, 'login.html', context)
#
#     def post(self, request):
#
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#         context = {'form': form}
#         return render(request, 'login.html', context)
#
#
#
# class profile(View):
#
#     def get(self, request):
#         user = request.user
#         if not user.is_authenticated:
#             return HttpResponseRedirect(reverse('users:login'))
#         baskets = Basket.objects.filter(user=request.user)
#         total_quantity = sum(basket.quantity for basket in baskets)
#         total_price = sum(basket.sum() for basket in baskets)
#         # for basket in baskets:
#         #     total_quantity += basket.quantity
#         #     total_price += basket.sum()
#         form = UserProfileForm(instance=request.user)
#         return render(request, 'profile.html', context={'form': form,
#                                                         'baskets': baskets,
#                                                         'total_quantity': total_quantity,
#                                                         'total_price': total_price})
#
#     def post(self, request):
#
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         return render(request, 'profile.html', context={'form': form})
#

class logout(View):

    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))


