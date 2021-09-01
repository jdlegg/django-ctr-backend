from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from authentication.models import CustomUser
from django.utils.text import slugify

class WebFlagMaster(models.Model):
    flag = models.CharField(max_length=12);
    points = models.IntegerField();
    name = models.CharField(max_length=20);
    def __str__(self):
        return f"{self.name}"

class Score(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='score_user')
    points = IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"