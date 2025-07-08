---

# Gaze Logger

This module provides basic tools to log gaze tracking data to a CSV file.

## Features

- Initialize a CSV file with headers for gaze data
- Append gaze data (frame, position, fixation, side) to the CSV

## Files

- `gaze_logger.py`: Contains two functions:
  - `init_csv(csv_file)`: Creates a new CSV file with column headers.
  - `append_gaze_data(csv_file, frame_count, gaze_vec, fixation, side)`: Appends one row of gaze data to the file.

## Example

from gaze_logger import init_csv, append_gaze_data

# Create the CSV file
init_csv("output.csv")

# Example of appending gaze data
gaze_vec = [0.45, 0.33]
append_gaze_data("output.csv", frame_count=1, gaze_vec=gaze_vec, fixation=True, side='left')
````

## Requirements

This module only uses Python's built-in `csv` module — no external libraries are needed.

## License

Free to use for academic or personal projects.

```
