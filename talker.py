# Simple class
class Talker(object):
    def __init__(self):
        self.msg = ""

    def speak(self, phrase, loudly=False):

        if loudly:
            # Speaking loudly
            self.yell(phrase)
        else:
            self.msg = phrase
            print(self.msg)

    def yell(self, phrase):
        print(phrase.upper())
