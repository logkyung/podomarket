from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post

# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (
    ('Custom Fields', {"fields": ('nickname', 'kakao_id', 'address','profile_pic')}),
)

admin.site.register(Post)