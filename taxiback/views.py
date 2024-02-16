from django.shortcuts import render

from form.models import FeedBack


def render_privacy_view(request):
    return render(request, 'main/privacy.html')

def render_documents_view(request):
    return render(request, 'main/documents.html')

def render_index(request):
    feedbacks = FeedBack.objects.all()[:10]
    return render(request, 'main/index.html', context={
        'feedbacks': feedbacks
    })