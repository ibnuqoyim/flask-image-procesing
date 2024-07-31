import os
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from .utils import process_image

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

@bp.route('/process/<filename>')
def process_image_route(filename):
    output_filename = process_image(filename)
    return send_from_directory('instance/uploads', output_filename)