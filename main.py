from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)
global flagmaster1
global flagmaster2
class MyApp(App):

    def build(self):
        global flagmaster1
        global flagmaster2
        flagmaster1 = False
        flagmaster2 = False
        self.title = 'My Kivy App'  # Set the title here

        layout = RelativeLayout(size=(300, 300))
        self.image = AsyncImage(source='logo.png', pos_hint = {'center_x': .5, 'center_y': .75},)


        self.username_input = TextInput(text='USERNAME', multiline=False, size_hint=(0.5, None), height=30,
                                        pos_hint = {'center_x': .5, 'center_y': .5}, halign='center')
        self.username_input.bind(focus=self.on_username_input_focus)
        self.username_input.bind(on_text_validate=self.on_enter)

        self.password_input = TextInput(text='PASSWORD',password=False, multiline=False, size_hint=(0.5, None), height=30,
                                        pos_hint = {'center_x': .5, 'center_y': .4}, halign='center')
        self.password_input.bind(focus=self.on_password_input_focus)
        self.password_input.bind(on_text_validate=self.on_sec)


        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.image)

        return layout

    def on_password_input_focus(self, instance, value):
        if value:
            self.password_input.password = True
            self.password_input.text = ''
    def on_username_input_focus(self, instance, value):
        if value:
            self.username_input.text = ''

    def on_enter(self, instance):
        global flagmaster1
        global flagmaster2
        user_input = self.username_input.text
        if user_input == "felipe":
            flagmaster1 = True
            self.username_input.text = "WELCOME " + str.upper(user_input)
            if flagmaster2:
                print("FULL ON 1")
            else:
                pass
        else:
            self.username_input.text = 'UNKNOWN USERNAME'

    def on_sec(self, instance):
        global flagmaster1
        global flagmaster2
        user_input = self.password_input.text
        if user_input == "rana":
            flagmaster2 = True
            self.password_input.password = False
            self.password_input.text = "AUTHORIZED"
            if flagmaster1:
                print("FULL ON 2")
            else:
                pass
        else:
            self.password_input.password = False
            self.password_input.text = 'UNKNOWN PASSWORD'




if __name__ == '__main__':
    MyApp().run()
