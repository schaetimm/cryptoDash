from django import template

register = template.Library()


@register.filter
def split_name(name):
    if not name:
        return ''

    # Check if the last four characters are all uppercase, if so, split there.
    if ("XRP") in name:
        return "XRP"
    elif ("BNB") in name:
        return "BNB"
    elif ("USDT") in name:
        return " Tether USDt"
    if name[-4:].isupper():
        return name[:-4]
    # Otherwise, try splitting at the last three characters.
    elif name[-3:].isupper():
        return name[:-3]
    else:
        # If no clear abbreviation is detected, return the name as it is.
        return name

