# Easy Computer

A touchless Windows volume and media controller powered by real-time computer vision. Built in Python using `OpenCV`, Google's `MediaPipe` Hand Landmarker task, `PyAutoGUI`, and `Pycaw`—letting you control system audio and YouTube playback directly through webcam hand gestures with 100% local processing.

## Prerequisites
1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Download Google's official **`HandLandmarker (float16)`** model (`hand_landmarker.task`) from the MediaPipe documentation and place it in the root project folder next to `EasyComputer.py`.

## How to Run
1. Make sure your webcam is not being used by another application.
2. Run the script in your terminal:
   ```bash
   python EasyComputer.py
   ```
3. Press **`q`** while the webcam window is focused to exit cleanly.

## Gesture Controls

| Hand Sign | Finger State | Action Triggered | Shortcut / API Used |
| :--- | :--- | :--- | :--- |
| **☝️ Index + Thumb Pinch** | Index finger up; middle, ring, and pinky curled | Smoothly adjusts Windows master volume (`0%`–`100%`) | `pycaw` `EndpointVolume` |
| **✊ Closed Fist** | All four fingers curled down | Play / Pause active media | `playpause` media key |
| **✌️ Peace Sign** | Index and middle fingers up; ring and pinky curled | Skip to next YouTube video | `Shift + N` |
| **🤟 Three Fingers** | Index, middle, and ring fingers up; pinky curled | Go to previous YouTube video | `Shift + P` |

## Variables You Can Customize

| Variable / Value | Default | What It Controls | Try Changing It To |
| :--- | :--- | :--- | :--- |
| **`[0.03, 0.22]`** | `0.03` to `0.22` | Min and max thumb-to-index pinch distance mapped to `0%`–`100%` volume | `[0.04, 0.18]` (shorter pinch range) or `[0.02, 0.25]` (wider range) |
| **`2.0`** (cooldown) | `2.0` seconds | Minimum delay between media actions to prevent accidental double triggers | `1.0` (faster skipping) or `3.0` (stricter debounce) |
| **`num_hands`** | `1` | Maximum number of hands tracked simultaneously | Keep at `1` for lowest CPU usage |

## Roadmap (Upcoming Commits)
* [ ] **Non-invasive Sleep/Wake Clutch:** Hold-to-wake toggle gesture so normal desk movements never trigger accidental commands
* [ ] **Toggleable Air Mouse:** Smoothed index-finger cursor control with middle-thumb pinch clicking
* [ ] **Context-Aware Gestures:** Auto-detect active windows (`Chrome`, `VS Code`, `Spotify`) to dynamically remap hand signs
