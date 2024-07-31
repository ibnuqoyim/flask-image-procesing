import os
from PIL import Image

def process_image(filename):
    img_path = os.path.join('instance/uploads', filename)
    img = Image.open(img_path)
    img = img.convert('L')
    output_filename = 'processed_' + filename
    img.save(os.path.join('instance/uploads', output_filename))
    return output_filename