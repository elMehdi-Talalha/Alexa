import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Initialize volume control - FIXED VERSION
speakers = AudioUtilities.GetSpeakers()
interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get volume range
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

# Initialize webcam - Try different camera indices
cap = None
for camera_index in [0, 1, 2]:
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)  # Use DirectShow for Windows
    if cap.isOpened():
        print(f"Camera found at index {camera_index}")
        break
    cap.release()

if not cap or not cap.isOpened():
    print("Error: Could not open camera!")
    print("Please check:")
    print("1. Camera is not being used by another application")
    print("2. Camera permissions are granted")
    print("3. Camera drivers are installed")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("\n✓ Hand Gesture Volume Control Started!")
print("✓ Use your thumb and index finger to control volume")
print("✓ Press 'q' to quit\n")

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Flip image for mirror effect
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process image for hand detection
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                img, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
            )
            
            # Get coordinates of thumb tip (4) and index finger tip (8)
            h, w, c = img.shape
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            
            # Convert normalized coordinates to pixel coordinates
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            
            # Calculate distance between thumb and index finger
            distance = math.sqrt((index_x - thumb_x)**2 + (index_y - thumb_y)**2)
            
            # Map distance to volume (20-200 pixels mapped to min-max volume)
            # Adjust these values based on your camera distance
            min_distance = 20
            max_distance = 200
            
            # Clamp distance
            distance = max(min_distance, min(distance, max_distance))
            
            # Convert distance to volume
            vol = np.interp(distance, [min_distance, max_distance], [min_vol, max_vol])
            vol_percentage = np.interp(distance, [min_distance, max_distance], [0, 100])
            
            # Set system volume
            volume.SetMasterVolumeLevel(vol, None)
            
            # Visual feedback - line thickness changes with distance
            line_thickness = int(np.interp(distance, [min_distance, max_distance], [2, 15]))
            
            # Draw line between thumb and index finger
            cv2.line(img, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 255), line_thickness)
            
            # Draw circles on fingertips
            cv2.circle(img, (thumb_x, thumb_y), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)
            
            # Draw midpoint circle
            mid_x, mid_y = (thumb_x + index_x) // 2, (thumb_y + index_y) // 2
            cv2.circle(img, (mid_x, mid_y), 8, (255, 255, 0), cv2.FILLED)
            
            # Display volume percentage
            cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
            cv2.rectangle(img, (50, int(np.interp(vol_percentage, [0, 100], [400, 150]))), 
                         (85, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(vol_percentage)}%', (40, 450), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            
            # Display distance
            cv2.putText(img, f'Distance: {int(distance)}px', (mid_x - 80, mid_y - 20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    # Instructions
    cv2.putText(img, 'Pinch fingers to control volume', (10, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, 'Press Q to quit', (10, 60), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    # Display image
    cv2.imshow('Hand Gesture Volume Control', img)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
hands.close()