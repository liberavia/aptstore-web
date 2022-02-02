from django.contrib import admin
from .models import (
    App,
    AppRegional,
    Tag,
    Category,
    CategoryRegional,
    Screenshot,
    Platform
)

admin.site.register(App)
admin.site.register(AppRegional)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(CategoryRegional)
admin.site.register(Screenshot)
admin.site.register(Platform)
