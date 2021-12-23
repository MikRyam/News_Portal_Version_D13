from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

# создаём новый класс для представления сообщений в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('id', 'author', 'categoryType', 'postTitle', 'postText', 'rating', 'isUpdated', 'pubDate')  # оставляем только имя и цену товара
    list_filter = ('author', 'categoryType', 'postTitle', 'rating', 'isUpdated', 'pubDate')  # добавляем примитивные фильтры в нашу админку

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)

