import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AI Factory Optimization",
    layout="wide"
)

st.title("🏭 AI Factory Optimization Dashboard")

st.markdown(
    "Enterprise AI-powered factory recommendation system"
)

# Sample dashboard data

factory_data = pd.DataFrame({
    "Factory": [
        "Wicked Choccy's",
        "Sugar Shack",
        "Secret Factory",
        "Lot's O' Nuts"
    ],
    "Predicted Lead Time": [
        4.6,
        5.4,
        5.5,
        5.9
    ],
    "Efficiency Score": [
        92,
        81,
        79,
        74
    ]
})

st.subheader("Factory Performance")

st.dataframe(factory_data)

st.subheader("Lead Time Analysis")

st.bar_chart(
    factory_data.set_index("Factory")[
        "Predicted Lead Time"
    ]
)

st.subheader("Efficiency Analysis")

st.line_chart(
    factory_data.set_index("Factory")[
        "Efficiency Score"
    ]
)

selected_factory = st.selectbox(
    "Select Factory",
    factory_data["Factory"]
)

st.success(
    f"Recommended Factory: {selected_factory}"
)