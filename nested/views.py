from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin


def generate_nested___test(request):
    messages.success(request, "Nested categories generated successfully.")
    referer_url = request.META.get('HTTP_REFERER')

    if referer_url:
        return redirect(referer_url)
    else:
        return redirect('/admin/')


@staff_member_required
def generate_nested(request, app_name, model_name):
    admin_context = admin.site.each_context(request)
    admin_context.update({
        "title": "Nested Tree",
        'message': "Nested categories have been generated!",
        'additional_data': "Here you can add extra details about the process.",
    })
    print("admin_context", admin_context)
    return render(request, 'admin/nested/generate_nested.html', admin_context)
