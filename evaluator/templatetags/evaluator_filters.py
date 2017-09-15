from django import template
import random

register = template.Library()

@register.filter
def get_question(value, number):
	return value[number-1].statement

@register.filter
def get_color(value):
	return random.choice(["#FFCA28", "#2196F3", "#ASAAAE", "#6DD8D1F", "#9CCC65", "#EC407A", "#666666"])