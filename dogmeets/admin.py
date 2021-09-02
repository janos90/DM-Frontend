from django.contrib import admin
from dogmeets.models import Dog, Activity, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Dog)
admin.site.register(Activity)