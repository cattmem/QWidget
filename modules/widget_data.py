class Widget:
    def __init__(self, title: str,
                 b1_icon, b1_func,
                 b2_icon, b2_func) -> None:
        self.title = title

        self.b1_icon = b1_icon
        self.b1_func = b1_func

        self.b2_icon = b2_icon
        self.b2_func = b2_func