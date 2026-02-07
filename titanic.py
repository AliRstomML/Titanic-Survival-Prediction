import pandas as pd

# تحميل البيانات
train_data = pd.read_csv("train.csv")

# عرض أول 5 صفوف
print("First 5 rows of Titanic dataset:")
print(train_data.head())

# معلومات عامة
print("\nDataset Info:")
print(train_data.info())

# نسبة الناجين
print("\nSurvival Count:")
print(train_data["Survived"].value_counts())