
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# تحميل البيانات
df = pd.read_csv("Indicators_of_Anxiety_or_Depression (3).csv")
df = df[df["Time Period"] >= 11].copy()

# توليد المتغير الهدف
df["Group_Label"] = df["Time Period"].apply(lambda x: 0 if 11 <= x <= 25 else 1)

# تنظيف وترميز
df = df.dropna(subset=["Subgroup", "Value", "Group_Label"])
encoder = LabelEncoder()
df["Subgroup_encoded"] = encoder.fit_transform(df["Subgroup"].astype(str))

# تجهيز البيانات
X = df[["Value", "Subgroup_encoded"]]
y = df["Group_Label"]
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# مقياس البيانات
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# تدريب النموذج
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# حفظ النموذج والأدوات
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoder, "encoder.pkl")
print("✅ Model saved successfully!")
print(df[["Time Period", "Group_Label"]].drop_duplicates().sort_values("Time Period"))
