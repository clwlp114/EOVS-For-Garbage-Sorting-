class Recorder:
    Number = 0  # 序号
    NumOfYouHai = 0  # 有害垃圾的数量
    NumOfKeHuiShou = 0  # 可回收垃圾的数量
    NumOfChuYu = 0  # 厨余垃圾的数量
    NumOfQiTa = 0  # 其他垃圾的数量

    YouHaiState = 0
    KeHuiShouState = 0
    ChuYuState = 0
    QiTaState = 0


    def __init__(self):
        self.Number = 0
        self.NumOfYouHai = 0
        self.NumOfKeHuiShou = 0
        self.NumOfChuYu = 0
        self.NumOfQiTa = 0
    # 一次设置各垃圾数量
    def setNum(self,a,b,c,d):
        self.NumOfYouHai = a
        self.NumOfKeHuiShou = b
        self.NumOfChuYu = c
        self.NumOfQiTa = d

    #设置垃圾总数量
    def setSum(self,a):
        self.Number = a

    #设置各种类垃圾的数量
    def setYouHaiNum(self,num):
        self.NumOfYouHai = num
    def setChuYuNum(self,num):
        self.NumOfChuYu = num
    def setQiTaNum(self,num):
        self.NumOfQiTa = num
    def setKeHuiShou(self,num):
        self.NumOfKeHuiShou = num


    #获得各种类垃圾的数量
    def getYouHaiNum(self):
        return self.NumOfYouHai
    def getKeHuiShouNum(self):
        return self.NumOfKeHuiShou
    def getChuYuNum(self):
        return self.NumOfChuYu
    def getQiTaNum(self):
        return self.NumOfQiTa

    def getNumOfKind(self,kind):
        if kind == 'YouHai':
            return self.NumOfYouHai
        elif kind == 'KeHuiShou':
            return self.NumOfKeHuiShou
        elif kind == 'ChuYu':
            return self.NumOfChuYu
        elif kind == 'QiTa':
            return self.NumOfQiTa


    #增加各种类垃圾数量 参数为垃圾种类，步长为1
    def addYouHaiNum(self):
        self.NumOfYouHai = self.NumOfYouHai + 1
    def addKeHuiShouNum(self):
        self.NumOfKeHuiShou = self.NumOfKeHuiShou + 1
    def addChuYuNum(self):
        self.NumOfChuYu = self.NumOfChuYu + 1
    def addQiTaNum(self):
        self.NumOfQiTa = self.NumOfQiTa + 1

    def addNumOfKind(self,kind):
        if kind == 'YouHai':
            self.addYouHaiNum()
        elif kind == 'KeHuiShou':
            self.addKeHuiShouNum()
        elif kind == 'ChuYu':
            self.addChuYuNum()
        elif kind == 'QiTa':
            self.addQiTaNum()

    #设置垃圾满载状态
    def SetYouHaiState(self):
        self.YouHaiState = 1
    def SetKeHuiShouState(self):
        self.KeHuiShouState = 1
    def SetChuYuState(self):
        self.ChuYuState = 1
    def SetQiTaState(self):
        self.QiTaState = 1

    #清除垃圾满载状态
    def ClearYouHaiState(self):
        self.YouHaiState = 0
    def ClearKeHuiShouState(self):
        self.KeHuiShouState = 0
    def ClearChuYuState(self):
        self.ChuYuState = 0
    def ClearQiTaState(self):
        self.QiTaState = 0

