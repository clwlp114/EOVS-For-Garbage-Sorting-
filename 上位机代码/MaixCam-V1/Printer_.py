from maix import uart, pinmap



class Printer:
    print(pinmap.get_pins())

    f1 = pinmap.get_pin_functions("A18")
    f2 = pinmap.get_pin_functions("A19")

    print(f"GPIO A18 pin functions:{f1}")
    print(f"GPIO A19 pin functions:{f2}")

    pinmap.set_pin_function("A18", f1[2])
    pinmap.set_pin_function("A19", f2[2])

    device1 = "/dev/ttyS1"

    ser = uart.UART(device1, 9600)
    # ----------定义输出函数------------#
    # 串口屏初始化显示函数（无参数）
    def PrinterStart(self):
        ser.write(b't3.txt=\"0\"')  # 屏幕组件控制指令 序号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't5.txt=\"\"')  # 屏幕组件控制指令  垃圾种类

        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't7.txt=\"0\"')  # 屏幕组件控制指令  数量
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't9.txt=\"\"')  # 屏幕组件控制指令  分类是否成功
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't11.txt=\"0\"')  # 屏幕组件控制指令   有害垃圾件数

        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't16.txt=\"0\"')  # 屏幕组件控制指令    可回收垃圾件数
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't20.txt=\"0\"')  # 屏幕组件控制指令    厨余垃圾件数
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b't24.txt=\"0\"')  # 屏幕组件控制指令    其他垃圾件数
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b'click b1,0')  # 屏幕组件控制指令    有害垃圾满载检测
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b'click b2,0')  # 屏幕组件控制指令    可回收垃圾满载检测
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b'click b3,0')  # 屏幕组件控制指令    厨余垃圾满载检测
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

        ser.write(b'click b4,0')  # 屏幕组件控制指令    其他垃圾满载检测
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号


    # 输出序号 使用Recorder的
    def PrintNumber(Number):
        ser.write(b't3.txt=')  # 屏幕组件控制指令  数量
        ser.write(b'\"%d\"' % Number)  # 数量   i自加
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号


    # 输出分类是否成功（参数：是否成功boolean）
    def PrintIsSuccess(boolean):
        if (boolean == 1):
            ser.write(b't9.txt=\"OK\"')
        else:
            ser.write(b't9.txt=\"NO\"')  # 屏幕组件控制指令  分类是否成功

        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号


    #必要  输出垃圾数量（参数：某种的数量）
    def PrintNumOfYouHai(NumOfYouHai):
        ser.write(b't11.txt=')
        ser.write(b'\"%d\"' % NumOfYouHai)
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
    def PrintNumOfKeHuiShou(NumOfKeHuiShou):
        ser.write(b't16.txt=')  # 屏幕组件控制指令  数量
        ser.write(b'\"%d\"' % NumOfKeHuiShou)
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
    def PrintNumOfChuYu(NumOfChuYu):
        ser.write(b't20.txt=')
        ser.write(b'\"%d\"' % NumOfChuYu)
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
    def PrintNumOfQiTa(NumOfQiTa):
        ser.write(b't24.txt=')
        ser.write(b'\"%d\"' % NumOfQiTa)
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号

    #输出满载信息
    def PrintYouHaiState(IsFull):
        if (IsFull == 1):
            ser.write(b'click b1,1')  # 屏幕组件控制指令    有害垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号

        else:
            ser.write(b'click b1,0')  # 屏幕组件控制指令    有害垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
    def PrintKeHuiShouState(IsFull):
        if (IsFull == 1):
            ser.write(b'click b2,1')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        else:
            ser.write(b'click b2,0')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  #
    def PrintChuYuState(IsFull):
        if (IsFull == 1):
            ser.write(b'click b3,1')  # 屏幕组件控制指令    厨余垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        else:
            ser.write(b'click b3,0')  # 屏幕组件控制指令    厨余垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  #
    def PrintQiTaState(IsFull):
        if (IsFull == 1):
            ser.write(b'click b4,1')  # 屏幕组件控制指令    其他垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        else:
            ser.write(b'click b4,0')  # 屏幕组件控制指令    其他垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')


    # 输出某种垃圾数量（参数：种类，数量）
    def PrintKindOfRubissh(kind,Num):
        ser.write(b't5.txt=')  # 屏幕组件控制指令  垃圾种类
        if (kind =="YouHai"):
            ser.write(b'\"\xd3\xd0\xba\xa6\xc0\xac\xbb\xf8\"')  # 有害垃圾
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b't7.txt=')
            ser.write(b'\"%d\"' % Num)
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        elif (kind =="KeHuiShou"):
            ser.write(b'\"\xbf\xc9\xbb\xd8\xca\xd5\"')  # 可回收垃圾
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b't7.txt=')
            ser.write(b'\"%d\"' % Num)
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        elif (kind =="ChuYu"):
            ser.write(b'\"\xb3\xf8\xd3\xe0\xc0\xac\xbb\xf8\"')  # 厨余垃圾
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b't7.txt=')
            ser.write(b'\"%d\"' % Num)
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        elif (kind =="QiTa"):
            ser.write(b'\"\xc6\xe4\xcb\xfb\xc0\xac\xbb\xf8\"')  # 其他垃圾
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b't7.txt=')
            ser.write(b'\"%d\"' % Num)
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号


    # 满载检测（参数：种类，是否满）
    def IsFull(kind, IsFull):
        if (kind == "YouHai"):
            if (IsFull == 1):
                ser.write(b'click b1,1')  # 屏幕组件控制指令    有害垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号

            else:
                ser.write(b'click b1,0')  # 屏幕组件控制指令    有害垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号


        elif (kind == "KeHuiShou"):
            if (IsFull == 1):
                ser.write(b'click b2,1')  # 屏幕组件控制指令    可回收垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
            else:
                ser.write(b'click b2,0')  # 屏幕组件控制指令    可回收垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  #

        elif (kind == "ChuYu"):
            if (IsFull == 1):
                ser.write(b'click b3,1')  # 屏幕组件控制指令    厨余垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
            else:
                ser.write(b'click b3,0')  # 屏幕组件控制指令    厨余垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  #
        elif (kind == "QiTa"):
            if (IsFull == 1):
                ser.write(b'click b4,1')  # 屏幕组件控制指令    其他垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
            else:
                ser.write(b'click b4,0')  # 屏幕组件控制指令    其他垃圾满载检测
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  # 结束符号
                ser.write(b'\xff')  #


    # 显示函数（参数：序号Number,种类kind）
    def PrintData(Number, kind,Num):

        PrintNumber(Number)
        PrintKindOfRubissh(kind)
        if (kind == "YouHai"):
            PrintNumOfYouHai(Num)
        elif (kind == "KeHuiShou"):
            PrintNumOfKeHuiShou(Num)
        elif (kind == "ChuYu"):
            PrintNumOfChuYu(Num)
        elif (kind == "QiTa"):
            PrintNumOfQiTa(Num)





