from django.contrib import admin
from .models import App, Tag, Category, Screenshot, Platform

admin.site.register(App)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Screenshot)
admin.site.register(Platform)
