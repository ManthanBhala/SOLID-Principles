class MouseInterface:
    def __init__(self):
        pass


class WiredMouse(MouseInterface):
    def __init__(self):
        pass


class Laptop:
    def __init__(self):
        self.mouse = MouseInterface()