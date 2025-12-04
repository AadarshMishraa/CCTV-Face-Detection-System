# ⚡ Quick Start Guide

Get up and running with the Facial Recognition System in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Git installed
- 5 minutes of your time

## Installation (3 steps)

### 1. Clone and Navigate
```bash
git clone https://github.com/yourusername/facial-recognition-system.git
cd facial-recognition-system
```

### 2. Install Dependencies
```bash
cd backend
pip3 install -r requirements.txt
```

**Note**: This may take 2-3 minutes as it installs OpenCV, dlib, and face_recognition.

### 3. Start the Application
```bash
# Terminal 1: Start backend
cd backend
python3 app.py

# Terminal 2: Start frontend (in a new terminal)
cd frontend
python3 server.py
```

## Usage (3 steps)

### 1. Open Browser
Navigate to: `http://localhost:8000`

### 2. Upload Target Photo
- Click "Choose File" under "Upload Target Photo"
- Select a clear, front-facing photo
- Click "Upload Photo"

### 3. Upload & Process Video
- Click "Choose File" under "Upload CCTV Video"
- Select a video file (MP4, AVI, MOV)
- Click "Upload Video"
- Click "Start Detection"
- Wait for results!

## Example Test

Want to test with sample data?

1. Place a test photo in `uploads/` folder
2. Place a test video in `videos/` folder
3. Follow the usage steps above

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5001
lsof -ti:5001 | xargs kill -9

# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Installation Errors
```bash
# On macOS, install cmake first
brew install cmake

# On Ubuntu/Debian
sudo apt-get install cmake

# Then retry
pip3 install -r requirements.txt
```

### Face Not Detected
- Use a clear, front-facing photo
- Ensure good lighting
- Try a different photo
- Check backend logs for errors

## Next Steps

- Read the full [README.md](README.md) for detailed information
- Check [DEPLOYMENT.md](DEPLOYMENT.md) to deploy to production
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Need Help?

- [Open an issue](https://github.com/yourusername/facial-recognition-system/issues)
- Check existing issues for solutions
- Read the full documentation

---

**That's it! You're now running a facial recognition system! 🎉**
