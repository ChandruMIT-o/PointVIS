from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import random

ROOT = r"D:\Iesa\MIT\Sem 4\AI Project\project"
IMAGE_PATH = ""
TEXT_FILE_PATH = ""
OUTPUT_PATH = ""

IMAGE_WIDTH = -1
IMAGE_HEIGHT = -1

model = YOLO("yolov8n-seg.pt")
print

def update_path(image_name):
    global IMAGE_PATH, TEXT_FILE_PATH, OUTPUT_PATH
    IMAGE_PATH = ROOT + "\\data\\" + image_name
    TEXT_FILE_PATH = (ROOT + "\\runs\\segment\\predict\\labels\\" + image_name).split(".")[0] + ".txt"
    OUTPUT_PATH = ROOT + "\\output\\" + image_name

def get_image_size(IMAGE_PATH):
    global IMAGE_WIDTH, IMAGE_HEIGHT
    image = Image.open(IMAGE_PATH)
    IMAGE_WIDTH, IMAGE_HEIGHT = image.size
    print(f"Width: {IMAGE_WIDTH}, Height: {IMAGE_HEIGHT}")

def parse_segmentation_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    segmentation_data = []
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        coords = list(map(float, parts[1:]))
        segmentation_data.append((class_id, coords))
    
    return segmentation_data

def normalize_to_pixel(coords, width, height):
    pixel_coords = [(int(x * width), int(y * height)) for x, y in zip(coords[::2], coords[1::2])]
    return pixel_coords

def generate_unique_color(existing_colors):
    while True:
        color = tuple(random.randint(0, 255) for _ in range(3))
        if color not in existing_colors:
            return color

# Draw the segmentation outlines on a blank image
def draw_segmentations(segmentation_data, width, height):
    blank_image = np.zeros((height, width, 3), np.uint8)
    
    # Dictionary to map colors to (ClassID, InstanceID, className)
    color_map = {}
    existing_colors = set()
    
    # object_count_dict = dict()
    # Read lookup table and instantiate a dictionary of having counts of each objectID
    # {objectID:count}

    for class_id, coords in segmentation_data:
        pixel_coords = normalize_to_pixel(coords, width, height)
        pts = np.array(pixel_coords, np.int32)
        pts = pts.reshape((-1, 1, 2))
        
        color = generate_unique_color(existing_colors)
        existing_colors.add(color)
        
        if objectID in object_count_dict:
            color_map[color] = (class_id, object_count_dict[objectID]+1, model.names[class_id])
            object_count_dict[objectID]+=1
        else:
            color_map[color] = (class_id, object_count_dict[objectID]+1, model.names[class_id])
            object_count_dict[objectID]+=1 
        cv2.fillPoly(blank_image, [pts], color=color)

        # WRITE THE NEW OBJECT INTO LOOKUP TABLE AND INTO COMMON FILE STORE

    return blank_image, color_map

# Assuming file is in .\data
update_path("image.png")
model.predict(source = IMAGE_PATH, show=False, save=True, save_txt=True, show_boxes=False)

get_image_size(IMAGE_PATH)

segmentation_data = parse_segmentation_file(TEXT_FILE_PATH)

segmented_image, color_map = draw_segmentations(segmentation_data, IMAGE_WIDTH, IMAGE_HEIGHT)

cv2.imwrite(OUTPUT_PATH, segmented_image)

print(color_map)

