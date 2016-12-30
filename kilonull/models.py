from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey('auth.user')
    body = models.TextField()
    published = models.DateField(db_index=True, auto_now_add=True)
    category = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    hide_listing = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.slug)

    def get_absolute_url(self):
        return reverse('kilonull:view_blog_post', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return '{}'.format(self.slug)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('kilonull:view_blog_category', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return '{}'.format(self.slug)

    def get_absolute_url(self):
        return reverse('kilonull:view_blog_tag', args=(self.slug))


class Menu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.slug)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    order = models.IntegerField()
    link_url = models.CharField(max_length=255)
    link_text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return '{0} in {1}'.format(self.link_text, self.menu.slug)
