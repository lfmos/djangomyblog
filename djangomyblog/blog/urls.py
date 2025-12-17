# djangomyblog\blog\urls.py

from django.urls import include, path
from .views import about, delete_post, home, new_post, post_detail, signup, profile

urlpatterns = [
    path('', home, name='home'),
    path('about/', about),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('profile/', profile),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('new/', new_post, name='new_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),
]