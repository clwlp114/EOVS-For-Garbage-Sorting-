from Printer_ import Printer
import time

printer = Printer()

printer.PrinterStart()
time.sleep(1)
printer.PrintNumber(1)
time.sleep(1)
printer.PrintIsSuccess(1)
time.sleep(1)
printer.PrintIsSuccess(0)
time.sleep(1)
printer.PrintNumOfYouHai(1)
time.sleep(1)
printer.PrintNumOfKeHuiShou(2)
time.sleep(1)
printer.PrintNumOfChuYu(3)
time.sleep(1)
printer.PrintNumOfQiTa(4)
time.sleep(1)
printer.PrintYouHaiState(1)
printer.PrintKeHuiShouState(1)
printer.PrintChuYuState(1)
printer.PrintQiTaState(1)
time.sleep(1)
printer.PrintYouHaiState(0)
printer.PrintKeHuiShouState(0)
printer.PrintChuYuState(0)
printer.PrintQiTaState(0)
time.sleep(1)
printer.PrintKindOfRubissh("YouHai",1)
time.sleep(1)
printer.PrintKindOfRubissh("KeHuiShou",2)
time.sleep(1)
printer.PrintKindOfRubissh("ChuYu",3)
time.sleep(1)
printer.PrintKindOfRubissh("QiTa",4)
time.sleep(1)

printer.PrinterStart()
time.sleep(1)
printer.PrintData(40,"YouHai",1)
time.sleep(1)
printer.PrintData(41,"KeHuiShou",2)
time.sleep(1)
printer.PrintData(42,"ChuYu",3)
time.sleep(1)
printer.PrintData(43,"QiTa",4)
time.sleep(1)
