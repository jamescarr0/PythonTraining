'''
Kivy Demo.
Vertical layout with buttons.
Uses KV language to separate the interface design from application logic: button.kv
'''

import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class ButtonApp(App):
    """
    Seperation of concerns, button attributes written in KV
    file: 'button.kv'
    """
    def build(self):
        layout = BoxLayout(orientation='vertical')
        colors = [red, green, blue, purple]

        for i in range(4):
            btn = Button(text=f"{i}", background_color=colors[i])
            layout.add_widget(btn)
        return layout

    def btn_pressed(self, instance):
        print(f"Your pressed button {instance.text}")

if __name__ == '__main__':
    app=ButtonApp()
    app.run()