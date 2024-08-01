from pystray import Icon, MenuItem, Menu
from PIL import Image
import logging
from tools import href

def create_icon(close_callback):
    logging.info('Create Icon')
    icon = Icon('App Icon',
                icon=Image.open(href('templates', 'icon.png')),
                menu=Menu(MenuItem('Close', close_callback))
               )
    return icon
