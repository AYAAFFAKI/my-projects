# Gaze Tracker Utils

This module provides utility functions for eye gaze estimation using facial landmarks.

## Features

- Compute the actual eye gaze vector from eye landmarks
- Normalize gaze direction based on eye geometry

## File

- `gaze_tracker_utils.py`:
  - `compte_actual_eye_gaze(landmarks, frame_width, frame_height)`:  
    Computes the eye center and the normalized gaze vector based on MediaPipe facial landmarks.

## How It Works

- Uses 3 key landmarks:
  - `iris` (index 468)
  - `outer eye corner` (index 33)
  - `inner eye corner` (index 133)
- Calculates eye axis and center
- Returns:
  - `eye_center`: midpoint between eye corners
  - `gaze_vec`: normalized vector from center to iris

## Requirements

- `numpy`

## Example

from gaze_tracker_utils import compte_actual_eye_gaze

eye_center, gaze_vec = compte_actual_eye_gaze(landmarks, width, height)

## License

Open for educational and personal use.

```

