from django.contrib import admin


class NestedCategoryAdmin(admin.ModelAdmin):
    list_display = ('nested_is_active', 'nested_parent', 'nested_left', 'nested_right', 'nested_row',
                    'nested_child_count')
    readonly_fields = ('nested_is_active', 'nested_left', 'nested_right', 'nested_row', 'nested_child_count')
    list_filter = ('nested_is_active', 'nested_parent')
    search_fields = ('name',)
    change_list_template = "admin/nested-set-model/change_list.html"
    ordering = ('id',)
