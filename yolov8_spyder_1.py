from ultralytics import YOLO

model = YOLO("yolov8x.pt")
        
if __name__ == '__main__':
    results = model.train(data=r'C:\Users\machi\tabata_ml\Data\yolov8_prac2\train_data\train\kaku_v8.yaml', epochs=30, batch=8, workers=32, degrees=0)
        
        
model = YOLO(r"C:\Users\machi\tabata_ml\Data\yolov8_prac2\best_data\best.pt")
 
if __name__ == '__main__':
    results = model.predict(r"C:\Users\machi\tabata_ml\Data\yolov8_prac2\test_data", save=True, line_width=1, show_labels=False, iou=0.25)
        