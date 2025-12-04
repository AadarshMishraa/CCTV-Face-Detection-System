import cv2
import numpy as np
import os
import face_recognition

class FaceDetector:
    def __init__(self):
        self.target_face = None
        self.target_encoding = None
        self.target_image_path = None
    
    def load_target_face(self, image_path):
        """Load and encode the target person's face using deep learning"""
        try:
            # Load image using OpenCV first to handle various formats
            img_cv = cv2.imread(image_path)
            if img_cv is None:
                raise ValueError("Could not load image file")
            
            # Convert BGR to RGB for face_recognition
            image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            
            # Find all face locations and encodings
            face_locations = face_recognition.face_locations(image, model="hog")
            
            if len(face_locations) == 0:
                # Try with CNN model if HOG fails
                print("HOG detection failed, trying CNN model...")
                face_locations = face_recognition.face_locations(image, model="cnn")
            
            if len(face_locations) == 0:
                raise ValueError("No face found in the uploaded image. Please use a clearer, front-facing photo with good lighting.")
            
            # Get face encodings
            face_encodings = face_recognition.face_encodings(image, face_locations)
            
            if len(face_encodings) == 0:
                raise ValueError("Could not encode the face. Please try a different photo.")
            
            # Use the first (or largest) face found
            self.target_encoding = face_encodings[0]
            self.target_face = image
            self.target_image_path = image_path
            
            print(f"Successfully loaded target face from {image_path}")
            print(f"Found {len(face_locations)} face(s) in the image")
            
            return True
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Error loading face: {str(e)}")
    
    def process_video(self, video_path, output_dir, tolerance=0.5):
        """Process video and detect target face using deep learning face recognition"""
        video = cv2.VideoCapture(video_path)
        fps = video.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            fps = 30  # Default if fps cannot be determined
        
        frame_count = 0
        detections = []
        
        # Process every 30th frame for speed (can adjust for accuracy vs speed)
        frame_skip = 30
        
        print(f"Processing video: {video_path}")
        print(f"FPS: {fps}, Processing every {frame_skip} frames")
        
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            
            frame_count += 1
            
            if frame_count % frame_skip != 0:
                continue
            
            # Convert BGR to RGB (face_recognition uses RGB)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Find all face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame, model="hog")
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            
            # Check each face found in the frame
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Compare face with target face
                matches = face_recognition.compare_faces([self.target_encoding], face_encoding, tolerance=tolerance)
                face_distance = face_recognition.face_distance([self.target_encoding], face_encoding)[0]
                
                # Calculate similarity percentage (inverse of distance)
                similarity = 1 - face_distance
                
                if matches[0]:  # If it's a match
                    timestamp = frame_count / fps
                    
                    print(f"Match found at frame {frame_count}, timestamp {timestamp:.2f}s, similarity: {similarity:.2f}")
                    
                    # Draw rectangle on the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    
                    # Draw label with similarity score
                    label = f"MATCH {similarity*100:.1f}%"
                    cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, label, (left + 6, bottom - 6),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                    
                    # Save frame with detection
                    filename = f"detection_{frame_count}_{timestamp:.2f}s.jpg"
                    output_path = os.path.join(output_dir, filename)
                    cv2.imwrite(output_path, frame)
                    
                    detections.append({
                        'frame': frame_count,
                        'timestamp': timestamp,
                        'image': filename,
                        'similarity': float(similarity),
                        'distance': float(face_distance),
                        'location': {'top': int(top), 'right': int(right), 'bottom': int(bottom), 'left': int(left)}
                    })
        
        video.release()
        print(f"Processing complete. Found {len(detections)} matches.")
        return detections
