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
    if state == "Start":
        kind = checker.GetKind()
        randwder.SendKind(kind)
        recorder.addNumOfKind(kind)
    elif state == "End":
        printer.PrintData(kind,recorder.getNumOfKind(kind))
    elif state == "Max":
        printer.PrintKeHuiShouState(1)


