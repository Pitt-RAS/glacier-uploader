import sys

class ProgressBar:
    """A simple progress bar on command line
    reference: http://stackoverflow.com/questions/3160699/python-progress-bar
    """

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
