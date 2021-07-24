from kivy.uix.screenmanager import Screen, ScreenManager
from data import log
from widgets import ConnectionPopup
from kivy.clock import Clock


class Manager(ScreenManager):
    pass


class HomeScreen(Screen):

    def on_enter(self, *args):
        popup = ConnectionPopup()
        if not popup.connection():
            Clock.schedule_once(lambda dt: popup.open())


class CCCScreen(Screen):
    question_number = -1

    @log.TimeStamp('ccc-task-started')
    def on_enter(self, *args):
        for response_field in self.ids['response_fields'].children:
            response_field.ids['expression_writer'].draw()
        self.ids['_navigation'].update_question()


class CompletionScreen(Screen):

    def on_pre_enter(self, *args):
        score = self.manager.get_screen('ccc_screen').ids['_navigation'].score
        self.ids['score'].text = str(score)


class TutorialScreen(Screen):

    def on_enter(self, *args):
        for i, response_field in enumerate(self.ids['response_fields'].children):
            response_field.ids['expression_writer'].draw()
            response_field.reset_field()
            if i < 3:
                response_field.switch_mode()
        self.ids['_navigation'].ids['compare'].disabled = True
