import sys

class ProgressBar:

    def __init__(self, length):
        self.length = length
        sys.stdout.write('[%s]' % (' '  * length))
        sys.stdout.flush()
        sys.stdout.write('\b' * (length + 1))

    def advance(self):
        sys.stdout.write('-')
        sys.stdout.flush()

    def finish(self):
        sys.stdout.write('\n')
