from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("PARENT", "Parent"),
        ("ENFANT", "Enfant"),
    )
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="ENFANT"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Document(models.Model):
    CATEGORY_CHOICES = (
        ("PIECE_ID", "Pièce d'identité (NPI, Carte)"),
        ("ACTE_NAISSANCE", "Acte de naissance"),
        ("ATTESTATION", "Attestation / Diplôme"),
        ("AUTRE_PRIVE", "Document confidentiel"),
    )

    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="documents"
    )
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="ATTESTATION"
    )
    file = models.FileField(upload_to="documents/%Y/%m/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.owner.username}"