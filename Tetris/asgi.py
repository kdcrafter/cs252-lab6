
import os

from channel.asgi import get_channel_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tetris.settings')

channel_layer = get_channel_layer()