from django.apps import AppConfig


class SearchesConfig(AppConfig):
    name = "searches"

    def ready(self):
        try:
            import searches.signals  # noqa F401
        except ImportError:
            pass
