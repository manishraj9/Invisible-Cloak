# 🫥 Invisible Cloak

A real-time **Invisible Cloak effect** built using **Python, OpenCV, and NumPy**.

The application uses a webcam to detect a selected cloak color and replaces that colored region with a previously captured background. This creates the illusion that the cloak — and the person wearing it — has become invisible.

---

## 📌 Overview

The Invisible Cloak project demonstrates how computer vision can be used to create a real-time invisibility effect.

The application first captures the background without the user in the frame. It then continuously captures webcam frames, detects the selected cloak color, and replaces the detected region with the corresponding pixels from the captured background.

### Basic workflow

```text
Webcam
   ↓
Capture Background
   ↓
Capture Live Frame
   ↓
Convert BGR → HSV
   ↓
Detect Cloak Color
   ↓
Create Color Mask
   ↓
Replace Cloak Area
   ↓
Combine With Live Frame
   ↓
Display Invisible Cloak Effect
✨ Features
🎥 Real-time webcam processing
🫥 Invisible cloak visual effect
🎨 Multiple cloak-color support
📸 Automatic background capture
🔄 Mirrored webcam view
🎯 HSV-based color detection
🧹 Noise reduction using morphological operations
🖼️ Background replacement
🔍 Debug mask window
⚡ Real-time OpenCV processing
💻 Runs locally on Windows, macOS, and Linux
🎨 Supported Cloak Colors

The current program supports four cloak colors:

Color	Supported
🔴 Red	✅
🔵 Blue	✅
🩷 Pink	✅
🟡 Yellow	✅

The active cloak color is selected in:

main(cloak_color="yellow")

For example, to use a red cloak:

main(cloak_color="red")
🛠️ Technologies Used
Python 3
OpenCV
NumPy
Webcam / Camera
HSV Color Space
Image Processing
📂 Project Structure
Invisible-Cloak/
│
├── invisible_cloak.py
├── .gitattributes
├── .gitignore
└── README.md
💻 Requirements

Before running the application, make sure you have:

Python 3 installed
A working webcam
OpenCV-compatible camera
Internet connection for installing Python packages
⚙️ Installation
1. Clone the Repository
git clone https://github.com/manishraj9/Invisible-Cloak.git

Move into the project directory:

cd Invisible-Cloak
2. Create a Virtual Environment

It is recommended to use a virtual environment.

Windows
python -m venv venv

Activate it:

venv\Scripts\activate

You should see:

(venv)

at the beginning of your terminal.

macOS / Linux
python3 -m venv venv
source venv/bin/activate
📦 Install Dependencies

Install the required Python packages:

python -m pip install opencv-python numpy

You can verify the installation:

python -c "import cv2, numpy; print('OpenCV:', cv2.__version__); print('NumPy:', numpy.__version__)"

Example output:

OpenCV: 4.x.x
NumPy: 2.x.x
▶️ Run the Application

Start the program with:

python invisible_cloak.py

The application will open your webcam.

You will first see:

Capturing background... step out of frame.
📸 Step 1 — Capture the Background

When the program displays:

Capturing background... step out of frame.

move completely out of the camera frame.

The program waits briefly and captures multiple background frames.

These frames are combined to create a clean background image.

After the process finishes, you will see:

Background captured.
🫥 Step 2 — Use the Cloak

After the background is captured, the program starts the cloak effect:

Cloak effect running. Press 'q' to quit.

Now enter the camera frame while wearing a cloth with the selected cloak color.

The application detects that color and replaces it with the previously captured background.

This creates the invisible cloak illusion.

🖥️ Application Windows

The application displays two windows.

1. Invisible Cloak

This window displays the final processed video.

Live Camera
     +
Background Replacement
     ↓
Invisible Cloak Effect
2. Mask (Debug)

This window displays the detected cloak-color mask.

The mask is useful for checking whether the selected cloak color is being detected correctly.

🛑 Stop the Application

To stop the application:

Click the Invisible Cloak window.
Press:
q

The OpenCV windows will close.

You can also stop the program from the terminal with:

Ctrl + C
🧠 How the Project Works

The project uses a simple computer-vision pipeline.

1. Webcam Capture

OpenCV accesses the webcam using:

cv2.VideoCapture(0)

The camera continuously provides video frames.

2. Background Capture

The application captures multiple frames while the user is outside the camera view.

The frames are combined using a median operation:

background = np.median(backgrounds, axis=0).astype(np.uint8)

This creates a stable background image.

3. Color Detection

The webcam frame is converted from BGR to HSV:

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

HSV makes it easier to identify a specific color.

4. Create the Cloak Mask

OpenCV's inRange() function is used to identify pixels belonging to the cloak.

For example:

mask = cv2.inRange(hsv_frame, lower, upper)

The resulting mask identifies the region that should become invisible.

5. Clean the Mask

Morphological operations are applied to remove noise and improve the mask:

cv2.morphologyEx()
cv2.medianBlur()

This helps produce smoother results.

6. Replace the Cloak

Pixels belonging to the cloak are taken from the captured background:

cloak_area = cv2.bitwise_and(
    background,
    background,
    mask=cloak_mask
)

The remaining pixels come from the live webcam frame.

7. Generate the Final Frame

The background and live image are combined:

final_output = cv2.addWeighted(
    cloak_area,
    1,
    visible_area,
    1,
    0
)

The final result is displayed in real time.

🎨 Changing the Cloak Color

At the bottom of invisible_cloak.py, you will find:

main(cloak_color="yellow")

Change the value to one of the supported colors.

Red
main(cloak_color="red")
Blue
main(cloak_color="blue")
Pink
main(cloak_color="pink")
Yellow
main(cloak_color="yellow")
🎯 Tips for Better Results

For a better invisible-cloak effect:

💡 Use a solid-colored cloth

Avoid patterns, logos, or multiple colors.

💡 Use good lighting

Make sure the cloak is clearly visible.

💡 Avoid background colors similar to the cloak

If the background contains the same color, the application may detect those areas too.

💡 Keep the camera stable

A stationary camera produces better background replacement.

💡 Capture a clean background

Make sure nobody is standing in the camera frame during background capture.

💡 Use the debug mask

The Mask (debug) window helps you determine whether the cloak color is being detected properly.

⚠️ Current Limitations

The current version uses color-based detection, so its performance depends on lighting and background conditions.

Known limitations include:

Similar colors in the background may also be detected.
Changing lighting can affect color detection.
Shadows may affect the cloak mask.
The camera should remain relatively stationary.
The cloak should have a reasonably consistent color.
The current system does not use AI-based person segmentation.
🚀 Future Improvements

The project can be expanded significantly.

🎨 Better Color Detection
Automatic color calibration
Interactive HSV controls
Dynamic color selection
Improved lighting compensation
🤖 AI-Based Segmentation

Future versions could use computer-vision or AI segmentation to detect the person instead of relying only on cloak color.

Possible improvements:

Person segmentation
Body segmentation
Background segmentation
Improved edge detection
🖥️ User Interface

A graphical interface could provide:

Start/Stop button
Camera selection
Cloak color selection
Background capture button
HSV sensitivity controls
FPS display
Processing status
🎬 Recording

Future versions could support:

Record the invisible effect
Save processed videos
Capture screenshots
Export demonstration clips
⚡ Performance

Potential improvements include:

Faster frame processing
Resolution controls
FPS optimization
GPU acceleration
Better mask processing
📸 Demo

A demonstration video/GIF will be added after the project receives its next major improvements.

🧪 Example Output

When the application starts successfully:

Capturing background... step out of frame.
Background captured.
Cloak effect running. Press 'q' to quit.

The application then displays the real-time invisible cloak effect.

🔧 Troubleshooting
Camera does not open

If you see:

Could not open webcam (index 0).

check that:

Your webcam is connected.
No other application is using the camera.
Windows has granted camera permission.
The correct camera index is being used.

You can try changing:

cv2.VideoCapture(0)

to:

cv2.VideoCapture(1)

if your computer has multiple cameras.

ModuleNotFoundError: No module named 'cv2'

Install OpenCV:

python -m pip install opencv-python

Then verify:

python -c "import cv2; print(cv2.__version__)"
ModuleNotFoundError: No module named 'numpy'

Install NumPy:

python -m pip install numpy
Cloak is not detected

Try:

Better lighting
A brighter cloak
A solid cloak color
Moving away from similarly colored objects
Checking the Mask (debug) window
Adjusting the HSV ranges in the Python code
🔐 Privacy

The application uses the webcam locally through OpenCV.

The current project does not require a backend server to process the camera frames.

Camera access is required for the application to work.

📈 Project Roadmap
[x] Webcam capture
[x] Background capture
[x] Color-based cloak detection
[x] Background replacement
[x] Multiple cloak colors
[x] Debug mask
[ ] Improved user interface
[ ] Automatic color selection
[ ] Better edge refinement
[ ] AI person segmentation
[ ] Video recording
[ ] Screenshot capture
[ ] Performance optimization
[ ] Packaged desktop application
🤝 Contributing

Contributions and suggestions are welcome.

If you want to improve the project:

Fork the repository.
Create a new branch.
Make your changes.
Test the application.
Commit your changes.
Open a pull request.

Example:

git checkout -b feature/improved-detection
📜 License

This project is created for educational and development purposes.

👨‍💻 Author
MANISH RAJ

GitHub:

https://github.com/manishraj9

Project:

https://github.com/manishraj9/Invisible-Cloak

⭐ Support

If you found this project interesting, consider giving the repository a ⭐ on GitHub.

🫥 Built with Python + OpenCV

Explore computer vision. Build something invisible.


### Then push it

After saving `README.md`, run:

```powershell
git add README.md
git commit -m "Add complete project documentation"
git push
