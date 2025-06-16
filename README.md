# Django Tree Menu

Приложение для создания и отображения древовидных меню в Django.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Добавьте 'tree_menu' в INSTALLED_APPS в settings.py

3. Выполните миграции:
```bash
python manage.py migrate
```

## Использование

1. Создайте меню через админ-панель Django
2. Используйте тег в шаблоне:
```html
{% load tree_menu %}
{% draw_menu 'main_menu' %}
``` 