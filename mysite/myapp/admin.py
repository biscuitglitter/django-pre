from django.contrib import admin

from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("reference", "status", "category", "created_at", "updated_at")
    search_fields = ("status", "category")
