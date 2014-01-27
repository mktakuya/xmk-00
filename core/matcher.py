import re
import settings

class Matcher:
    def __init__(self, text):
        self.pattern = re.compile(settings.KEY_WORDS)
        self.text = text

    def is_match_me(self):
        if re.search(self.pattern, self.text):
            if settings.DEBUG is True: print u'match me!'
            return True
        return False

