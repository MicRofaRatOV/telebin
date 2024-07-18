from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import markdown

register = template.Library()


@register.filter(name="replace")
def replace(value: str, args: str) -> str:
    arg_list = [arg for arg in args.split("->")]
    return value.replace(arg_list[0], arg_list[1])


@register.filter
@stringfilter
def md_render(value):
    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])
    return mark_safe(md.convert(value))


@register.filter
@stringfilter
def text_render(value):
    return mark_safe(value.replace("\n", "<br/>"))
