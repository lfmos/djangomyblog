# djangomyblog\blog\urls.py

from django.urls import include, path
from .views import about, home, signup, profile

urlpatterns = [
    path('', home),
    path('about/', about),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('profile/', profile),
]