def text_color(color_theme:str):
    """
    Help changing the color theme for specific events
    :param color_theme: what type of color do we need?
    :return: the color code
    """
    color_dict = {
        'base': '\033[97m',  # white
        'ERROR': '\033[91m',  # red
        'backup': '\033[96m',  # cyan
        'INFO': '\033[92m',  # green
        'TITLE': '\033[93m'  # yellow
    }
    try:
        return color_dict[color_theme]
    except:
        return color_dict['base']
