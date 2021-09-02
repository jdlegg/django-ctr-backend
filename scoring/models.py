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

class Flags(models.Model):
    flag = models.CharField(max_length=12);
    points = models.IntegerField();
    name = models.CharField(max_length=20, unique=True);

    def __str__(self):
        return f"{self.name}"

class Score(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, related_name='score_user')
    flags = models.ManyToManyField(Flags, related_name='user_flags')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"
    
    def points_total(self):
        return sum(flags.points for flags in self.flags.all())