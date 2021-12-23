from django import forms
from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post, Category, PostCategory


# Создаём модельную форму
class PostForm(ModelForm):
    check_box = BooleanField(label='Подтвердить!')  # добавляем галочку, или же true-false поле

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'postTitle', 'postCategory', 'postText', 'categoryType',
                  'check_box']  # не забываем включить галочку в поля иначе она не будет показываться


# Создаём модельную форму
# class CategoryForm(ModelForm):
#
#     class Meta:
#         model = Category
#
#         fields = {
#             'categoryName': ['exact'],  # по названию категории (выбор из существуещего списка)
#         }

