from PyQt6.QtGui import QIcon


def path(file: str) -> str:
    return f'src/images/{file}'


add = QIcon(path('add.svg'))
delete = QIcon(path('delete.svg'))

load = QIcon(path('load.svg'))
unload = QIcon(path('unload.svg'))
reload_ = QIcon(path('reload.svg'))

pin = QIcon(path('pin.svg'))

star = QIcon(path('star.svg'))
full_star = QIcon(path('full_star.svg'))

hide = QIcon(path('hide.svg'))
close = QIcon(path('close.svg'))

left_arrow = QIcon(path('left_arrow.svg'))
right_arrow = QIcon(path('right_arrow.svg'))
