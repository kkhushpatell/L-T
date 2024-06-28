from flask import Flask, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)

def verify(p1, p2):
    img1 = cv2.imread(p1)
    img2 = cv2.imread(p2)
    
    result = DeepFace.verify(p1, p2)
    
    return result

@app.route('/verify', methods=['POST'])
def verify_api():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'error': 'Please provide both image1 and image2'}), 400
    
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    img1_path = 'image1.jpg'
    img2_path = 'image2.jpg'
    image1.save(img1_path)
    image2.save(img2_path)
    
    try:
        result = verify(img1_path, img2_path)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)