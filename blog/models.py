
from django.db import models
from django.contrib.auth.models import  User

class Categories(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    categories= models.ManyToManyField(Categories)
    image = models.ImageField(upload_to="doctor/images/")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    def __str__(self):
        return self.title










STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    def __str__(self):
        return self.reviewer.title

    