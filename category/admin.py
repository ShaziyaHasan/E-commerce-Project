from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from .models import Category

class DoInactiveActionsMixin(object):
    def get_inline_actions(self, request, obj=None):
        actions = super(DoInactiveActionsMixin, self).get_inline_actions(request, obj)
        if obj:
            if obj.status == Category.a:
                actions.append('inactivate')
            elif obj.status == Category.i:
                actions.append('activate')
        return actions

    def inactivate(self, request, obj, parent_obj=None):
        obj.status = Category.i
        obj.save()
        messages.info(request, _("Status Inactive."))

    inactivate.short_description = _("Active")

    def activate(self, request, obj, parent_obj=None):
        obj.status = Category.a
        obj.save()
        messages.info(request, _("Status Active."))
    activate.short_description = _("Inactivate")

@admin.register(Category)
class CategoryAdmin(DoInactiveActionsMixin,admin.ModelAdmin):
    def fullpath(self, obj):
        print(repr(obj))
        if obj.parent is not None:
            return format_html("{}->{}", obj.parent, obj.name)
        else:
            return format_html("{}", obj.name)

    def category_name(self, obj):
        return capfirst(obj.name)

    exclude = ('slug',)

    list_display = ('category_name', 'fullpath', 'description', 'status')


