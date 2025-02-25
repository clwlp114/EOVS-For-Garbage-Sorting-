from maix import camera, display, image, nn, app, uart, pinmap, time

# --------------下位机控制信号配置------------#
device0 = "/dev/ttyS0"
serial = uart.UART(device0, 115200)
serial.write_str("hello world")
print("received:", serial.read(timeout=2000))

detector = nn.YOLOv8(model="/root/models/maixhub/gxsljt_swj/yolov8_1_int8.mud")
#detector = nn.YOLO11(model="/root/models/maixhub/gxsljt_swj/yolov11_1_int8.mud")
cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
dis = display.Display()

# -------------串口屏信号----------#

print(pinmap.get_pins())

f1 = pinmap.get_pin_functions("A18")
f2 = pinmap.get_pin_functions("A19")

print(f"GPIO A18 pin functions:{f1}")
print(f"GPIO A19 pin functions:{f2}")

pinmap.set_pin_function("A18", f1[2])
pinmap.set_pin_function("A19", f2[2])

device1 = "/dev/ttyS1"

ser = uart.UART(device1, 9600)


# 串口屏显示内容
Number = -1  # 序号
NumOfYouHai = 0  # 有害垃圾的数量
NumOfKeHuiShou = 0  # 可回收垃圾的数量
NumOfChuYu = 0  # 厨余垃圾的数量
NumOfQiTa = 0  # 其他垃圾的数量
print("串口屏初始化结束")

#----------定义输出函数------------#
    #输出序号
def PrintNumber(Number):
    ser.write(b't3.txt=')  #屏幕组件控制指令  数量
    ser.write(b'\"%d\"'%Number) #数量   i自加
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

#输出分类是否成功（参数：是否成功boolean）
def PrintIsSuccess( boolean):
    if(boolean == 1):
        ser.write(b't9.txt=\"OK\"')
    else:
        ser.write(b't9.txt=\"NO\"')  # 屏幕组件控制指令  分类是否成功

    ser.write(b'\xff')  # 结束符号
    ser.write(b'\xff')  # 结束符号
    ser.write(b'\xff')  # 结束符号

#输出垃圾数量（参数：某种的数量）
def PrintNumOfYouHai(NumOfYouHai):
    ser.write(b't11.txt=')
    ser.write(b'\"%d\"'%NumOfYouHai)
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
def PrintNumOfKeHuiShou(NumOfKeHuiShou):
    ser.write(b't16.txt=')  #屏幕组件控制指令  数量
    ser.write(b'\"%d\"'%NumOfKeHuiShou)
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
def PrintNumOfChuYu(NumOfChuYu):
    ser.write(b't20.txt=')
    ser.write(b'\"%d\"'%NumOfChuYu)
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
def PrintNumOfQiTa(NumOfQiTa):
    ser.write(b't24.txt=')
    ser.write(b'\"%d\"'%NumOfQiTa)
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号


#输出垃圾种类（参数：种类，数量）
def PrintKindOfRubissh( kind):
    ser.write(b't5.txt=')  #屏幕组件控制指令  垃圾种类
    if(kind+1 == 1):
        ser.write(b'\"\xd3\xd0\xba\xa6\xc0\xac\xbb\xf8\"') #有害垃圾
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b't7.txt=')
        ser.write(b'\"%d\"'%NumOfYouHai)
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
    elif(kind+1 == 2):
        ser.write(b'\"\xbf\xc9\xbb\xd8\xca\xd5\"')  #可回收垃圾
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b't7.txt=')
        ser.write(b'\"%d\"'%NumOfKeHuiShou)
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
    elif(kind+1 == 3):
        ser.write(b'\"\xb3\xf8\xd3\xe0\xc0\xac\xbb\xf8\"')  #厨余垃圾
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b't7.txt=')
        ser.write(b'\"%d\"'%NumOfChuYu)
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
    elif(kind+1 == 4):
        ser.write(b'\"\xc6\xe4\xcb\xfb\xc0\xac\xbb\xf8\"')  #其他垃圾
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b'\xff')  # 结束符号
        ser.write(b't7.txt=')
        ser.write(b'\"%d\"'%NumOfQiTa)
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号
        ser.write(b'\xff')  #结束符号


#满载检测（参数：种类，是否满）
def IsFull(kind,IsFull):
    if(kind+1 == 1):
        if(IsFull == 1):
            ser.write(b'click b1,1')  # 屏幕组件控制指令    有害垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号

        else:
            ser.write(b'click b1,0')  # 屏幕组件控制指令    有害垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号


    elif(kind+1 == 2):
        if(IsFull == 1):
            ser.write(b'click b2,1')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        else:
            ser.write(b'click b2,0')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  #

    elif(kind+1 == 3):
        if (IsFull == 1):
            ser.write(b'click b3,1')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        else:
            ser.write(b'click b3,0')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  #
    elif(kind+1 == 4):
        if (IsFull == 1):
            ser.write(b'click b4,1')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
        else:
            ser.write(b'click b4,0')  # 屏幕组件控制指令    可回收垃圾满载检测
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  # 结束符号
            ser.write(b'\xff')  #


#显示函数（参数：序号Number,种类kind）
def PrintData(Number,kind):
    print("In PrintData")
    PrintNumber(Number)
    PrintKindOfRubissh(kind)
    if(kind ==0):
        PrintNumOfYouHai(NumOfYouHai)
    elif(kind == 1):
        PrintNumOfKeHuiShou(NumOfKeHuiShou)
    elif(kind == 2):
        PrintNumOfChuYu(NumOfChuYu)
    elif(kind == 3):
        PrintNumOfQiTa(NumOfQiTa)
    print("In PrintData")
#串口屏初始化显示函数（无参数）
def PrinterStart():
    ser.write(b't3.txt=\"0\"')  #屏幕组件控制指令 序号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't5.txt=\"\"')  #屏幕组件控制指令  垃圾种类

    
    
   

    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't7.txt=\"0\"')  #屏幕组件控制指令  数量
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't9.txt=\"\"')  #屏幕组件控制指令  分类是否成功
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't11.txt=\"0\"')  #屏幕组件控制指令   有害垃圾件数
    
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't16.txt=\"0\"')  #屏幕组件控制指令    可回收垃圾件数
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't20.txt=\"0\"')  #屏幕组件控制指令    厨余垃圾件数
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b't24.txt=\"0\"')  #屏幕组件控制指令    其他垃圾件数
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b'click b1,0')  #屏幕组件控制指令    有害垃圾满载检测
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b'click b2,0')  #屏幕组件控制指令    可回收垃圾满载检测
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b'click b3,0')   #屏幕组件控制指令    厨余垃圾满载检测
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号

    ser.write(b'click b4,0')   #屏幕组件控制指令    其他垃圾满载检测
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号
    ser.write(b'\xff')  #结束符号


#last_sent_time = 0  # 记录上次发送时间
send_interval = 1  # 超过1s没有收到信息
acked = False  # 是否已确认接收
# processed = False   # 下位机是否已处理完成 有云台电机后改正
initial_detection = False  # 是否进行了初始检测

# 初始化变量
last_label = None
last_index = None
count = 0
MAX_COUNT = 20  # 设置连续相同分类结果的次数阈值
class_id = 0  # 确定识别种类的编号
frame_header = 0xAA  # 帧头
frame_footer = 0xFF  # 帧尾
# 0 hazadrous
# 1 recycle
# 2 kitchen
# 3 other
Receive = False
kind = 5
PrinterStart()
while not app.need_exit():
    current_time = time.time()  # 获取当前时间
    last_sent_time = time.time()
    # 读取串口数据
    data = serial.read()
    if data:
        print("read data sucsess")
        print(data)
        # 满载检测
        if len(data) == 4 and data[0] == 0xAA and data[-1] == 0xFF:  # 满载处理
            print("In 满载处理")
            if data[1] == 0x00:
                IsFull(0, 1)  # hazadrous full
                print("Hazadrous Full")
            elif data[1] == 0x01:
                IsFull(1, 1)  # recyle full
                print("Recyle Full")
            elif data[1] == 0x02:
                IsFull(2, 1)  # kitchen full
                print("Kitchen Full")
            elif data[1] == 0x03:
                IsFull(3, 1)  # other full
                print("Other Full")
            print("In 满载处理")
        elif len(data) == 3 and data[0] == 0xAA and data[-1] == 0xFF:
            print("In Detection")
            print(data)
            if data[1] == 0x04:
                print("IN 04!!!!!!!!!!!!!!")
                print("In 掉落检测")
                initial_detection = True  # 掉落检测
                Receive = False
                print("Initial detection trigered")
                # print("Starting to read framges.")
            elif data[1] == 0x02:
                print("IN 02!!!!!!!!!!!!!!")
                initial_detection = False  # 确认下位机收到消息，暂停发送
                acked = True
                PrintData(Number,kind)
                PrintIsSuccess(True)
                print("Message acknowledged")
                acked = False
                # 在串口屏程序中，根据b做出相应处理，最后把标志位acked改为false，即可重新进行10次运算
            # elif data[1] == 0x03 and acked:  # 只有在收到0x02之后，0x03才有效
            #     processed = True
            #     print("满载检测")  #云台电机后改正
            print("In Detection")

    img = cam.read()
    # 进行检测的条件：初始检测触发，且未收到确认消息或已处理完成
    if  initial_detection and not acked and not Receive:
        print("in second if")
        objs = detector.detect(img, conf_th=0.5, iou_th=0.45)
        for obj in objs:
            # obj.class_id 标签号
            # detector.labels[obj.class_id] 标签名
            # obj.score 置信度
            img.draw_rect(obj.x, obj.y, obj.w, obj.h, color=image.COLOR_RED)
            msg = f'{detector.labels[obj.class_id]}: {obj.score:.2f}'
            img.draw_string(obj.x, obj.y, msg, color=image.COLOR_RED)
            current_label = detector.labels[obj.class_id]  # 现在的标签
            print(f"Detected: {detector.labels[obj.class_id]} with ID: {obj.class_id}")
            # 检查是否与上一次的分类结果相同
            if current_label == last_label and last_index == obj.class_id:
                count += 1  # 增加计数器
            else:
                count = 0  # 重置计数器
                last_label = current_label  # 更新上一次的分类结果
                last_index = obj.class_id  # 更新上一次的分类结果索引

            if count == MAX_COUNT:
                print(f"连续10次分类结果相同：{msg}, 编号：{obj.class_id}")
                count = 0  # 重置计数器
                last_label = None  # 重置上一次的分类结果
                last_index = None  # 重置上一次的分类结果索引
                print(obj.class_id)
                if obj.class_id in (0,1,2):
                    kind = 0
                elif obj.class_id in (3,4):
                    kind = 1
                elif obj.class_id in (5,6,7):
                    kind = 2
                elif obj.class_id == 8:
                    kind = 3
                frame_data = kind.to_bytes(1, byteorder='big')
                serial.write(frame_header.to_bytes(1, byteorder='big') + frame_data + frame_footer.to_bytes(1, byteorder='big'))
                last_sent_time = time.time()
                Receive = True
                Number += 1
                if kind == 0:
                    NumOfYouHai += 1
                elif kind == 1:
                    NumOfKeHuiShou += 1
                elif kind == 2:
                    NumOfChuYu += 1
                elif kind == 3:
                    NumOfQiTa += 1
                print(Number)
                print(kind)
                print(NumOfYouHai)
                print(NumOfKeHuiShou)
                print(NumOfChuYu)
                print(NumOfQiTa)
                time.sleep(2)
    if not acked and (time.time() - last_sent_time >= send_interval) and Receive :
        serial.write(frame_header.to_bytes(1, byteorder='big') + kind.to_bytes(1, byteorder='big') + frame_footer.to_bytes(1, byteorder='big'))
                                                                                                                 

    dis.show(img)  # 显示图像       
