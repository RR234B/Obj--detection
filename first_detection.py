from ultralytics import YOLO
import cv2

#Load model
model = YOLO("yolo11n.pt")
#Read image
cap = cv2.VideoCapture(0)
#YOLO Prediction


#Get bounding 
while True:
  sucess , img = cap.read()
  img = cv2.flip(img , 1)
  results = model(img, verbose = False)
 #First result
  result = results[0]
  boxes = result.boxes.xyxy
  confidences =  result.boxes.conf
  class_ids = result.boxes.cls
  #Loop through every detected object 
  for box, confidence, class_id in zip(boxes, confidences, class_ids):

    #Coordinates
    x1 = int(box[0])
    y1 = int(box[1])
    x2 = int(box[2])
    y2 = int(box[3])

    class_id = int(class_id)
    class_name = result.names[class_id]

   #Create label
    label = f"{class_name} {confidence:.2f}"

    print("Class ID:", class_id)
    print("Class Name:", class_name)
    print("Confidence:",confidence)

    #dRaw rectangle
    cv2.rectangle(
     img,
    (x1, y1),
    (x2, y2),
    (0,255,0),
    2
    )

    cv2.putText(
    img,label,
    (x1, y1 - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0,255,0),
    2
    )

  cv2.imshow("YOLO Detection", img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  # cv2.destroyAllWindows()