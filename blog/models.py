from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'blog_post'
        verbose_name_plural = 'blog_posts'

    def __str__(self):
        return self.title
