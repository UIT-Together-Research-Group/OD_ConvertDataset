import json
import os

labels_dir = "/home/cvpr2023/LuuTru/dataset/COCO2YOLO/MS-COCO/labels" #repalce path labels dir (YOLO)

if not os.path.exists(labels_dir):
    os.makedirs(labels_dir)
    
with open("/home/cvpr2023/LuuTru/dataset/COCO2YOLO/MS-COCO/labels.json", 'r') as json_file: #repalce path labels.json (COCO)
    data = json.load(json_file)

for image in data['images']:
    image_id = image['id']
    image_file_name = image['file_name']
    image_width = image['width']
    image_height = image['height']

    yolo_file_name = os.path.splitext(image_file_name)[0] + '.txt'
    with open(os.path.join(labels_dir, yolo_file_name), 'w') as yolo_file:

        for annotation in data['annotations']:
            if annotation['image_id'] == image_id:
                category_id = annotation['category_id']
                bbox = annotation['bbox']

                x_center = (bbox[0] + bbox[2] / 2) / image_width
                y_center = (bbox[1] + bbox[3] / 2) / image_height
                width = bbox[2] / image_width
                height = bbox[3] / image_height

                yolo_file.write(f"{category_id} {x_center} {y_center} {width} {height}\n")