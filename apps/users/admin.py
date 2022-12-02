from django.contrib import admin
from django import forms
from apps.users.models import Payment, User, UserInfo
from apps.users.usercode.models import UserCode
from apps.users.userdocument.models import UserDocument


class UserInfoTabularInline(admin.StackedInline):
    model = UserInfo


class UserDocumentTabularInline(admin.StackedInline):
    model = UserDocument


class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'status', 'is_driver', 'type_user')
    list_editable = ('status',)
    fields = ('phone', 'status', 'is_driver', 'type_user', 'firebase_token')
    inlines = (UserInfoTabularInline, UserDocumentTabularInline)


admin.site.register(UserCode)
admin.site.register(User, UserAdmin)
admin.site.register(UserInfo)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

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
