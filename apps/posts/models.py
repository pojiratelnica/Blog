# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta(object):
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=45)

    def __unicode__(self):
        return "%s" % (self.title)


class Article(models.Model):
    class Meta(object):
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=45)
    author = models.ForeignKey(User, blank=True, null=True)
    category = models.ForeignKey(Category, null=True)
    image = models.ImageField(max_length=256, null=True, upload_to='posts/images/')
    text = models.TextField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    display = models.BooleanField(default=True)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)

    def __unicode__(self):
        return "%s" % (self.title)
