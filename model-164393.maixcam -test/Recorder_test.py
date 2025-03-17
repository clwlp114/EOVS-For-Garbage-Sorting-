from Recorder_ import Recorder
import time
recorder = Recorder()
recorder.setNum(1,2,3,4)
print(recorder.getYouHaiNum())
print(recorder.getKeHuiShouNum())
print(recorder.getChuYuNum())
print(recorder.getQiTaNum())
time.sleep(2)

recorder.setNumber(5)
print(recorder.getNumber())

recorder.addYouHaiNum()
recorder.addKeHuiShouNum()
recorder.addChuYuNum()
recorder.addQiTaNum()

print(recorder.getYouHaiNum())
print(recorder.getKeHuiShouNum())
print(recorder.getChuYuNum())
print(recorder.getQiTaNum())


recorder.SetYouHaiState()
print(recorder.getYouHaiState())
recorder.ClearYouHaiState()
print(recorder.getYouHaiState())

