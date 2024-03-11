from django.contrib import admin
from .models import Blog
from .models import Reply
from .models import Comments

# Register your models here.
admin.site.register(Blog)
admin.site.register(Reply)
admin.site.register(Comments)