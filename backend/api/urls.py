from django.urls import path, include
from .views import health
from rest_framework.routers import DefaultRouter
from .views_notes import NoteViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('health/', health, name='Health'),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),  # DRF login/logout
    path('', include(router.urls)),    # all /api/notes/ routes
]
