import torch


def load_model(weights_path="models/yolo5/yolo5s.pt"):
    model = torch.hub.load("ultralytics/yolo5", "custom", path=weights_path)
    return model


def count_people(frame, model):
    results = model(frame)
    detections = results.xyxy[0]  # To get detection results
    people_count = 0
    for detection in detections:
        if int(detection[-1]) == 0:  # checking if the detection is a person
            people_count += 1
    return people_count
