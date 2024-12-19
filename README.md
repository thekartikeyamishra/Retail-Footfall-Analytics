# Retail-Footfall-Analytics
For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

The **Retail Footfall Analytics** project is designed to help small businesses and MSMEs track customer footfall in retail stores. By leveraging **Computer Vision** techniques, this tool counts people entering and exiting stores from video footage, offering real-time insights and efficient data logging. 

---

### **Features**

1. **Real-Time Footfall Counting**:
   - Utilizes a pre-trained object detection model (**YOLOv5**) to count the number of people in video streams.  

2. **Data Logging**:
   - Logs footfall data for every video frame into a CSV file for analysis.  

3. **Simple Dashboard**:
   - Provides a GUI to display the current footfall count and total footfall statistics.  

---

### **File and Folder Structure**

```bash
RetailFootfallAnalytics/
├── data/
│   ├── videos/                  # Folder for input video files
│   ├── logs/                    # Folder for saving footfall data logs
├── models/
│   ├── yolov5/                  # Pre-trained YOLOv5 model weights
├── utils/
│   ├── __init__.py              # Initializes the utils module
│   ├── footfall_counter.py      # Logic for counting people in video
│   ├── file_handler.py          # File handling utilities for logs
│   ├── video_processor.py       # Video processing logic
├── gui/
│   ├── __init__.py              # Initializes the GUI module
│   ├── analytics_gui.py         # GUI implementation using Tkinter
├── main.py                      # Entry point for the application
├── requirements.txt             # Dependencies required for the project
├── README.md                    # Documentation for the project
```

---

### **Installation Instructions**

Follow these steps to set up and run the project:

#### **1. Clone the Repository**:
```bash
git clone https://github.com/thekartikeyamishra/Retail-Footfall-Analytics.git
cd RetailFootfallAnalytics
```

#### **2. Set Up Virtual Environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### **3. Install Dependencies**:
```bash
pip install -r requirements.txt
```

#### **4. Run the Application**:
```bash
python main.py
```

---

### **How It Works**

1. **Real-Time Counting**:  
   - The application processes video streams using YOLOv5 to detect and count individuals in each frame.  

2. **Data Logging**:  
   - Saves the footfall count for each frame into a CSV file, enabling businesses to analyze customer patterns over time.  

3. **User-Friendly Dashboard**:  
   - A simple GUI, built with Tkinter, displays the current and total footfall counts and allows video uploads.  

---

### **Future Enhancements**

1. **Support for Additional Programming Languages**:
   - Expand support to other programming languages like **Java** and **C++**.  

2. **Auto-Fix Suggestions**:
   - Implement automated solutions for common errors detected during video analysis.  

3. **Advanced AI Models**:
   - Integrate advanced AI capabilities for behavior detection, heatmap generation, and live stream integration.  

---

### **Basic Features**

- **Real-Time Footfall Counting**:
   - Detect and count people in videos using **YOLOv5**.  

- **Data Logging**:
   - Automatically logs footfall data to a CSV file for future reference.  

- **Interactive Dashboard**:
   - View and manage footfall data through a user-friendly GUI.

---

### **Contribute and Feedback**

Feel free to contribute to this project by submitting pull requests or reporting issues. Your feedback is invaluable in enhancing this tool. If you find this project helpful, don’t forget to ⭐ **star the repository** on GitHub!

---

### **Contact**

For queries or suggestions, reach out via GitHub issues or email. Let’s collaborate to make this project even better!  

#RetailAnalytics #ComputerVision #YOLOv5 #PythonProjects #DataLogging #FootfallAnalytics #OpenSource #MSME
