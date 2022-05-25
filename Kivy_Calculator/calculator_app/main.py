from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class OperandsButton(Button):
    pass


class EqualsButton(Button):
    pass


class CalculatorApp(App):

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )

        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                h_layout.add_widget(Button(
                    text=label) if label not in self.operators else OperandsButton(text=label))

            main_layout.add_widget(h_layout)

        main_layout.add_widget(EqualsButton())

        return main_layout

    def btn_pressed(self, instance):
        current = self.solution.text
        btn_pressed = instance.text

        if btn_pressed == "C":
            self.solution.text = ""
            return

        if self.last_was_operator and btn_pressed in self.operators:
            return

        if current == "" and btn_pressed in self.operators:
            return

        self.solution.text = current + btn_pressed if btn_pressed != "=" else current
        self.last_button = btn_pressed
        self.last_was_operator = self.last_button in self.operators

    def equals(self, instance):
        # Eval is dangerous as it can run arbitary code, this is simply a basic
        # calculator example and we are only allowing ints/operators/period as defined
        # within the class
        if self.solution.text:
            try:
                solution = str(eval(self.solution.text))
            except SyntaxError:
                solution = "SyntaxError"
            except ZeroDivisionError:
                solution = "ZeroDivisionError"

            self.solution.text = solution


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
