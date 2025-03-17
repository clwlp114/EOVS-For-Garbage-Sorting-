from maix import camera, display,image,nn

class Display:



    def show(self):
        detector = nn.YOLOv8(model="/root/models/maixhub/gxsljt_swj/yolov8_1_int8.mud")
        cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
        dis = display.Display()
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
        dis.show(img)  # 显示图像