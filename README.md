# Network Intrusion Detection System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-green)
![Dataset](https://img.shields.io/badge/Dataset-NSL--KDD-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## Project Overview

This project implements a Machine Learning based Network Intrusion Detection System (NIDS) using the NSL-KDD dataset.

The system analyzes network traffic data and classifies it as normal traffic or malicious attack.

The objective of this project is to improve network security by detecting cyber attacks in network traffic using machine learning techniques and intelligent data analysis.

## Technologies Used

- Python  
- Scikit-learn  
- XGBoost  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Google Colab / Jupyter Notebook  

## Dataset

This project uses the NSL-KDD Dataset, a widely used benchmark dataset for network intrusion detection research.

### Dataset Features

The dataset contains several network traffic attributes such as:

- Duration of connection  
- Protocol type  
- Network service  
- Source bytes  
- Destination bytes  
- Error rates  
- Traffic statistics  

Each network record is labeled as:

- Normal Traffic  
- Attack Traffic  

## Methodology
The intrusion detection system follows the workflow shown below:

NSL-KDD Dataset
↓
Data Preprocessing
↓
Missing Value Checking
(Self-Healing Data Preparation)
↓
Feature Encoding
↓
Feature Scaling
↓
Machine Learning Model Training
↓
Intrusion Detection
↓
Performance Evaluation

## Machine Learning Models

The following machine learning models were implemented:

- Decision Tree  
- Random Forest  
- XGBoost  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

Among these models, Random Forest and XGBoost showed the best performance in detecting network intrusions.

## Evaluation Metrics

The model performance was evaluated using the following metrics:

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

## Results

The developed intrusion detection system achieved an accuracy between:

77% – 95%

Random Forest and XGBoost models demonstrated strong performance in detecting malicious network traffic.

## Project Structure

Network-Intrusion-Detection-System
│
├── dataset
│ ├── NSL_KDD_Train.csv
│ └── NSL_KDD_Test.csv
│
├── notebooks
│ └── intrusion_detection_model.ipynb
│
├── results
│ └── confusion_matrix.png
│
├── code
│ └── intrusion_detection.py
│
└── README.md

## Future Improvements

- Implement deep learning based intrusion detection models  
- Add real-time network traffic monitoring  
- Develop a web dashboard for network security monitoring  
- Integrate with cybersecurity monitoring systems  

## Author

Adarsh T K
Sirisha B A
Vaishnavi N Waddar
Janani K V 

Information Science and Engineering  
Nitte Meenakshi Institute of Technology
