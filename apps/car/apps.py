from django.apps import AppConfig


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
<<<<<<< HEAD:apps/car/apps.py
    name = 'apps.car'
=======
    name = 'users'

    def ready(self) -> None:
        import users.signals
        return super().ready()
>>>>>>> origin/release:users/apps.py
