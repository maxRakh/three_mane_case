from django import template
from django.core.exceptions import ObjectDoesNotExist

from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = MenuItem.objects.select_related('menu').get(menu__name=menu_name, parent=None)
    context['menu'] = menu
    current_url = context['request'].path
    try:
        current_menu = MenuItem.objects.get(url=current_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = current_menu.get_parents() + [current_menu.id]
        context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids

    return context


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu_children(context, menu_item_id):
    menu_item = MenuItem.objects.select_related('parent', 'menu').get(id=menu_item_id)
    context['menu'] = menu_item

    return context
