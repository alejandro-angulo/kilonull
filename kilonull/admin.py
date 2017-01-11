from django import forms
from django.conf import settings
from django.contrib import admin

from kilonull.models import Post, Category, Tag, Menu, MenuItem


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'published', 'slug']
    search_fields = ['title', 'body']
    date_hierarchy = 'published'
    exclude = ('author', 'body_html')

    def save_model(self, request, obj, form, change):
        # if not change:
        #     obj.author = request.user
        # obj.parse_body_markdown()
        obj.author = request.user
        obj.save()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    search_fields = ('post')


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}


class MenuForm(forms.ModelForm):
    class Media:
        model = Menu
        js = (
            '{}kilonull/jquery/jquery-3.1.1.min.js'.format(settings.STATIC_URL),
            '{}kilonull/jquery/jquery-ui.min.js'.format(settings.STATIC_URL),
            '{}kilonull/js/menu-sort.js'.format(settings.STATIC_URL),
        )

admin.site.register(Menu, inlines=[MenuItemInline], form=MenuForm,
                    prepopulated_fields={'slug': ('title',)})
