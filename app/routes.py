from flask import Blueprint, render_template, request, jsonify
from app.models import analyze_data, generate_graph
from app.utils import allowed_file

import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if file and allowed_file(file.filename):
            filename = os.path.join('uploads', file.filename)
            file.save(filename)
            question = request.form.get('question', '')
            analysis = analyze_data(filename, question)
            graph = generate_graph(filename)

            return render_template('result.html', analysis=analysis, graph=graph)
        
    return render_template('index.html')