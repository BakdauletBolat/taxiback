from django.db.models.signals import post_save
from django.dispatch import receiver
from taxiback.request import FireBaseRequest
from apps.users.models import Payment
from sentry_sdk import capture_exception


@receiver(post_save, sender=Payment)
def create(sender, instance: Payment, **kwargs):
    request = FireBaseRequest()
    if instance.is_confirmed:
        try:
            res = request.send(instance.user.firebase_token, f'#{instance.gen_id} Успешно принят',
                               body=f'{instance.coin} тг')
            if res['success'] == 0:
                raise Exception(res)
        except Exception as e:
            capture_exception(e)
