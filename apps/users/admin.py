from django.contrib import admin
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.car.models import Car
from apps.message.models import Message, MessageType
from apps.users.actions import approve, discard
from apps.users.models import Payment, User, UserInfo
from apps.users.usercode.models import UserCode
from apps.users.userdocument.models import UserDocument
from taxiback.request import FireBaseRequest


class UserInfoTabularInline(admin.StackedInline):

    model = UserInfo
    can_delete = False
    fields = ('preview_image','email', 'city','birthday','last_name','first_name')
    readonly_fields = ('preview_image', 'email', 'city','birthday','last_name','first_name')

    

class CarInline(admin.StackedInline):
    model = Car


class UserDocumentTabularInline(admin.StackedInline):
    model = UserDocument
    can_delete = False
    fieldsets = [(
        'Водительское удостоверение',
        {
            'fields': [('preview_passport_photo_front', 'preview_passport_photo_back')]
        }),
        (
        'Свидетелесьтво о регистраций ТС',
        {
            'fields': [('preview_car_passport_front', 'preview_car_passport_back')]
        }),
       ( 'Машина',
        {
            'fields': ['car']
        })
        ]
    readonly_fields = ('preview_passport_photo_front', 'preview_passport_photo_back', 'preview_car_passport_front', 'preview_car_passport_back')
    inlines = [CarInline]


request = FireBaseRequest()

def _send_message_firebase(user_id: int, title: str, body: str):
    user = User.objects.get(id=user_id)
    message_type = MessageType.objects.last()
    Message.objects.create(user=user,title=title, text=body, type=message_type)
    request.send(user.firebase_token,title,
                               body=body)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'status', 'firebase_token')
    list_filter = ('status', )
    change_form_template = 'admin/change_form_user.html'
    fields = ('phone', 'status','type_user')
    readonly_fields = ('phone', 'status', 'is_driver', 'type_user', 'firebase_token')
    inlines = (UserInfoTabularInline, UserDocumentTabularInline)

    def response_change(self, request, obj):
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        if "_approve" in request.POST:
            # handle the action on your obj
            redirect_url = reverse('admin:%s_%s_change' %
                               (opts.app_label, opts.model_name),
                               args=(pk_value,),
                               current_app=self.admin_site.name)
            approve(pk_value)
            _send_message_firebase(pk_value, 'Уважаемый пользователь, ', 'Мы рады сообщить вам, что ваш аккаунт был успешно обновлен. Теперь вы зарегистрированы в качестве водителя в нашем приложении.')
            return HttpResponseRedirect(redirect_url)
        if "_discard" in request.POST:
            # handle the action on your obj
            redirect_url = reverse('admin:%s_%s_change' %
                               (opts.app_label, opts.model_name),
                               args=(pk_value,),
                               current_app=self.admin_site.name)
            discard(pk_value)
            return HttpResponseRedirect(redirect_url)
        else:
             return super(UserAdmin, self).response_change(request, obj)


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
