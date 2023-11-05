import cv2
import os

image_dir = "/home/cvpr2023/LuuTru/dataset/COCO2YOLO/MS-COCO/images/" #replace path images dir

labels_dir = "/home/cvpr2023/LuuTru/dataset/COCO2YOLO/MS-COCO/labels_yolo/" #repalce path labels dir (YOLO)

output_dir = "/home/cvpr2023/LuuTru/dataset/COCO2YOLO/MS-COCO/visualize_results/" #repalce path images result

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

categories = {
    0: {"name": "pedestrian", "color": (255, 0, 0)},
    1: {"name": "motor", "color": (0, 255, 0)},
    2: {"name": "car", "color": (0, 0, 255)},
    3: {"name": "bus", "color": (255, 255, 0)}
}

for filename in os.listdir(labels_dir):
    if filename.endswith(".txt"):
        image_filename = os.path.splitext(filename)[0] + '.jpg'
        image_path = os.path.join(image_dir, image_filename)

        image = cv2.imread(image_path)

        with open(os.path.join(labels_dir, filename), 'r') as yolo_file:
            lines = yolo_file.readlines()

        for line in lines:
            values = line.split()
            category_id, x_center, y_center, width, height = map(float, values)

            x = int((x_center - width / 2) * image.shape[1])
            y = int((y_center - height / 2) * image.shape[0])
            w = int(width * image.shape[1])
            h = int(height * image.shape[0])

            class_info = categories.get(int(category_id), {"name": "Unknown", "color": (0, 0, 0)})
            class_name = class_info["name"]
            color = class_info["color"]

            thickness = 2
            image = cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

            text = f"{class_name}"
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        output_filename = os.path.splitext(filename)[0] + '.jpg'
        output_path = os.path.join(output_dir, output_filename)
        cv2.imwrite(output_path, image)
