from django import template


register = template.Library()


@register.filter(name='enumerate')
def _enumerate(iterable):
    return enumerate(iterable)


@register.filter(name='next')
def _next(obj):
    return next(obj)


@register.filter(name='get_item')
def _get_item(obj, index_):
    return obj[index_]


@register.filter(name='str')
def _str(obj):
    return str(obj)


@register.filter(name='slice')
def _slice(obj, index_):
    if len(obj) >= index_:
        return obj[:index_]
    else:
        return obj