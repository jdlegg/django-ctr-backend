from enum import Flag
from django.contrib import admin
from .models import *

admin.site.register(Score)
admin.site.register(WebFlagMaster)
admin.site.register(Flags)