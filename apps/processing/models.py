from django.db import models as md



class InputType(md.TextChoices):
    """ Input type choices """

    TEXT = ("text", "Text")
    FILE = ("file", "File")
    URL = ("url", "URL")


class OutputType(md.TextChoices):
    """ Output type choices """

    TEXT = ("text", "Text")
    FILE = ("file", "File")


class OperationStatus(md.TextChoices):
    """ Operation status choices """

    PENDING = ("pending", "Pending")
    COMPLETED = ("completed", "Completed")
    FAILED = ("failed", "Failed")


class Input(md.Model):
    """ Represents the original data submitted by the user """

    input_type: md.CharField = md.CharField(
        max_length=10,
        choices=InputType.choices,
        default=InputType.TEXT.value
    )

    user: md.ForeignKey = md.ForeignKey(
        "apps.accounts.User",
        on_delete= md.CASCADE,
        related_name="inputs"
    )

    raw_text: md.TextField = md.TextField()
    source_url: md.URLField = md.URLField(max_length=200)
    media_file: md.ForeignKey = md.ForeignKey(
        "apps.media.MediaFile",
        on_delete=md.CASCADE,
        related_name="input"
    )

    created_at: md.DateTimeField = md.DateTimeField(auto_now_add=True)
    updated_at: md.DateTimeField = md.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.input_type}"



class Operation(md.Model):
    """ Represents a processing request performed on an input """

    operation_type: md.CharField = md.CharField(
        max_length=200
    )
    status: md.CharField = md.CharField(
        max_length=100,
        choices=OperationStatus.choices,
        default=OperationStatus.PENDING.value
    )

    input: md.ForeignKey = md.ForeignKey(
        "Input",
        on_delete=md.CASCADE,
        related_name="operations"
    )

    created_at: md.DateTimeField = md.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.input.input_type} - {self.operation_type}"



class Output(md.Model):
    """ Represents a result generated from an operation """

    output_type: md.CharField = md.CharField(
        max_length=100,
        choices=OutputType,
        default=OutputType.FILE.value
    )

    operation: md.OneToOneField = md.OneToOneField(
        "Operation",
        on_delete=md.CASCADE,
        related_name="output"
    )

    raw_text: md.TextField = md.TextField(null=True)
    media_file: md.OneToOneField = md.OneToOneField(
        "apps.media.MediaFile",
        on_delete=md.CASCADE,
        related_name="output",
        null=True
    )

    text_length: md.PositiveIntegerField = md.PositiveIntegerField(
        null=True
    )
    audio_duration: md.PositiveIntegerField = md.PositiveIntegerField(
        null=True
    ) # if audio file output, save duration in seconds

    created_at: md.DateTimeField = md.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.operation.operation_type} - {self.output_type}"
