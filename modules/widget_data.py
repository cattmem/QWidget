from modules.widget_form import widget


class Widget:
    def __init__(self, id_: int, loaded: bool,
                 title: str, preview, type_: int,
                 b1_icon, b1_func,
                 b2_icon, b2_func, context_menu: list[dict]) -> None:
        self.id = id_
        self.qwidget = widget.WidgetWindow(self.id)

        self.title = title
        self.preview = preview
        self.type = type_

        self.loaded = loaded

        self.b1_icon = b1_icon
        self.b1_func = b1_func

        self.b2_icon = b2_icon
        self.b2_func = b2_func

        self.context_menu = context_menu
    
    def copy(self, id_=None):
        if id_ is None:
            id_ = self.id 
        return Widget(id_, self.loaded,
                      self.title, self.preview, self.type,
                      self.b1_icon, self.b1_func,
                      self.b2_icon, self.b2_func,
                      self.context_menu)