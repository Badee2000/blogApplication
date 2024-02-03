from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # This attribute specifies the fields to be displayed in the admin list view for the `Post` model. In this case, the list will include the `title`, `slug`, `author`, `publish`, and `status` fields.
    list_display = ['title', 'slug', 'author', 'publish', 'status',]
    # This attribute adds filters to the admin list view, allowing you to filter posts based on specific criteria. The filters include `status`, `created` (date created), `publish` (date published), and `author`.
    list_filter = ['status', 'created', 'publish', 'author']
    # This attribute adds filters to the admin list view, allowing you to filter posts based on specific criteria. The filters include `status`, `created` (date created), `publish` (date published), and `author`.
    search_fields = ['title', 'body']
    # This attribute automatically populates the `slug` field based on the value of the `title` field. In this case, the `slug` field will be prepopulated using the `title` field.
    prepopulated_fields = {'slug': ('title',)}
    # This attribute replaces the default dropdown select widget for the `author` field with a raw id input field. This is useful when there are many authors and selecting from a dropdown becomes impractical.
    raw_id_fields = ['author']
    # This attribute adds a date-based drill-down navigation in the admin interface, allowing you to navigate posts by their `publish` date. It creates a hierarchy based on the `publish` field.
    date_hierarchy = 'publish'
    # This attribute specifies the default ordering of posts in the admin list view. In this case, the posts will be ordered by `status` first and then by `publish`.
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
