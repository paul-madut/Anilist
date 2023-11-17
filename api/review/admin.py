from django.contrib import admin
from .models import Review
# Register your models here

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', 'anime')

admin.site.register(Review, ReviewAdmin)
