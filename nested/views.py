from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin


def generate_nested(request):
    messages.success(request, "Nested categories generated successfully.")
    referer_url = request.META.get('HTTP_REFERER')

    if referer_url:
        return redirect(referer_url)
    else:
        return redirect('/admin/')


@staff_member_required
def generate_nested2(request):
    messages.success(request, "Nested categories generated successfully.")

    # Admin interfeysi uchun zarur kontekstni olish
    admin_context = admin.site.each_context(request)

    # Maxsus ma'lumotlarni qo'shish
    admin_context.update({
        'message': "Nested categories have been generated!",
        'additional_data': "Here you can add extra details about the process.",
    })

    return render(request, 'admin/nested/generate_nested.html', admin_context)
