from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_migrate

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in list view
    search_fields = ('title', 'author')  # Enable search
    list_filter = ('publication_year',)  # Enable filtering

admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


def create_groups_and_permissions():
    book_content_type = ContentType.objects.get_for_model(Book)


    permissions = {
        "can_view": Permission.objects.get(codename="can_view", content_type=book_content_type),
        "can_create": Permission.objects.get(codename="can_create", content_type=book_content_type),
        "can_edit": Permission.objects.get(codename="can_edit", content_type=book_content_type),
        "can_delete": Permission.objects.get(codename="can_delete", content_type=book_content_type),
    }


    groups = {
        "Viewers": [permissions["can_view"]],
        "Editors": [permissions['can_edit'], permissions['can_create']],
        "Admins": permissions.values(),
    }


    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        group.permissions.set(perms)

@receiver(post_migrate)
def create_groups_and_permissions_signal(sender, **kwargs):
    create_groups_and_permissions()