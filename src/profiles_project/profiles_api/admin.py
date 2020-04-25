from django.contrib import admin
from . import models  #from current location import models


# Register your models here.

admin.site.register(models.UserProfile)


admin.site.register(models.ProfileFeedItem)
