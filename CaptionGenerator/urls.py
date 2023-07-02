from django.urls import path
from .views import CaptionGeneratorView

urlpatterns = [
    path('caption_generator/', CaptionGeneratorView.as_view(), name='caption_generator'),
]
