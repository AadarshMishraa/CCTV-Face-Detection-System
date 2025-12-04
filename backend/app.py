from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from face_detector import FaceDetector
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuration
UPLOAD_FOLDER = '../uploads'
VIDEO_FOLDER = '../videos'
RESULTS_FOLDER = '../results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov'}

# Create directories
for folder in [UPLOAD_FOLDER, VIDEO_FOLDER, RESULTS_FOLDER]:
    os.makedirs(folder, exist_ok=True)

detector = FaceDetector()

def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

@app.route('/api/upload-target', methods=['POST'])
def upload_target():
    """Upload target person's photo"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        try:
            detector.load_target_face(filepath)
            return jsonify({'success': True, 'message': 'Target face loaded successfully'})
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/upload-video', methods=['POST'])
def upload_video():
    """Upload CCTV video"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename, ALLOWED_VIDEO_EXTENSIONS):
        filename = secure_filename(file.filename)
        filepath = os.path.join(VIDEO_FOLDER, filename)
        file.save(filepath)
        return jsonify({'success': True, 'filename': filename})
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/detect', methods=['POST'])
def detect():
    """Run detection on uploaded video"""
    data = request.json
    video_filename = data.get('video_filename')
    
    if not video_filename:
        return jsonify({'error': 'No video specified'}), 400
    
    if detector.target_face is None:
        return jsonify({'error': 'Please upload target photo first'}), 400
    
    video_path = os.path.join(VIDEO_FOLDER, video_filename)
    if not os.path.exists(video_path):
        return jsonify({'error': 'Video not found'}), 404
    
    try:
        detections = detector.process_video(video_path, RESULTS_FOLDER)
        return jsonify({
            'success': True,
            'detections': detections,
            'count': len(detections)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/results/<filename>')
def get_result(filename):
    """Serve detection result images"""
    return send_from_directory(RESULTS_FOLDER, filename)

@app.route('/api/videos')
def list_videos():
    """List available videos"""
    videos = [f for f in os.listdir(VIDEO_FOLDER) 
              if allowed_file(f, ALLOWED_VIDEO_EXTENSIONS)]
    return jsonify({'videos': videos})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug, port=port, host='0.0.0.0')
