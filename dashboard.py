import streamlit as st
import snowflake.connector
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Live Sales Dashboard", layout="wide")
st.title("📊 Live Retail Sales Dashboard")
st.markdown("Fetching data directly from **Snowflake Silver Layer**...")

# --- Connect to Snowflake ---
# Uses st.secrets to connect to Snowflake
try:
    ctx = snowflake.connector.connect(**st.secrets["snowflake"])

    # --- Fetch Data ---
    query = "SELECT * FROM SALES_ANALYTICS"
    cur = ctx.cursor()
    cur.execute(query)
    data = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=columns)

    # --- KPI Metrics ---
    total_revenue = df["TOTAL_REVENUE"].sum()
    total_units = df["QUANTITY"].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Total Units Sold", f"{total_units}")

    # --- Visualizations ---
    st.divider()
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Revenue by Product")
        st.bar_chart(df, x="PRODUCT", y="TOTAL_REVENUE")

    with col4:
        st.subheader("Raw Data (Silver Layer)")
        st.dataframe(df)

except Exception as e:
    st.error(f"An error occurred: {e}")
