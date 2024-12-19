import csv
import os


def save_footfall_log(data, log_path="data/logs/footfall_log.csv"):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, mode="w", newline=" ", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Frame", "Footfall"])
        writer.writerow(data)
