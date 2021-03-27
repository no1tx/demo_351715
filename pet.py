class Pet(object):
    def __init__(self, type, legs):
        self.type = type
        self.legs = legs

    def pogladit(self):
        if self.type == 'cat':
            return 'murrr'
        elif self.type == 'dinosaur':
            return 'arrrr'
        else:
            return 'What?'