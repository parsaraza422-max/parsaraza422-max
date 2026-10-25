from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor = (0.045, 0.055, 0.12, 1)
KV = '''
#:import dp kivy.metrics.dp
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(18)
        spacing: dp(12)
        canvas.before:
            Color:
                rgba: .045,.055,.12,1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'REZA PLUS  +'
            font_size: '30sp'
            bold: True
            color: .55,.45,1,1
            size_hint_y: .14
        Label:
            text: 'Your everyday super app'
            color: .72,.77,.95,1
            size_hint_y: .07
        GridLayout:
            cols: 2
            spacing: dp(12)
            size_hint_y: .66
            Button:
                text: 'AI Assistant'
                on_release: app.open_page('AI Assistant', 'AI chat needs a connected service. This is a demo.')
            Button:
                text: 'Classifieds'
                on_release: app.open_page('Classifieds', 'Post and browse listings (demo).')
            Button:
                text: 'Games'
                on_release: app.open_page('Games', 'Your game library (demo).')
            Button:
                text: 'Community'
                on_release: app.open_page('Community', 'Online messaging requires a server.')
            Button:
                text: 'Profile'
                on_release: app.open_page('Profile', 'Welcome to your profile!')
            Button:
                text: 'Notifications'
                on_release: app.open_page('Notifications', 'No notifications yet.')
        Button:
            text: 'Change theme'
            size_hint_y: .1
            on_release: app.change_theme()
        Label:
            text: 'Offline demo  |  v0.1'
            color: .65,.7,.8,1
            size_hint_y: .06
<PageScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(22)
        spacing: dp(20)
        Label:
            text: app.page_title
            font_size: '27sp'
            bold: True
            color: .55,.45,1,1
        Label:
            text: app.page_body
            text_size: self.width, None
            halign: 'center'
            color: .85,.87,1,1
        Button:
            text: 'Back to home'
            size_hint_y: .15
            on_release: app.root.current = 'home'
ScreenManager:
    MainScreen:
        name: 'home'
    PageScreen:
        name: 'page'
'''
class MainScreen(Screen): pass
class PageScreen(Screen): pass
class RezaPlus(App):
    page_title = StringProperty('')
    page_body = StringProperty('')
    def build(self):
        self.title = 'Reza Plus'
        return Builder.load_string(KV)
    def open_page(self, title, body):
        self.page_title, self.page_body = title, body
        self.root.current = 'page'
    def change_theme(self):
        Window.clearcolor = (.11,.14,.24,1) if Window.clearcolor[0] < .1 else (.045,.055,.12,1)
if __name__ == '__main__':
    RezaPlus().run()
