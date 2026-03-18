import streamlit as st
import pandas as pd
import pickle
import io
import collections

# Load model + columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# UI Title
st.title("🔐 Intrusion Detection System")
st.write("Upload NSL-KDD formatted CSV/TXT file to detect Normal or Attack")

# File upload
uploaded_file = st.file_uploader("Upload file", type=["csv", "txt"])

if uploaded_file is not None:
    try:
        # Read file safely
        file_bytes = uploaded_file.read()
        data = pd.read_csv(io.StringIO(file_bytes.decode('latin-1')), header=None)

        st.success("File loaded successfully ✅")

        # Show sample data
        st.write("### 📄 Sample Data:")
        st.dataframe(data.head())

        # ---------------- PREPROCESSING ----------------
        data = data.iloc[:, :-1]  # remove difficulty column
        data.rename(columns={data.columns[-1]: "label"}, inplace=True)

        # Convert label
        data['label'] = data['label'].apply(lambda x: 0 if x == "normal" else 1)

        # Encoding
        data = pd.get_dummies(data)
        data.columns = data.columns.astype(str)

        # Align features with training
        data = data.reindex(columns=columns, fill_value=0)

        X = data

        # ---------------- PREDICTION ----------------
        predictions = model.predict(X)

        # Convert output
        result = ["Normal" if i == 0 else "Attack" for i in predictions]

        # ---------------- OUTPUT ----------------
        st.success("Prediction completed successfully 🚀")

        # Summary
        count = collections.Counter(result)

        st.write("### 🔍 Summary:")
        st.write(f"🟢 Normal: {count.get('Normal', 0)}")
        st.write(f"🔴 Attack: {count.get('Attack', 0)}")

        # Sample predictions
        st.write("### 📊 Sample Predictions:")
        st.write(result[:20])

    except Exception as e:
        st.error("Error processing file ❌")
        st.write(e)