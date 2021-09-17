from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user is needed because they will act as the author to the posts
#User is a different table to posts and we merge those table
from django.urls import reverse

class  Post(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #author acts as a foreign key between user and the post table.

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    #recerse returns the url as string to the route.
    #self.pk helps to get to the particular post.