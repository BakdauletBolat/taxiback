from django.shortcuts import render


def render_privacy_view(request):
    return render(request, 'main/privacy.html')
