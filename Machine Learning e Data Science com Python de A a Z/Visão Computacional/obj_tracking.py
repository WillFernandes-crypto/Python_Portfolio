import cv2
import os

tracker = cv2.TrackerCSRT_create()

video_path = os.path.join(os.path.dirname(__file__), 'imgs', 'rua.mp4')
video = cv2.VideoCapture(video_path)
ok, frame = video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break
    
    ok, bbox = tracker.update(frame)
    
    if ok:
       (x, y, w, h) = [int(v) for v in bbox]
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, "Tracking falhou", 
                    (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.75, (0, 0, 255), 2)
    
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break