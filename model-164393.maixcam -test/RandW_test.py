from RandW_ import RandWder
import time
 

randwder = RandWder()

while True:
    #------------------测试接受输入------------------#
    
    state = randwder.ReadState()
    if(state == "Start"):
        print(state)
        time.sleep(5)
    elif(state == "End"):
        print(state)
        time.sleep(5)
    elif(state == "Max"):
        print(state)
        time.sleep(5)   
    else:
        print(state)


'''Pass
#--------------------测试输出-------------------#
kind1 = "YouHai"
kind2 = "KeHuiShou"
kind3 = "ChuYu"
kind4 = "QiTa"
kind5 = "qita"
randwder.SendKind(kind1)
randwder.SendKind(kind2)
randwder.SendKind(kind3)
randwder.SendKind(kind4)
randwder.SendKind(kind5)
'''