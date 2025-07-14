from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# PUBLIC_INTERFACE
class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on notes.
    Only authenticated users may access. Users may only access their own notes.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Show only user's own notes
        return Note.objects.filter(user=self.request.user).order_by('-updated_at')

    def perform_create(self, serializer):
        # Assign note ownership to logged in user.
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """Create a new note for the authenticated user."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Update an existing note for the authenticated user."""
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete one of the user's own notes."""
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a user's note by ID."""
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """List all notes belonging to the authenticated user."""
        return super().list(request, *args, **kwargs)
