from django.db import models

# Create your models here.
class Blog(models.Model):

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

        ordering = ['category', 'title']
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    content = models.TextField(verbose_name="description")
    category = models.CharField(max_length=30)

    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title