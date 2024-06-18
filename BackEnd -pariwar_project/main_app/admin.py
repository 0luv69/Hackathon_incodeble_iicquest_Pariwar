from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(IssueModel)
admin.site.register(ReplyModel)
admin.site.register(RelationModel)
admin.site.register(ChatModel)