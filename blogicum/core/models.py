from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True