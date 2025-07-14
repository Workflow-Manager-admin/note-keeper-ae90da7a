from rest_framework import serializers
from .models import Note

# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note with validation for non-empty title and content."""

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Note title cannot be empty.")
        return value

    def validate_content(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Note content cannot be empty.")
        return value
