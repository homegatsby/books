from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

