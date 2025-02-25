from Recorder_ import Recorder
from Checker_ import Checker
from Printer_  import Printer
from RandW_ import RandWder

recorder = Recorder()
checker = Checker()
printer = Printer()
randwder = RandWder()
while True:
    state = randwder.ReadState()
    print(state)
