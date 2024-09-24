from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class Tweet(models.Model):
    text_tweet = models.TextField(max_length=280)
    author_tweet = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tweets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tweet by {self.author_tweet.username}: {self.text_tweet[:50]}..."

class Like(models.Model):
    user_like = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    connection = models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_like.username} liked {self.connection.id}"

class Follow(models.Model):
    other_users = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    link_between_users = models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.other_users.username} follows {self.link_between_users.username}"









