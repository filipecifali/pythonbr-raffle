from django.contrib import admin

from lottery.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['pk']
    ordering = ['pk']
    actions = ['select_one']

    def select_one(self, request, queryset):
        selected = Person.objects.order_by('?').first()

        # XXX check the origin database
        self.message_user(request, '{} ({}), I CHOOSE YOU!!!'.format(
                          selected.name,
                          selected.email))

# Register your models here.
admin.site.register(Person, PersonAdmin)
