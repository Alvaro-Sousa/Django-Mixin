from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views import View

# Create your views here.
class HomeView(TemplateView):
    template_name = 'funcionarios/home.html'

class LoginView(View):
    template_name = 'funcionarios/login.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('painel_view')
        
        return render(request, self.template_name,{'erro': 'Usuário ou senha inválidos'})
    login_url = 'login_view'

class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionarios/logout.html'
    login_url = 'login_view'

class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionarios/painel.html'
    login_url = 'login_view'

class PerfilView(LoginRequiredMixin,TemplateView):
    template_name = 'funcionarios/perfil.html'
    login_url = 'login_view'
