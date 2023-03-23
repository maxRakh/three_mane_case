from django.contrib import admin

from menu_app.models import MenuItem, Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_id', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {'named_url': ('url',)}


admin.site.register(MenuItem, MenuAdmin)
admin.site.register(Menu)
