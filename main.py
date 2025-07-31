from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyCalculator(BoxLayout):
    def calculate(self):
        try:
            a, o, y = self.ids.input.text.split()
            a = int(a)
            y = int(y)
            if o == "+":
                result = a + y
            elif o == "-":
                result = a - y
            elif o == "×":
                result = a * y
            elif o == "÷":
                result = a // y if y != 0 else "Invalid operation"
            else:
                result = "Unknown operator"
            self.ids.output.text = str(result)
        except:
            self.ids.output.text = "Error"

    def clear(self):
        self.ids.input.text = ""
        self.ids.output.text = ""

class MyApp(App):
    def build(self):
        return MyCalculator()

MyApp().run()