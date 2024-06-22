from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Professor name")
    school = models.CharField(max_length=100, verbose_name="which school")
    post = models.CharField(max_length=100, verbose_name="which post")
    subject = models.CharField(max_length=100, verbose_name="subject")
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name


