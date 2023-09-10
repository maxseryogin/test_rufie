from kivy.uix.label import Label


class Sits(Label):
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = "Залишилось присідань: " + str(self.total)
        super().__init__(text=my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        self.remain = max(0, self.total - self.current)
        my_text = "Залишилось присідань: " + str(self.remain)
        self.text = my_text
