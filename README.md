Hand Gesture Volume Control 🎚️🖐️

A Python project that lets you control your system's volume using **hand gestures** captured through your webcam. The index finger and thumb positions are tracked in real-time using **MediaPipe** and **OpenCV**, and volume is adjusted via **PyAutoGUI**.

🛠️ Tech Stack
- Python
- OpenCV
- MediaPipe
- PyAutoGUI

💡 How It Works?
- 📷 The webcam captures your hand in real-time.
- ✋ If the **index finger** is higher than the **thumb**, the volume goes **up**.
- 👇 If the **index finger** is lower than the **thumb**, the volume goes **down**.
- 🕒 A cooldown is used to avoid too many rapid changes.
- ❌ Press `q` to exit the program.

🧪 Installation & Running the Code

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/hand-gesture-volume-control.git
cd hand-gesture-volume-control

# Step 2: (Optional) Create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Step 3: Install required libraries
pip install opencv-python mediapipe pyautogui

# Step 4: Run the script
python hand_volume_control.py
```
📸 Output Preview

You’ll see a live webcam window titled "Hand Gesture Volume Control". 

Based on the finger gesture : "Volume Up" or"Volume Down" will be displayed, and the system volume will change accordingly.
