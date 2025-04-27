#Sight Beyond Vision: An AI-Driven Approach to Currency and Object Detection for the Visually Impaired
Sight Beyond Vision is a socially impactful AI project designed to empower visually impaired individuals by providing real-time assistance in identifying currency notes and everyday objects. Leveraging the power of Artificial Intelligence (AI), Machine Learning (ML), and Computer Vision, this system bridges the accessibility gap, promoting greater independence and confidence in day-to-day activities.

Project Objective
The primary goal of Sight Beyond Vision is to create an affordable, user-friendly, and efficient tool that enables visually impaired users to:

Detect and recognize different denominations of currency.

Identify and classify commonly used objects in their surroundings.

Receive instant feedback through audio output for easy understanding.

Features
🎯 Currency Detection: Accurately recognizes multiple denominations, including worn or slightly damaged notes.

🛍️ Object Detection: Identifies a wide range of common objects (e.g., bottle, book, pen, phone, etc.).

🎤 Voice Assistance: Converts detection results into clear voice output in real-time.

🌐 Multi-Language Support: Supports multiple Indian languages, making it accessible to a wider user base.

📱 Simple User Interface: Minimal interaction needed; optimized for ease of use.

⚡ Lightweight and Fast: Optimized models to work on basic devices without requiring high-end hardware.

Technology Stack
Programming Language: Python

AI/ML Frameworks: TensorFlow, Keras

Computer Vision: OpenCV, YOLOv5 (You Only Look Once) / SSD (Single Shot MultiBox Detector)

Audio Output: pyttsx3 / gTTS (Google Text-to-Speech)

Platform Compatibility: Windows, Linux, Android (prototype version)

Additional Tools: Numpy, Pandas, Pillow, SpeechRecognition

Architecture Overview
Input: Live camera feed or uploaded image.

Preprocessing: Frame resizing, noise removal, and normalization.

Detection:

Currency recognition model classifies denominations.

Object detection model classifies objects.

Voice Output: Detected information is converted into speech and announced to the user.

Feedback Loop: Continuous detection for new frames.

How It Works
The user points the device camera towards an object or currency note.

The system captures the frame and processes it using trained AI models.

The recognized item is converted into an audio message.

The audio is played through speakers or earphones, informing the user about the object or currency denomination.
![Currency Detection Screenshot](images/currency_detection_outp![Screenshot 2025-04-01 175920](https://github.com/user-attachments/assets/b6853815-e5e2-4011-900b-eea8a7ff0b1d)
ut.png)
![Screenshot 2025-04-01 175616](https://github.com/user-attachments/assets/980d57dc-0e1d-42df-a80a-e5a69d1c79f8)


Key Benefits
Enhances independence and confidence of visually impaired individuals.

Eliminates the risk of currency fraud.

Assists in daily object recognition, promoting a better quality of life.

Affordable and scalable solution suitable for real-world deployment.

Future Enhancements
📈 Expand the object detection library to cover more items.

🎙️ Improve voice interaction for two-way communication.

📱 Develop a lightweight mobile app for Android and iOS.

🌐 Enable offline functionality for remote areas with limited internet access.

🔋 Optimize battery usage for portable devices.

Team Members
Avula Venkat Rao

AS Ashiq

A Rajesh Kumar

Guide
Mrs. S. Jenita Christy (M-Tech), Professor

Institution
Bharath Institute of Science and Technology

Acknowledgements
Special thanks to our guide, Mrs. S. Jenita Christy, for her valuable mentorship, and to all the professors, peers, and open-source contributors whose resources and guidance made this project possible.
