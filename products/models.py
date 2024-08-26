from django.db import models
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )
    views = models.PositiveIntegerField(default=0)
    tag_hashtags = models.ManyToManyField("Hashtag", related_name="tag_products")

    
    def __str__(self):
        return self.title
    
    def add_hashtags(self, hashtags):
        for tag in hashtags:
            hashtag, _ = Hashtag.objects.get_or_create(keyword=tag)
            self.tag_hashtags.add(hashtag)


class Hashtag(models.Model):
    keyword = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.keyword