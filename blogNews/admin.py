from django.contrib import admin
from .models import New

# Register your models here.

admin.site.site_header="Initial Project";
admin.site.site_title="Initial Project";

class NewAdmin(admin.ModelAdmin):
    list_display = ['title','subtitle','published_date']
    pass
admin.site.register(New,NewAdmin)

"""
admin.site.unregister(User)

class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )

admin.site.register(User, MyUserAdmin)
"""