import os
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from .storage import OverwriteStorage, upload_file


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, blank=False, unique=True)
    version = models.CharField(max_length=10, blank=False)
    logo = models.ImageField(
        upload_to=upload_file,
        storage=OverwriteStorage()
    )
    file = models.FileField(
        upload_to=upload_file,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
    )

    def delete(self, *args, **kwargs):
        if os.path.isdir(self.id):
            os.remove(self.id)
        super(Game, self).delete(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.name, self.version)

    class Meta:
        unique_together = ("name", "version")
        ordering = ("id", "name", "version",)
