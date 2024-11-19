from modules.widget_form import widget


class Widget:
    def __init__(self, id_: int, loaded: bool, title: str,
                 b1_icon, b1_func,
                 b2_icon, b2_func) -> None:
        self.id = id_
        self.qwidget = widget.WidgetWindow(self.id)
        self.title = title

        self.loaded = loaded

        self.b1_icon = b1_icon
        self.b1_func = b1_func

        self.b2_icon = b2_icon
        self.b2_func = b2_func
    
    def copy(self, id_=None):
        if id_ is None: id_ = self.id 
        return Widget(id_, self.loaded, self.title,
                      self.b1_icon, self.b1_func,
                      self.b2_icon, self.b2_func)