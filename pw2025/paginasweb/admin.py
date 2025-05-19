from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Categoria, Post, Comentario, Avaliacao
from .models import Post


admin.site.register(User, UserAdmin)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Avaliacao)
