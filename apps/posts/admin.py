from django.contrib import admin
from models import Categories, Posts, Comments
from forms import PostsAdminForm

# Register your models here.


class PostsComments(admin.StackedInline):
    model = Comments
    extra = 1


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    form = PostsAdminForm
    fields = ('title', 'slug', 'author', 'category', 'display', 'image', 'text')
    inlines = [PostsComments]
    list_filter = ['created_at']


admin.site.register(Categories)
# admin.site.register(Posts, PostsAdmin)
# admin.site.register(Comments)
