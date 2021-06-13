from django.contrib import admin
from core.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone_no",
    )
    search_fields = (
        "phone_no",
    )