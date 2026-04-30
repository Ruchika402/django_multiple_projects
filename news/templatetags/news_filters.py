from django import template

register = template.Library()

@register.filter(name='word_count')
def word_count(value):
    """
    Returns the number of words in a string
    """
    if not value:
        return 0
    return len(str(value).split())

@register.filter(name='truncate_smart')
def truncate_smart(value, limit=50):
    """
    Truncates text without cutting words
    """
    if not value:
        return ""
    
    words = value.split()
    if len(words) <= limit:
        return value
    
    truncated = ' '.join(words[:limit])
    return truncated + '...'

@register.filter(name='headline_case')
def headline_case(value):
    """
    Converts text to headline case (each word capitalized)
    """
    return ' '.join(word.capitalize() for word in value.split())