from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Comments(models.Model):
    commented_by = models.CharField(max_length=200)
    body = models.CharField(max_length=2000,null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.commented_by} {self.post}"