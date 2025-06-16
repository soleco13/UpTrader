from django import template
from django.urls import resolve
from tree_menu.models import Menu, MenuItem

register = template.Library()


def get_active_items(menu_items, current_url):
    active_items = set()
    
    for item in menu_items:
        item_url = item.get_url()
        if item_url == current_url:
            # Добавляем текущий элемент и всех его родителей
            active_items.add(item)
            parent = item.parent
            while parent:
                active_items.add(parent)
                parent = parent.parent
            # Добавляем прямых детей текущего элемента
            active_items.update(item.children.all())
    
    return active_items


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(menu_name):
    current_url = resolve(request.path).url_name or request.path
    
    # Получаем все пункты меню одним запросом
    menu_items = MenuItem.objects.filter(
        menu__name=menu_name
    ).select_related('parent', 'menu').prefetch_related('children')
    
    # Определяем активные элементы
    active_items = get_active_items(menu_items, current_url)
    
    # Формируем дерево меню
    menu_tree = []
    for item in menu_items:
        if not item.parent:  # Корневые элементы
            menu_tree.append({
                'item': item,
                'is_active': item in active_items,
                'children': [
                    {'item': child, 'is_active': child in active_items}
                    for child in item.children.all()
                ]
            })
    
    return {'menu_tree': menu_tree} 