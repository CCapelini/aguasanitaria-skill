from mycroft import MycroftSkill, intent_file_handler


class Aguasanitaria(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('aguasanitaria.intent')
    def handle_aguasanitaria(self, message):
        self.speak_dialog('aguasanitaria')


def create_skill():
    return Aguasanitaria()

