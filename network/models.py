from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ManyToManyField(User, related_name="followers", symmetrical=False)

    def __str__(self):
        # get a list of all the users that the current user is following

        following = ", ".join([user.username for user in self.following.all()])
        return f"{self.user} follows {following}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")


    def __str__(self):
        return f"{self.user} {self.timestamp.strftime('%b %d %Y, %I:%M %p')}"

    # This method is used to serialize the data to JSON, but I would stick with the
    # default serializer for now
    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "content": self.content,
    #         "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
    #         "likes": self.likes.count(),
    #         "user": self.user.username
    #     }

