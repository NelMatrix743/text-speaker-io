import uuid, os
from django.db import models as md



class FileType(md.TextChoices):
    """ File type choices """

    TEXT = ("text", "Text")
    AUDIO = ("audio", "Audio")
    VIDEO = ("video", "Video")


class Origin(md.TextChoices):
    """ Origin choices """
    
    INPUT = ("input", "Input")
    OUTPUT = ("output", "Output")


def origin_path(instance, filename) -> str:
    ext: any = filename.split(".")[-1]
    unique_name: str = f"{uuid.uuid4()}.{ext}"
    return f"{instance.origin}/{unique_name}"


class MediaFile(md.Model):
    """ Represents any stored file (input or output) """

    file: md.FileField = md.FileField(upload_to=origin_path)
    original_filename: md.CharField = md.CharField(max_length=200)
    file_type: md.CharField = md.CharField(
        max_length=20,
        choices=FileType.choices,
    )

    mime_type: md.CharField = md.CharField(max_length=100)

    origin: md.CharField = md.CharField(
        max_length=10,
        choices=Origin.choices,
    )

    size: md.PositiveIntegerField = md.PositiveIntegerField()
    duration: md.PositiveIntegerField = md.PositiveIntegerField(
        null=True,
        blank=True
    ) # duration in seconds
    
    created_at: md.DateTimeField = md.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs) -> None:
        if self.file and not self.original_filename:
            self.original_filename = os.path.basename(self.file.name)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.original_filename}({self.file.path})"
