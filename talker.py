# Simple class
class Talker(object):
    def __init__(self):
        self.msg = ""

    def speak(self, phrase, loudly=False):

        if loudly:
            # Speaking loudly
            self.msg = phrase.upper()
        else:
            self.msg = phrase
        print(self.msg)
