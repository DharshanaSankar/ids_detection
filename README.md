# 🔐 Intrusion Detection System (IDS) using Machine Learning
## 🧠 Overview
This project is a Machine Learning-based Intrusion Detection System (IDS) that classifies network traffic as **Normal** or **Attack**. It uses the NSL-KDD dataset and a Random Forest classifier to detect malicious activities.
The system is deployed as an interactive web application using Streamlit, allowing users to upload network traffic data and get real-time predictions
## 🚀 Features
- Detects network traffic as **Normal** or **Attack**
- Uses **NSL-KDD dataset**
- Implements **Random Forest algorithm**
- Performs **data preprocessing & feature engineering**
- Interactive **Streamlit web application**
- Displays **prediction summary and sample results**
## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
## ⚙️ How It Works
1. Dataset is preprocessed:
   - Removes unnecessary columns
   - Encodes categorical data
   - Converts labels to binary (Normal/Attack)
2. Model Training:
   - Random Forest classifier is trained
   - Model and feature columns are saved
3. Deployment:
   - Streamlit app loads model
   - User uploads dataset
   - System predicts traffic type
## ▶️ How to Run
### 1. Install dependencies
pip install -r requirements.txt
### 2. Train the model
python train_model.py
### 3. Run the application
streamlit run app.py

## 📊 Sample Output
- Summary of Normal and Attack traffic
- Sample predictions displayed in UI
## 🎯 Use Case
This system can be used in cybersecurity applications to monitor and detect suspicious network activities.
## 🎤 Author
Developed as a Machine Learning project for Intrusion Detection.
