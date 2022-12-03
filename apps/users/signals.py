from django.db.models.signals import post_save
from django.dispatch import receiver
from taxiback.request import FireBaseRequest
from apps.users.models import Payment


@receiver(post_save, sender=Payment)
def create(sender, instance: Payment, **kwargs):
    request = FireBaseRequest()
    if instance.is_confirmed:
        try:
            res = request.send(instance.user.firebase_token, f'#{instance.gen_id} Успешно принят', body=f'{instance.coin} тг')
            print(res)
        except Exception as e:
            print(e)
