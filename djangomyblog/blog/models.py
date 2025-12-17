# djangomyblog\blog\models.py

from django.db import models
from django.conf import settings

STATUS_CHOICES = [
    ('ON', 'Online'),
    ('OFF', 'Offline'),
    ('DEL', 'Deletado'),
]

class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='ON',
        db_index=True
    )
    views = models.PositiveIntegerField(default=0)
    # JSON reservado para uso futuro
    metadata = models.JSONField(blank=True, null=True, default='{}')

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='ON',
        db_index=True
    )
    # JSON reservado para uso futuro
    metadata = models.JSONField(blank=True, null=True, default='{}')

    def __str__(self):
        return f'Comentário #{self.id} por {self.user}'