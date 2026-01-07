# djangomyblog\blog\urls.py

from django.urls import include, path
from .views import about, comment_post, delete_post, edit_post, home, new_post, post_detail, signup

urlpatterns = [
    path('', home, name='home'),
    path('about/', about),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('new/', new_post, name='new_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),
    path('edit/<int:id>/', edit_post, name='edit_post'),
    path("comment/", comment_post, name="comment_post"),
]