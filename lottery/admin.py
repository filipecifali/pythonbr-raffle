from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from lottery.models import Person, Registration


class PersonAdmin(admin.ModelAdmin):
    list_display = ['pk']
    ordering = ['-pk']

    def get_urls(self):
        urls = super(PersonAdmin, self).get_urls()
        my_urls = [
            path(r'election/', self.select_one, name='election')
        ]
        return my_urls + urls

    def select_one(self, request):
        while True:
            registered = Registration.objects.order_by('?').first()
            try:
                selected = Person.objects \
                    .filter(email=registered.email) \
                    .first()
                self.message_user(
                    request,
                    '{} ({}), I ARE A WINNER!!!'.format(
                        selected.name,
                        selected.email))
                break
            except (Person.DoesNotExist, AttributeError):
                # Attribute error happens when filter finds no records,
                # returns nNone and we try to print `.name` out of it.
                self.message_user(
                    request,
                    '{} selected, but not in the raffle'.format(
                        registered.email))
        return HttpResponseRedirect(request.META["HTTP_REFERER"])


admin.site.register(Person, PersonAdmin)
admin.site.register(Registration)
