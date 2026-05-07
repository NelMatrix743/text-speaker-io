from django.db import models as md
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class AccountStatus(md.TextChoices):
    """ Account status choices """

    ACTIVE = ("active", "Active")
    EXPIRED = ("expired", "Expired")
    CANCELLED = ("cancelled", "Cancelled")


class PlanType(md.TextChoices):
    """ plan type choices """

    FREE = ("free", "Free")
    STANDARD = ("standard", "Standard")
    PRO = ("pro", "Pro")


class User(AbstractUser):
    """ Represents an authenticated user of the platform """
    email: md.EmailField = md.EmailField(unique=True)

    created_at: md.DateTimeField = md.DateTimeField(auto_now_add=True)
    updated_at: md.DateTimeField = md.DateTimeField(auto_now=True)

    USERNAME_FIELD: str = "email" # use email for login
    REQUIRED_FIELDS: list[str] = [
        "username"
    ]

    def __str__(self):
        return f"EMAIL({self.email}); USERNAME({self.username})"



class Account(md.Model):
    """ Represents a user's subscription and usage """

    user: md.OneToOneField = md.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=md.CASCADE,
        related_name="account"
    )
    plan: md.ForeignKey = md.ForeignKey(
        "Plan",
        on_delete=md.CASCADE,
        related_name="accounts"
    )

    status: md.CharField = md.CharField(
        max_length=10,
        choices=AccountStatus.choices,
        default=AccountStatus.ACTIVE.value
    )

    # subscription date
    sub_start_date: md.DateTimeField = md.DateTimeField()
    sub_end_date: md.DateTimeField = md.DateTimeField(null=True, blank=True)

    # usage metrics
    total_input_created: md.IntegerField = md.IntegerField(default=0)
    total_operations_generated: md.IntegerField = md.IntegerField(default=0)
    total_output_generated: md.IntegerField = md.IntegerField(default=0)
    
    created_at: md.DateTimeField = md.DateTimeField(auto_now_add=True)
    updated: md.DateTimeField = md.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Account #{self.id} - {self.user}"



class Plan(md.Model):
    """ Defines subscription tiers and platform limits """

    type: md.CharField = md.CharField(
        max_length=10,
        choices=PlanType.choices,
        default=PlanType.FREE.value
    )
