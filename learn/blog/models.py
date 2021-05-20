from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user is needed because they will act as the author to the posts
#User is a different table to posts and we merge those table

class  Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #author acts as a foreign key between user and the post table.

    def __str__(self):
        return self.title