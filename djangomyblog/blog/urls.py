# djangomyblog\blog\urls.py

from django.urls import include, path
from .views import about, home, post_detail, signup, profile

urlpatterns = [
    path('', home),
    path('about/', about),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('profile/', profile),
    path('post/<int:id>/', post_detail, name='post_detail'),
]