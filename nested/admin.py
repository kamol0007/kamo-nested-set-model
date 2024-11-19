from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

class NestedCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'nested_left', 'nested_right', 'nested_row', 'nested_parent')
    readonly_fields = ('nested_left', 'nested_right', 'nested_row' )
    list_filter = ('nested_parent',)
    search_fields = ('name',)
    change_list_template = "admin/nested/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate-nested/', self.generate_nested, name='generate_nested'),
        ]
        return custom_urls + urls

    def generate_nested(self, request):
        self.message_user(request, "Nested categories generated successfully.")
        referer_url = request.META.get('HTTP_REFERER')

        if referer_url:
            return redirect(referer_url)
        else:
            return redirect('/admin/')
         