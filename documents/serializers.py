from rest_framework import serializers
from .models import Document, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']


class DocumentSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Document
        fields = [
            'id', 
            'title', 
            'category', 
            'category_display', 
            'file', 
            'uploaded_at', 
            'owner', 
            'owner_username'
        ]
        read_only_fields = ['owner', 'uploaded_at']