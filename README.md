# 📢 Poland Bankruptcy Prediction

* This project focuses on predicting which companies in Poland are at risk of bankruptcy using machine learning classification models. It leverages data balancing techniques and model tuning to build a robust predictive pipeline capable of handling highly imbalanced datasets.


---

# 📦 Project Overview

* Goal: Predict company bankruptcy risk in Poland

* Problem Type: Binary Classification (Bankrupt vs. Not Bankrupt)

* Challenge: Highly imbalanced dataset (~95% non-bankrupt, ~5% bankrupt)



---

# 🛠️ Tools & Libraries

* Data Manipulation: pandas, numpy

* Visualization: matplotlib, seaborn

* Modeling: scikit-learn (DecisionTreeClassifier, RandomForestClassifier)

* Imbalanced Data Handling: imblearn (OverSampling, UnderSampling)

* Model Tuning: GridSearchCV, cross_val_score

* Dashboard: ipywidgets (for interactive tuning of precision/recall)



---

# 🧪 Data Handling & Preprocessing

* ⚖️ Addressing Imbalanced Classes

* The dataset was severely imbalanced, with:

* 95% of companies labeled as Not Bankrupt

* 5% labeled as Bankrupt



**Techniques Applied:**

**Oversampling:**

* Increased the number of samples in the minority (bankrupt) class to match the majority class.


**Undersampling:**

* Reduced the number of samples in the majority (non-bankrupt) class to match the minority class.



* Both approaches were tested to evaluate their effectiveness.


---

# 🤖 Model Development

**1️⃣ Decision Tree Classifier**

* Trained on three variations of the dataset:

* Original (Imbalanced)

* Oversampled

* Undersampled


**Results:**

* Oversampled Dataset performed best:

* Training Accuracy: 1.00

* Testing Accuracy: 0.95



* However, the high accuracy alone was not enough—confusion matrix analysis showed that more robust metrics were needed to ensure real-world reliability.

**2️⃣ Random Forest Classifier**

* Trained on the oversampled dataset

* Evaluated with cross-validation, achieving scores in the 0.99 range, indicating strong generalization

* Applied GridSearchCV for hyperparameter tuning, which improved performance even further



---

# 📊 Evaluation Metrics

* Accuracy

* Confusion Matrix

* Cross-Validation Scores

* Precision and Recall tuning (based on business need)



---

# 🧩 Interactive Dashboard

* An interactive dashboard was created using ipywidgets to dynamically adjust the recall vs. precision tradeoff, allowing stakeholders to fine-tune model behavior depending on the cost of false positives vs. false negatives.


---

# ✅ Conclusion

* Oversampling with SMOTE combined with a Random Forest Classifier delivered the best performance on this imbalanced dataset.

* Hyperparameter tuning significantly improved model accuracy and reliability.

* Interactive tools were implemented for flexible model threshold adjustment, supporting real-world business decisions.



---

🙏 Acknowledgments

Thanks for checking out this project! Feedback and collaboration are welcome.

Link: https://poland-bankrupty-predictionw.streamlit.app/



