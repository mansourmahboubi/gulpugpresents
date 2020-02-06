from django.db import models


class Persentation(models.Model):
    title = models.CharField(max_length=50)
    presenter = models.CharField(max_length=20)
    descripton = models.CharField(max_length=250)
    presentaion_link = models.URLField(max_length=300)
    author_link = models.URLField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.title