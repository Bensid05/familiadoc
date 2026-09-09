from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from .models import Document
from .serializers import DocumentSerializer


class IsParentForDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.role == 'PARENT'
        return True


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsParentForDelete]
    parser_classes = [MultiPartParser, FormParser]  # Permet le téléversement de fichiers

    def get_queryset(self):
        user = self.request.user
        
        # Un Parent voit tous les documents
        if user.role == 'PARENT':
            return Document.objects.all().order_by('-uploaded_at')
        
        # Un Enfant voit ses documents + les pièces d'identité des parents
        return Document.objects.filter(
            Q(owner=user) | Q(owner__role='PARENT', category='PIECE_ID')
        ).order_by('-uploaded_at')

    def perform_create(self, serializer):
        # Assigne automatiquement l'utilisateur connecté comme propriétaire du document
        serializer.save(owner=self.request.user)