from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
def log():
    Config.set('graphics', 'resizable', True)
    global flagmaster1
    global flagmaster2

    class MyApp(App):

        def build(self):
            global flagmaster1
            global flagmaster2
            flagmaster1 = False
            flagmaster2 = False
            self.title = 'LOGIN'  # Set the title here

            layout = RelativeLayout(size=(300, 300))
            self.image = AsyncImage(source='logo.png', pos_hint={'center_x': .5, 'center_y': .75}, )

            self.username_input = TextInput(text='', multiline=False, size_hint=(0.5, None), height=30,
                                            pos_hint={'center_x': .5, 'center_y': .5}, halign='center')
            self.username_input.focus = True
            self.username_input.bind(focus=self.on_username_input_focus)
            self.username_input.bind(on_text_validate=self.on_enter)

            self.password_input = TextInput(text='PASSWORD', password=False, multiline=False, size_hint=(0.5, None),
                                            height=30,
                                            pos_hint={'center_x': .5, 'center_y': .4}, halign='center',opacity = 0)
            self.password_input.bind(focus=self.on_password_input_focus)
            self.password_input.bind(on_text_validate=self.on_sec)
            self.hint = Label(text = str.upper("usuário"),color= "red",pos_hint={'center_x': .29, 'center_y': .55}, halign='center',opacity = 1)
            self.hint2 = Label(text = "SENHA",color= "red",pos_hint={'center_x': .28, 'center_y': .45}, halign='center',opacity = 0)
            layout.add_widget(self.hint)
            layout.add_widget(self.hint2)
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
                self.username_input.text = "Olá " + user_input.capitalize()
                self.password_input.opacity = 1
                self.hint2.opacity = 1
                self.password_input.focus = True

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
                    App.stop(self)
                    firtsoff()
                else:
                    pass
            else:
                self.password_input.password = False
                self.password_input.text = 'UNKNOWN PASSWORD'

    if __name__ == '__main__':
        MyApp().run()
def firtsoff():
    Config.set('graphics', 'resizable', True)
    global flagmaster1
    global flagmaster2

    class MyApp(App):

        def build(self):
            self.title = 'MENU'  # Set the title here

            layout = RelativeLayout(size=(300, 300))
            self.licks = Label(text = "ALL CAPS")
            self.image = AsyncImage(source='logo.png', pos_hint={'center_x': .5, 'center_y': .75}, )

            layout.add_widget(self.image)
            layout.add_widget(self.licks)

            return layout



    if __name__ == '__main__':
        MyApp().run()


log()
