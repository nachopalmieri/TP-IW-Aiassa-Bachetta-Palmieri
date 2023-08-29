from django.apps import AppConfig


class SitioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sitio'

    def ready(self):
        import sitio.signals
