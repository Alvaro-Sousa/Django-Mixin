from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('login/', views.LoginView.as_view(), name = 'login_view'),
    path('logout/', views.LogoutView.as_view(), name = 'logout_view'),
    path('painel/', views.PainelView.as_view(), name = 'painel_view'),
    path('perfil/', views.PerfilView.as_view(), name = 'perfil_view'),


]