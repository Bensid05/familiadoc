from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Document


def accessible_documents(user):
    if user.role == 'PARENT':
        return Document.objects.all().order_by('-uploaded_at')

    return Document.objects.filter(
        Q(owner=user) | Q(owner__role='PARENT', category='PIECE_ID')
    ).order_by('-uploaded_at')


@login_required
def document_list(request):
    user = request.user

    # Traitement de l'envoi d'un nouveau document
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        file = request.FILES.get('file')

        if title and category and file:
            Document.objects.create(
                owner=user, title=title, category=category, file=file
            )
            return redirect('document_list')

    documents = accessible_documents(user)

    categories = Document.CATEGORY_CHOICES
    return render(
        request,
        'documents/list.html',
        {
            'documents': documents,
            'categories': categories,
        },
    )


@login_required
def my_documents(request):
    return render(
        request,
        'documents/my_documents.html',
        {'documents': accessible_documents(request.user)},
    )


@login_required
@require_POST
def delete_document(request, document_id):
    if request.user.role != 'PARENT':
        return HttpResponseForbidden('La suppression est réservée aux parents.')

    document = get_object_or_404(Document, pk=document_id)
    document.file.delete(save=False)
    document.delete()
    return redirect(request.POST.get('next') or 'document_list')