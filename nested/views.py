from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from django.apps import apps


def generate_nested___test(request):
    messages.success(request, "Nested categories generated successfully.")
    referer_url = request.META.get('HTTP_REFERER')

    if referer_url:
        return redirect(referer_url)
    else:
        return redirect('/admin/')


@staff_member_required
def generate_nested(request, app_name, model_name):
    # NestedModel = None
    try:
        nestedModel = apps.get_model(app_label=app_name, model_name=model_name)
        data = nestedModel.objects.all()
        print('data', data)
        admin_context = admin.site.each_context(request)
        admin_context.update({
            "title": "Nested Set Model - " + app_name.capitalize() + "." + model_name.capitalize(),
            'additional_data': "Commit your changes to the nested model and regenerate the tree. You cannot automatically revert to the current state after generation.",
        })
        return render(request, 'admin/nested-set-model/generate_nested.html', admin_context)
    except LookupError:
        messages.error(request, f"Model '{app_name}.{model_name}' not found.")
        admin_context = admin.site.each_context(request)
        admin_context.update({
            "title": "Nested Set Model - " + app_name.capitalize() + "." + model_name.capitalize(),
            'additional_data': "Commit your changes to the nested model and regenerate the tree. You cannot automatically revert to the current state after generation.",
        })
        return render(request, 'admin/nested-set-model/generate_nested.html', admin_context)
