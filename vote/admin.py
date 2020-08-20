from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from vote.models import Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_name', 'vote_cnt', 'ongoing', 'elected')


admin.site.register(Vote, VoteAdmin)
