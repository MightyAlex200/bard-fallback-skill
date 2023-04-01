from mycroft import FallbackSkill
import Bard


class BardFallback(FallbackSkill):
    """
    Calls to google bard for a response when mycroft cannot fulfill the request.
    """

    def __init__(self):
        super(BardFallback, self).__init__(name="Bard Fallback")

    def initialize(self):
        key = self.settings.get('bard-cookie')
        if key is None or key == '':
            self.speak("You need to set up your bard cookie")
            return
        self.chatbot = Bard.Chatbot(key)
        self.register_fallback(self.handle_fallback, 99)

    def handle_fallback(self, message):
        utterance = message.data.get('utterance')
        res = self.chatbot.ask(utterance)
        if res.get("content"):
            self.speak(res.get("content"))
        else:
            return False
        return True

    def shutdown(self):
        self.remove_fallback(self.handle_fallback)
        super(BardFallback, self).shutdown()


def create_skill():
    return BardFallback()
