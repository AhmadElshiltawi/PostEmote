from django.contrib import admin
from .models import Profile, Post, Comment, SuprisedReact, HappyReact, AngryReact, SadReact

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SuprisedReact)
admin.site.register(HappyReact)
admin.site.register(AngryReact)
admin.site.register(SadReact)

