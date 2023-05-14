from django.contrib import admin

from blog.models import Post, Category, Popular, Banner

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Popular)
admin.site.register(Banner)