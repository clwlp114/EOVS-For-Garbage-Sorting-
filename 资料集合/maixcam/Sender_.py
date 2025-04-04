from maix import uart

class Sender:
    frame_header = 0xAA  # 帧头
    frame_footer = 0xFF  # 帧尾
    frame_data = 0x66
    # --------------下位机控制信号配置------------#
    device0 = "/dev/ttyS0"
    serial = uart.UART(device0, 115200)
    serial.write_str("hello world")
    print("received:", serial.read(timeout=2000))


    def CreateFrameData(self,kind):
        if kind == "YouHai":
            temp = 0
            frame_data = temp.to_bytes(1, byteorder='big')
        elif kind == "KeHuiShou":
            temp = 1
            frame_data = temp.to_bytes(1, byteorder='big')
        elif kind == "ChuYu":
            temp = 2
            frame_data = temp.to_bytes(1, byteorder='big')
        elif kind == "QiTa":
            temp = 3
            frame_data = temp.to_bytes(1, byteorder='big')
        return frame_data

    def SendKind(self,kind):
        frame_data = self.CreateFrameData(kind)
        self.serial.write(
            self.frame_header.to_bytes(1, byteorder='big') +
            frame_data +
            self.frame_footer.to_bytes(1, byteorder='big')
        )


