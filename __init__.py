from mycroft import MycroftSkill, intent_file_handler


class BardFallback(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fallback.bard.intent')
    def handle_fallback_bard(self, message):
        self.speak_dialog('fallback.bard')


def create_skill():
    return BardFallback()

