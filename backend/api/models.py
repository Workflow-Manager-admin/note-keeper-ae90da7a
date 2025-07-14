from django.db import models
from django.conf import settings

# PUBLIC_INTERFACE
class Note(models.Model):
    """Represents a Note belonging to a user."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes',
        help_text="Owner of the note"
    )
    title = models.CharField(max_length=255, help_text="Title of the note")
    content = models.TextField(help_text="Content of the note")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last update timestamp")

    def __str__(self):
        return f"{self.title} ({self.user})"
