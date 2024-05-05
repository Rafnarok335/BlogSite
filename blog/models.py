from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15, null=False)
    profile_picture = models.ImageField()


class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='-')

    class Meta:
        db_table = 'blog_BlogPosts'
        indexes = [
            models.Index(fields=['author', 'time'])
        ]
