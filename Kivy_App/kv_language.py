# Using the KV language as a seperation of concerns, as part of MVC.
# button.kv defines button properties.

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def btn_pressed(self, instance):
        print(f'You pressed the button! {instance.text}')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()