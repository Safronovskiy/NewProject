from django.db import models



class BlogPost(models.Model):
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=2000, blank=True)
    is_published = models.DateTimeField(auto_now=True)
    is_edited = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    is_archivated = models.BooleanField(default=False)
    res = models.CharField(max_length=100,blank=True, null=True)
    res1 = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

class BlogCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'













