from typing import Dict, Any

from django import template
from django.template import Context

from tree.models import MenuItem, Menu


register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context: Context, menu: str) -> Dict[str, Any]:
    """template for generate tree menu

    Args:
        context (_type_): request and other params
        menu (_type_): name of main tree menu

    Returns:
        context Dict[str, Any]
    """
    link = context.request.path[1:]
    main_menu = Menu.objects.filter(link=menu).first()

    down_items = []
    up_items = {}
    if link == main_menu.link:
        # if url is in main menu
        menu_items = MenuItem.objects.filter(menu__link=menu, parent=None)
        up_items = {'level': menu_items}
    else:
        # if url is not in main menu
        menu_items = MenuItem.objects.filter(menu__link=menu)
        if menu_items.filter(link=link).exists():
            down_items = menu_items.filter(parent__link=link)
            curent_item = MenuItem.objects.get(link=link)
            up_items = {'level': down_items}
            while curent_item:
                level = menu_items.filter(parent=curent_item.parent)
                buf = {'next': up_items}
                buf['active'] = curent_item
                buf['level'] = level
                up_items = buf
                curent_item = curent_item.parent

    # items - tree of ItemMenu, main_menu - name of main menu
    context['items'] = up_items
    context['main_menu'] = main_menu
    return context
