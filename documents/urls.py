from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import DocumentViewSet

# Configuration du routeur API
router = DefaultRouter()
router.register(r'api/documents', DocumentViewSet, basename='api-documents')

urlpatterns = [
    # Routes Web classique
    path('', views.document_list, name='document_list'),
    path('mes-documents/', views.my_documents, name='my_documents'),
    path('documents/<int:document_id>/supprimer/', views.delete_document, name='delete_document'),
    path('login/', auth_views.LoginView.as_view(template_name='documents/login.html'), name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='documents/login.html'), name='legacy_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Routes API REST
    path('', include(router.urls)),
]