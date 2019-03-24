from django.contrib.auth.models import Group

from .permissions import IsLoader


class LoaderGroup(Group):
    permissions = [IsLoader]
