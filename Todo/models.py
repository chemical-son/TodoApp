from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length = 200, blank=False)
    is_compleated = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]


    def __str__(self):
        return self.content