from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        Custom user model extending Django's AbstractUser.
        
        Adds a role field with predefined choices for access control.
    """
    class Role(models.TextChoices):
        USER = "user", "User"
        PREMIUM = "premium", "Premium"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=max(len(choice.value) for choice in Role),
        choices=Role.choices,
        default=Role.USER,
    )

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"
