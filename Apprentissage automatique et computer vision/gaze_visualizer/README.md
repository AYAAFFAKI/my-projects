# Gaze Visualizer

This module provides visualization tools to display eye gaze data on video frames.

## Features

- Draws gaze direction bars indicating left, center, and right gaze counts
- Visualizes gaze data overlayed on video frames using OpenCV

## File

- `gaze_visualizer.py`:
  - `draw_gaze_bar(frame, counts, position=(20,80))`:
    Draws colored bars representing gaze counts for left, center, and right directions.

## Requirements

- OpenCV (`cv2`)

## Example

import cv2
from gaze_visualizer import draw_gaze_bar

# Dummy frame and counts
frame = cv2.imread('frame.jpg')
counts = {'Left': 10, 'Center': 5, 'Right': 3}

draw_gaze_bar(frame, counts)

cv2.imshow('Gaze Visualization', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

## License

Free for academic and personal use.



