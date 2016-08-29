from django.apps import AppConfig


class API_RestFulConfig(AppConfig):
    name = 'API_RestFul'

    def ready(self):
        import API_RestFul.signals.handlers