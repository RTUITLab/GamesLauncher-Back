import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from .storage import OverwriteStorage, upload_logo, upload_game


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, blank=False, unique=True)
    logo = models.ImageField(upload_to=upload_logo, blank=False, null=False)
    version = models.CharField(max_length=10, blank=False)
    file = models.FileField(
        upload_to=upload_game,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=False,
    )

    def __str__(self):
        return "{}-{}".format(self.name, self.version)

    class Meta:
        unique_together = ("name", "version")
        ordering = ("name", "version", "id",)

# todo refactor
# import os
# from django.dispatch import receiver

# @receiver(models.signals.pre_save, sender=Game)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     if not instance.id:
#         return False
#     try:
#         old_file = Game.objects.get(id=instance.id).file
#     except Game.DoesNotExist:
#         return False

#     if os.path.isfile(old_file.path):
#         os.remove(old_file.path)


# @receiver(models.signals.pre_save, sender=Game)
# def auto_delete_logo_on_change(sender, instance, **kwargs):
#     if not instance.id:
#         return False
#     try:
#         old_file = Game.objects.get(id=instance.id).logo
#     except Game.DoesNotExist:
#         return False

#     if os.path.isfile(old_file.path):
#         os.remove(old_file.path)
