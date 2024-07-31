from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from .utils import convert_to_grayscale, resize_image, rotate_image, edge_detection, blur_image, adjust_brightness_contrast

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('instance/uploads', filename))
        return redirect(url_for('main.show_image', filename=filename))

@bp.route('/uploads/<filename>')
def show_image(filename):
    return render_template('result.html', filename=filename)

@bp.route('/process/grayscale/<filename>')
def process_grayscale(filename):
    output_filename = convert_to_grayscale(os.path.join('instance/uploads', filename))
    return send_from_directory('instance/uploads', os.path.basename(output_filename))

@bp.route('/process/resize/<filename>')
def process_resize(filename):
    output_filename = resize_image(os.path.join('instance/uploads', filename), 200, 200)
    return send_from_directory('instance/uploads', os.path.basename(output_filename))

@bp.route('/process/rotate/<filename>')
def process_rotate(filename):
    output_filename = rotate_image(os.path.join('instance/uploads', filename), 45)
    return send_from_directory('instance/uploads', os.path.basename(output_filename))

@bp.route('/process/edges/<filename>')
def process_edges(filename):
    output_filename = edge_detection(os.path.join('instance/uploads', filename), 100, 200)
    return send_from_directory('instance/uploads', os.path.basename(output_filename))

@bp.route('/process/blur/<filename>')
def process_blur(filename):
    output_filename = blur_image(os.path.join('instance/uploads', filename), 5)
    return send_from_directory('instance/uploads', os.path.basename(output_filename))

@bp.route('/process/adjust/<filename>')
def process_adjust(filename):
    output_filename = adjust_brightness_contrast(os.path.join('instance/uploads', filename), 1.2, 50)
    return send_from_directory('instance/uploads', os.path.basename(output_filename))
