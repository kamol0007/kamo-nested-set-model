from django.contrib import admin

class NestedCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'nested_left', 'nested_right', 'nested_row', 'nested_parent')
    list_filter = ('nested_parent',)
    search_fields = ('name',)