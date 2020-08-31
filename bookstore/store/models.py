from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = "Тэги"

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

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
