import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Central Migration Tool", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Data Migration", "Validation", "Variance Monitoring"])

if page == "Data Migration":
    st.header("🚀 Data Migration")

    st.subheader("Foundation Object")
    st.file_uploader("Upload Foundation Object File", type=["csv", "xlsx"])

    st.subheader("Position Object")
    st.file_uploader("Upload Position Object File", type=["csv", "xlsx"])

    st.subheader("Employee Object")
    st.file_uploader("Upload Employee Object File", type=["csv", "xlsx"])

    st.subheader("EC Payroll")
    st.file_uploader("Upload Payroll Data", type=["csv", "xlsx"])

    st.subheader("EC Time & Attendance")
    st.file_uploader("Upload Time & Attendance File", type=["csv", "xlsx"])

elif page == "Validation":
    st.header("✅ Validation")
    st.info("Upload migrated data and validation rules.")

    rules_file = st.file_uploader("Upload Validation Rules (CSV/JSON)", type=["csv", "json"])
    data_file = st.file_uploader("Upload Migrated Data", type=["csv", "xlsx"])

    if st.button("Run Validation"):
        st.success("Validation complete. Display results here.")

elif page == "Variance Monitoring":
    st.header("📊 Variance Monitoring")
    
    source = st.file_uploader("Upload SAP ECC Extract", type=["csv", "xlsx"])
    target = st.file_uploader("Upload SAP SF Data", type=["csv", "xlsx"])

    if st.button("Run Variance Check"):
        st.success("Variance check complete. Display comparison here.")
