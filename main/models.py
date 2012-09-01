from django.db import models

# Create your models here.

from hashlib import md5
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

def _upload_path(instance, filename):
    basepath = settings.UPLOAD_BASE_PATH
    return os.path.join(basepath, md5(filename).hexdigest())


class File(models.Model):
    name = models.CharField(max_length=256)
    title = models.TextField()
    content = models.FileField(upload_to = _upload_path,
            storage = FileSystemStorage(location = settings.UPLOAD_BASE_PATH))
