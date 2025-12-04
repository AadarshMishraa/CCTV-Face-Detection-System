const API_URL = 'http://localhost:5001/api';
let selectedVideo = null;
let targetUploaded = false;

// Upload target photo
async function uploadTarget() {
    const fileInput = document.getElementById('targetPhoto');
    const file = fileInput.files[0];
    
    if (!file) {
        showStatus('targetStatus', 'Please select a photo', 'error');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch(`${API_URL}/upload-target`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            showStatus('targetStatus', '✓ Target photo uploaded successfully!', 'success');
            targetUploaded = true;
            
            // Show preview
            const preview = document.getElementById('targetPreview');
            preview.innerHTML = `<img src="${URL.createObjectURL(file)}" alt="Target">`;
            
            updateDetectButton();
        } else {
            showStatus('targetStatus', `Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showStatus('targetStatus', `Error: ${error.message}`, 'error');
    }
}

// Upload CCTV video
async function uploadVideo() {
    const fileInput = document.getElementById('cctvVideo');
    const file = fileInput.files[0];
    
    if (!file) {
        showStatus('videoStatus', 'Please select a video', 'error');
        return;
    }
    
    showStatus('videoStatus', 'Uploading video...', 'info');
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch(`${API_URL}/upload-video`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            showStatus('videoStatus', '✓ Video uploaded successfully!', 'success');
            selectedVideo = data.filename;
            loadVideos();
            updateDetectButton();
        } else {
            showStatus('videoStatus', `Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showStatus('videoStatus', `Error: ${error.message}`, 'error');
    }
}

// Load available videos
async function loadVideos() {
    try {
        const response = await fetch(`${API_URL}/videos`);
        const data = await response.json();
        
        const videoList = document.getElementById('videoList');
        videoList.innerHTML = '<h3>Available Videos:</h3>';
        
        data.videos.forEach(video => {
            const item = document.createElement('div');
            item.className = 'video-item';
            if (video === selectedVideo) {
                item.classList.add('selected');
            }
            item.textContent = video;
            item.onclick = () => selectVideo(video);
            videoList.appendChild(item);
        });
    } catch (error) {
        console.error('Error loading videos:', error);
    }
}

// Select video
function selectVideo(filename) {
    selectedVideo = filename;
    loadVideos();
    updateDetectButton();
}

// Update detect button state
function updateDetectButton() {
    const btn = document.getElementById('detectBtn');
    btn.disabled = !(targetUploaded && selectedVideo);
}

// Run detection
async function runDetection() {
    if (!targetUploaded || !selectedVideo) {
        showStatus('detectionStatus', 'Please upload both target photo and video', 'error');
        return;
    }
    
    document.getElementById('loading').style.display = 'block';
    document.getElementById('resultsCard').style.display = 'none';
    showStatus('detectionStatus', 'Processing video...', 'info');
    
    try {
        const response = await fetch(`${API_URL}/detect`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ video_filename: selectedVideo })
        });
        
        const data = await response.json();
        
        document.getElementById('loading').style.display = 'none';
        
        if (data.success) {
            showStatus('detectionStatus', `✓ Detection complete! Found ${data.count} matches.`, 'success');
            displayResults(data.detections);
        } else {
            showStatus('detectionStatus', `Error: ${data.error}`, 'error');
        }
    } catch (error) {
        document.getElementById('loading').style.display = 'none';
        showStatus('detectionStatus', `Error: ${error.message}`, 'error');
    }
}

// Display results
function displayResults(detections) {
    const resultsCard = document.getElementById('resultsCard');
    const resultsCount = document.getElementById('resultsCount');
    const resultsGrid = document.getElementById('resultsGrid');
    
    resultsCard.style.display = 'block';
    
    if (detections.length === 0) {
        resultsCount.textContent = 'No matches found';
        resultsGrid.innerHTML = '<p>The target person was not detected in the video.</p>';
        return;
    }
    
    resultsCount.textContent = `Found ${detections.length} match${detections.length > 1 ? 'es' : ''}`;
    
    resultsGrid.innerHTML = '';
    detections.forEach(detection => {
        const item = document.createElement('div');
        item.className = 'result-item';
        item.innerHTML = `
            <img src="${API_URL}/results/${detection.image}" alt="Detection">
            <div class="result-info">
                <p><strong>Timestamp:</strong> ${formatTime(detection.timestamp)}</p>
                <p><strong>Frame:</strong> ${detection.frame}</p>
            </div>
        `;
        resultsGrid.appendChild(item);
    });
}

// Helper functions
function showStatus(elementId, message, type) {
    const status = document.getElementById(elementId);
    status.textContent = message;
    status.className = `status ${type}`;
}

function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

// Load videos on page load
loadVideos();
