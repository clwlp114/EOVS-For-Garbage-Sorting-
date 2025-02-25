from Recorder_ import Recorder
from Printer_ import Printer

recorder = Recorder()
printer = Printer()

recorder.setNum(1,2,3,0)
print(recorder.getYouHaiNum())
printer.printNumOfKind("YouHai",recorder.getYouHaiNum())


