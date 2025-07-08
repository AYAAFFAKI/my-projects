#Apprentissage Automatique et Computer Vision

This repository contains projects and modules related to machine learning and computer vision, focusing on eye gaze tracking, emotion detection, and visualization tools.

## Project Structure

- `gaze_logger/`  
  Functions to log gaze tracking data into CSV files.

- `gaze_tracker_utils/`  
  Utility functions for eye gaze estimation from facial landmarks.

- `gaze_visualizer/`  
  Visualization tools to display gaze data on video frames.

- Main scripts  
  Integrate emotion recognition, gaze tracking, and visualization in real-time video processing.

## Features

- Real-time face mesh and holistic landmark detection using MediaPipe  
- Eye gaze vector calculation and fixation detection  
- Emotion recognition with a trained TensorFlow model  
- Visualization of gaze direction statistics on video frames  
- Data logging for further analysis  

## Requirements

- Python 3.x  
- OpenCV  
- MediaPipe  
- TensorFlow  
- NumPy

## How to Run

1. Install dependencies:

   pip install opencv-python mediapipe tensorflow numpy


2. Run the main script (adjust filename as needed):

   python main.py
  

## License

Free for academic and personal use.

## Contact

For questions or contributions, feel free to open an issue or contact the repository owner.



