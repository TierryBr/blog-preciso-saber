from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
  title = models.CharField(max_length=50, default='geral')

  class Meta:
    verbose_name_plural = 'categorias'

  def __str__(self):
    return self.title


class Post(models.Model):
  title = models.CharField(max_length=255)
  cover = models.CharField(max_length=500)
  summary = RichTextField()
  content = RichTextField()
  author = models.ForeignKey(User, on_delete=models.PROTECT)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Postagens'

  def __str__(self):
    return self.title


class Popular(models.Model):
  post = models.ForeignKey(Post, on_delete=models.PROTECT)

  class Meta:
    verbose_name_plural = 'Populares'

  def __str__(self):
    return self.post.title


class Banner(models.Model):
  post = models.ForeignKey(Post, on_delete=models.PROTECT)

  class Meta:
    verbose_name_plural = 'Banner'

  def __str__(self):
    return self.post.title

