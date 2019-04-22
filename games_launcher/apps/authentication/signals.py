from games_launcher.apps.authentication.models import Role, RolesEnum


def create_roles(sender, **kwargs):
    """Create if not exists default roles in database when server start"""

    for role in RolesEnum:
        Role.objects.get_or_create(name=role.value[0])
