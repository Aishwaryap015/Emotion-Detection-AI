# 🧠 Emotion Detection AI Web App
🧠 Emotion Detection AI Web App
👩‍💻 Developed By

Aishwarya Priydarshni
CSE (Data Science)

## 📌 Overview

This project is an advanced Emotion Detection Web Application built using Python and Flask. It analyzes user-input text and predicts the underlying emotions such as joy, sadness, anger, fear, and more.

The application is enhanced with an interactive and modern UI, making it not just functional but also visually appealing and user-friendly.

---

## 🚀 Features

* 🔍 **Real-time Emotion Detection**
  Analyze emotions instantly from user input text

* 🎤 **Voice Input Support**
  Speak instead of typing using built-in speech recognition

* 🌗 **Dark / Light Mode Toggle**
  Switch themes dynamically for better user experience

* 🎨 **Dynamic Animated UI**
  Auto-changing gradient background with floating elements

* 📊 **Emotion Visualization**
  Displays results using interactive charts

* 📥 **Download Results**
  Save emotion analysis output as a file

* ⚠️ **Error Handling**
  Handles invalid input and API failures gracefully

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js
* **AI Service:** Watson NLP Emotion Detection

---

## 📂 Project Structure

```
EmotionDetection/
│
├── static/
│   ├── style.css
│   └── favicon.png
│
├── templates/
│   └── index.html
│
├── emotion_detection.py
├── server.py
├── test_emotion_detection.py
├── README.md
└── LICENSE
```

---

## ⚙️ How It Works

1. User enters or speaks text
2. Request is sent to Flask backend
3. Backend calls emotion detection function
4. Results are processed and returned
5. Frontend displays:

   * Dominant emotion
   * Emotion scores chart

---

## ▶️ Running the Project

### Step 1: Install dependencies

```bash
pip install flask requests
```

### Step 2: Run the server

```bash
python server.py
```

### Step 3: Open browser

```
http://127.0.0.1:5000
```

---

## 🧪 Testing

Unit tests are included to verify the functionality of the emotion detection module.

```bash
python test_emotion_detection.py
```

---

## 🌟 Future Improvements

* Add user authentication
* Store history of emotion analysis
* Improve ML model accuracy
* Mobile responsive UI

---

## 📄 License

This project is licensed under the Apache 2.0 License.

---

## 🙌 Acknowledgment

This project is inspired by IBM Watson AI-based emotion detection concepts and extended with additional features and UI enhancements.
