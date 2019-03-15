import os
import pathlib

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def compare_dirs(path, filename):
    try:
        abspath = pathlib.Path(settings.MEDIA_ROOT)
        abspath /= filename
        return os.path.samefile(abspath, path)
    except FileNotFoundError:
        return False


def upload_game(instance, file_name):
    file_name = "bin_game." + file_name.split(".")[-1]
    return os.path.join("games", str(instance.id), str(instance.version), file_name)


def upload_logo(instance, file_name):
    file_name = "logo." + file_name.split(".")[-1]
    return os.path.join("games", str(instance.id), file_name)
