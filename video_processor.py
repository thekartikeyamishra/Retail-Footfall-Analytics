import cv2
from utils.footfall_counter import load_model, count_people

def process_video(video_path, model):
    cap = cv2.VideoCapture(video_path)
    footfall_data = []
    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_number += 1
        people_count = count_people(frame, model)
        footfall_data.append([frame_number, people_count])

        # Display the video with the count overlay
        cv2.putText(frame, f"People: {people_count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Retail Footfall Analytics: ", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return footfall_data