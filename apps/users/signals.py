from django.db.models.signals import post_save
from django.dispatch import receiver
from taxiback.request import FireBaseRequest
<<<<<<< HEAD:apps/users/signals.py
from apps.users.models import Payment
=======
from users.models import Payment
>>>>>>> origin/release:users/signals.py


@receiver(post_save, sender=Payment)
def create(sender, instance: Payment, **kwargs):
    request = FireBaseRequest()
    if instance.is_confirmed:
        try:
            request.send(instance.user.firebase_token, f'#{instance.gen_id} Успешно принят', body=f'{instance.coin} тг')
        except Exception as e:
            print(e)