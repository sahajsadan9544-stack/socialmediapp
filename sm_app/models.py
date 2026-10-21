from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    email=models.EmailField()


class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="post_img", null=True)
    description=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment=models.CharField(max_length=800)
    added_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_obj=models.ForeignKey("Post", on_delete=models.CASCADE)

class Like(models.Model):
    post_obj=models.ForeignKey("Post", on_delete=models.CASCADE)
    owner_obj=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=("owner_obj", "post_obj")