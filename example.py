"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""


import vlc
import time
import cv2
from gaze_tracking import GazeTracking

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new('gen.mp3')
player.set_media(media)
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
start=time.time()
text=""
text_state=""
count=0
#flag=0


while True:
    _, frame = webcam.read()
    #print('Hello')
    dist=gaze.face_id(frame)

    if dist == 0:
        #print('Hello')
        continue
    elif dist<0.6:
        print('%s, Distance: %s' % (dist<0.6, dist)) 
        break;
    

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"
    
    if gaze.test(text,start):
        text_state="Sleepy State!!"
        count+=1
    else:
        text_state="Normal"
    
    if count ==3 and text_state=="Sleepy State!!":
        player.play()
        count=0

    cv2.putText(frame, text, (0, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, text_state, (0,120),cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (0, 360), cv2.FONT_HERSHEY_DUPLEX, 1.3, (147, 58, 31), 2)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (0, 400), cv2.FONT_HERSHEY_DUPLEX, 1.3, (147, 58, 31), 2)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
