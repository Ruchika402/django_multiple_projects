from django import template

register = template.Library()

@register.filter(name='word_count')
def word_count(value):
    """Returns the number of words in a string"""
    if not value:
        return 0
    return len(str(value).split())

@register.filter(name='reading_time')
def reading_time(value, words_per_minute=200):
    """Estimates reading time in minutes"""
    if not value:
        return 0
    word_count = len(str(value).split())
    minutes = round(word_count / words_per_minute)
    return max(1, minutes)

@register.filter(name='headline_case')
def headline_case(value):
    """Converts to headline case (capitalizes each word)"""
    if not value:
        return ""
    return ' '.join(word.capitalize() for word in value.split())