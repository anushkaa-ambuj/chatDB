from django.urls import path
from .views import TextToSQLAPIView, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Root URL to show a welcome message
    path('text-to-sql/', TextToSQLAPIView.as_view(), name='text_to_sql'),  # API endpoint
]
