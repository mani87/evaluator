from django import template

register = template.Library()

@register.filter
def get_question(value, number):
	return value[number-1].statement