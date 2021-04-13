from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
