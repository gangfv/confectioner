from django.contrib import admin
from home.models import Card, Review, Work, Number
from django.contrib.auth.models import Group
admin.site.unregister(Group)

admin.site.register(Card)
admin.site.register(Review)
admin.site.register(Work)
admin.site.register(Number)
