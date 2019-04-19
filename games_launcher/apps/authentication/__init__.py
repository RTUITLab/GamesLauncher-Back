from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AuthConfig(AppConfig):
    name = "games_launcher.apps.authentication"
    label = "authentication"
    verbose_name = "Authentication"

    def ready(self):
        import games_launcher.apps.authentication.signals

        post_migrate.connect(
            games_launcher.apps.authentication.signals.create_roles, sender=self
        )


default_app_config = "games_launcher.apps.authentication.AuthConfig"
