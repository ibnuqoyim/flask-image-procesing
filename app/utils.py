import os
from PIL import Image
import cv2

def convert_to_grayscale(image_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_path = 'instance/uploads/gray_' + os.path.basename(image_path)
    cv2.imwrite(output_path, gray_img)
    return output_path

def resize_image(image_path, width, height):
    img = cv2.imread(image_path)
    resized_img = cv2.resize(img, (width, height))
    output_path = 'instance/uploads/resized_' + os.path.basename(image_path)
    cv2.imwrite(output_path, resized_img)
    return output_path

def rotate_image(image_path, angle):
    img = cv2.imread(image_path)
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, M, (w, h))
    output_path = 'instance/uploads/rotated_' + os.path.basename(image_path)
    cv2.imwrite(output_path, rotated_img)
    return output_path

def edge_detection(image_path, lower_threshold, upper_threshold):
    img = cv2.imread(image_path)
    edges = cv2.Canny(img, lower_threshold, upper_threshold)
    output_path = 'instance/uploads/edges_' + os.path.basename(image_path)
    cv2.imwrite(output_path, edges)
    return output_path

def blur_image(image_path, ksize):
    img = cv2.imread(image_path)
    blurred_img = cv2.GaussianBlur(img, (ksize, ksize), 0)
    output_path = 'instance/uploads/blurred_' + os.path.basename(image_path)
    cv2.imwrite(output_path, blurred_img)
    return output_path

def adjust_brightness_contrast(image_path, alpha, beta):
    img = cv2.imread(image_path)
    adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    output_path = 'instance/uploads/adjusted_' + os.path.basename(image_path)
    cv2.imwrite(output_path, adjusted_img)
    return output_path