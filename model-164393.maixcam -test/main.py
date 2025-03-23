# main.py
from Checker_ import Checker
from Printer_ import Printer
from RandW_ import RandWder
from Recorder_ import Recorder
from Display_ import Display
import time


class GarbageSortingSystem:
    def __init__(self):
        self.checker = Checker()
        self.printer = Printer()
        self.comm = RandWder()
        self.recorder = Recorder()
        self.display = Display()
        # 初始化硬件
        self._initialize_system()

    def _initialize_system(self):
        """系统初始化操作"""
        self.printer.PrinterStart()
        self.printer.PrintData(0, "", 0)  # 清空初始显示
        print("System Initialization Completed")

    def _handle_full_status(self, kind):
        """处理垃圾满载状态"""
        if kind == "YouHai":
            self.recorder.SetYouHaiState()
            self.printer.PrintYouHaiState(1)
        elif kind == "KeHuiShou":
            self.recorder.SetKeHuiShouState()
            self.printer.PrintKeHuiShouState(1)
        elif kind == "ChuYu":
            self.recorder.SetChuYuState()
            self.printer.PrintChuYuState(1)
        elif kind == "QiTa":
            self.recorder.SetQiTaState()
            self.printer.PrintQiTaState(1)

    def _update_display(self, kind):
        """更新所有显示信息"""
        current_num = self.recorder.getNumber() + 1
        self.recorder.setNumber(current_num)
        self.recorder.addNumOfKind(kind)

        # 更新主界面
        self.printer.PrintData(
            current_num,
            kind,
            self.recorder.getNumOfKind(kind)
        )

        # 更新分类统计
        self.printer.PrintNumOfYouHai(self.recorder.NumOfYouHai)
        self.printer.PrintNumOfKeHuiShou(self.recorder.NumOfKeHuiShou)
        self.printer.PrintNumOfChuYu(self.recorder.NumOfChuYu)
        self.printer.PrintNumOfQiTa(self.recorder.NumOfQiTa)

    def run(self):
        """主运行循环"""
        
        while True:
            # 读取下位机状态
            state = self.comm.ReadState()
            
            if state == "Start":
                
                # 执行物体识别
                kind = self.checker.GetKind()
                #kind = "YouHai"
                if kind and kind != "Error":
                    # 通信协议处理
                    self.comm.SendKind(kind)

                    # 数据记录与显示
                    self._update_display(kind)

                    # 成功反馈
                    self.printer.PrintIsSuccess(1)
                else:
                    self.printer.PrintIsSuccess(0)

            elif state == "Max":
                
                # 获取当前满载的垃圾种类
                full_kind = "KeHuiShou"
                self._handle_full_status(full_kind)

            elif state == "End":
                
                # 复位显示
                self.printer.PrintIsSuccess(0)
                self.printer.PrintKindOfRubissh("", 0)

            #time.sleep(0.1)  # CPU节流


if __name__ == "__main__":
    system = GarbageSortingSystem()
    system.run()