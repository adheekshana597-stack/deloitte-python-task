# 🏭 IoT Sensor Data Analysis Project

## 📌 Project Overview
This project analyzes IoT sensor data from a manufacturing factory to monitor machine health and temperature conditions.  
The workflow includes *data cleaning, transformation, and exploratory data analysis (EDA)* using Python.

---

## 📂 Dataset

The dataset contains IoT device readings from factory machines.

### Key Fields:
- device_id → Unique machine identifier  
- device_type → Type of machine (e.g., LaserCutter)  
- timestamp → Sensor reading time  
- location → Factory location details  
- status → Machine health status (HEALTHY / FAULTY)  
- temperature → Machine operating temperature  

---

## 🧹 Data Cleaning
Performed in src/data_cleaning.py:

- Removed nested structure  
- Standardized column names  
- Normalized location fields  
- Converted timestamp format  
- Standardized status values  
- Ensured temperature consistency  

---

## 📊 Analysis Performed
Performed in src/analysis.py:

- Machine status distribution  
- Average temperature analysis  
- Location-wise device count  
- Basic trend visualization  

---

## 🛠️ Tools Used
- Python  
- Pandas  
- Matplotlib  

---

## 📁 Project Structure
- data/ → raw & cleaned data  
- src/ → Python scripts  
- output/ → charts and results  

---

## 🚀 Result
This analysis helps in monitoring machine health and identifying operational patterns in IoT factory systems.

---

## 👨‍💻 Author
Data Analytics Project (Portfolio Practice)
