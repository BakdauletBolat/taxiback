from django.urls import path

from form.views import render_form_view, save_form_view

urlpatterns = [
    path('', render_form_view),
    path('save/', save_form_view),
]
