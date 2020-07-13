from mycroft import MycroftSkill, intent_file_handler


class PatrickLightsOn(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('on.lights.patrick.intent')
    def handle_on_lights_patrick(self, message):
        self.speak_dialog('on.lights.patrick')


def create_skill():
    return PatrickLightsOn()

