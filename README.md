# Network Intrusion Detection System (NIDS) using Machine Learning
This project presents a Machine Learning-based Network Intrusion Detection System (NIDS) that classifies benign and malicious network traffic using flow-based features. The system is designed to detect cyber attacks such as DDoS, Botnet, and Bruteforce activities while addressing challenges like class imbalance and data leakage in cybersecurity datasets.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24+-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)

## Project Overview:
As cyber threats become increasingly sophisticated, traditional rule-based intrusion detection systems struggle to keep up. This project explores a data-driven approach to cybersecurity, utilizing Machine Learning to classify network traffic and detect malicious activities in a multiclass setting.

## Dataset:
The data is sourced from network traffic captures and includes features extracted from network flows (`Benign`, `DDoS`, `Botnet`, `Bruteforce`.).

## Methodology & Pipeline:
Data integration: A consolidated dataset was created by combining multiple daily data.
Data preprocessing and encoding: Categorical text labels were converted to numeric format using `LabelEncoder`.
Dealing with class imbalance: A targeted undersampling strategy was applied. To prevent the model from being biased towards the majority class (benign), the dataset was balanced so that each class was equally represented during training.
Model Architecture: A `RandomForestClassifier` (100 estimators) was trained due to its robustness against overfitting and ability to handle nonlinear relationships in network data.

## Results & Evaluation:
The model achieved very high classification performance on the test set.
Accuracy: ~99.8%
F1-Score: 1.00 across most classes.

## Critical Analysis & Future Work:
While the initial metrics are very good, I acknowledge that in intrusion detection datasets (such as CICIDS-2017) models sometimes unintentionally learn highly correlated identifiers (data leakage) such as IP addresses or exact timestamps, instead of the actual malicious flow patterns.

## My roadmap for future research and improvement includes:
Feature Selection: Using feature importance tracking and SHAP values ​​to isolate the most common network features (e.g., flow duration, packet size) and exclude potentially leaked metadata.
Improved Resampling: Using SMOTE (Synthetic Minority Over-Sampling Technique) instead of undersampling to retain more innocent data when synthesizing minority attack classes.

## Research Significance:
This project explores how machine learning can enhance modern network security systems by identifying malicious traffic patterns automatically. The work also highlights important research challenges such as data leakage, class imbalance, and generalization in cybersecurity datasets.

## Technologies Used:
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- PyArrow

## Project Structure

```
NIDS-ML-Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── models/
├── images/
├── requirements.txt
├── README.md
└── train_model.py
```

---



## 📊 Visualizations

Add your model results here:

### Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)

### Pipeline Diagram
![Pipeline](images/pipeline.png)

### Feature Importance
![Feature Importance](images/feature_importance.png)


## Dataset Source

- CICIDS-style network traffic dataset: (
    "Benign-Monday-no-metadata.parquet",
    "Botnet-Friday-no-metadata.parquet",
    "Bruteforce-Tuesday-no-metadata.parquet",
    "DDoS-Friday-no-metadata.parquet"
  )

## Author

This project is developed for academic and research purposes to explore machine learning applications in cybersecurity.
