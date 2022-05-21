from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Window.size = (1000, 800)

class MainWidget(GridLayout):
    def on_button_click(self):
        print("Button clicked")



    # def selected(self, filename):
    #     try:
    #         self.ids.my_file.source = filename[0]
    #         print(filename[0])
    #
    #     except:
    #         pass


class ConcurWorkday(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    window = ConcurWorkday()
    window.run()