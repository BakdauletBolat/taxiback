from django.contrib import admin
from django import forms
from users.models import CityToCityOrder, Payment, Profile, ProfileInfo, ProfileLoginOTP, UserDocuments

admin.site.register(ProfileLoginOTP)


class ProfileInfoTabularInline(admin.StackedInline):
    model = ProfileInfo


class UserDocumentsTabularInline(admin.StackedInline):
    model = UserDocuments


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('phone', 'status', 'is_driver', 'type_user')
    list_editable = ('status',)
    fields = ('phone', 'status', 'is_driver', 'type_user', 'firebase_token')
    inlines = (ProfileInfoTabularInline, UserDocumentsTabularInline)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileInfo)
admin.site.register(UserDocuments)
admin.site.register(CityToCityOrder)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        try:
            self.fields['is_confirmed'].widget = forms.CheckboxInput(
                attrs={
                    'id': 'id_is_confirmed',
                    'onchange': 'changePaymentStatus()',
                    'style': 'width:200px'
                }
            )
        except Exception as _:
            pass


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentForm

    list_display = ('coin', 'user', 'is_confirmed')
    class Media:
        js = (
            'js/payment.js',
        )


admin.site.register(Payment, PaymentAdmin)
