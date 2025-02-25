from maix import camera, display,image, nn,app

class Checker:

    def GetObjId(self):

        detector = nn.YOLOv5(model="/root/models/maixhub/164393/model_164393.mud")
        cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
        dis = display.Display()


        # 初始化变量
        last_label = None
        last_index = None
        count = 0
        MAX_COUNT = 20  # 设置连续相同分类结果的次数阈值
        class_id = 0  # 确定识别种类的编号
        frame_header = 0xAA  # 帧头
        frame_footer = 0xFF

        while  not app.need_exit():
            img = cam.read()
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
                    return  obj.class_id

    def GetKind(self):
        id = Checker.GetObjId();
        if id in (2, 6, 7):
            kind = "YouHai"
        elif id in (0, 3):
            kind = "KeHuiShou"
        elif id in (5, 4):
            kind = "ChuYu"
        elif id in (1):
            kind = "QiTa"
        return kind