from django.apps import AppConfig


class ActionsConfig(AppConfig):
    name = 'actions'

class SelectionsConfig(AppConfig):
    name = 'selections'
    def ready(self):
        # import signal handlers
        import selections.signals
