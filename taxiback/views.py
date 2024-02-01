from django.shortcuts import render


def render_privacy_view(request):
    return render(request, 'main/privacy.html')



def render_index(request):
    return render(request, 'main/index.html')