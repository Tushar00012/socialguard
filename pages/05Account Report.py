import streamlit as st
import os
import pandas as pd
import altair as alt

# Path to the CSV file
csv_file_path = "Accountreport.csv"

# Check if the file exists
if not os.path.exists(csv_file_path):
    st.warning("⚠ No Report Found. Please Start a New Analysis.")

    # Form for requesting a new analysis
    with st.form(key='request_analysis_form'):
        submitted = st.form_submit_button("Request Analysis")
        if submitted:
            st.page_link("pages/01Request_Analysis.py", label="Proceed to Analysis", icon="🔍")

else:
    # Load the CSV file
    df = pd.read_csv(csv_file_path)
    
    st.title("📊 Account Report")
    st.header("Account Analysis Report")
    st.write(df)

    # Multiselect for filtering based on status
    selected_status = st.multiselect(
        "Choose Status to Filter", ["Red", "Green", "Yellow"], default=["Red", "Green"]
    )

    if not selected_status:
        st.error("❌ Please select at least one status.")
    else:
        # Filter data based on the selected statuses
        filtered_data = df[df['Status'].isin(selected_status)]

        st.subheader("🔎 Filtered Data")
        st.write(filtered_data)

        # Prepare data for visualization
        status_counts = filtered_data['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']

        color_scale = alt.Scale(domain=["Red", "Green", "Yellow"], range=["#FF4B4B", "#4CAF50", "#FFD700"])

        # Create and display Altair chart
        chart = (
            alt.Chart(status_counts)
            .mark_bar()
            .encode(
                x=alt.X("Status:N", title="Status"),
                y=alt.Y("Count:Q", title="Count"),
                color=alt.Color("Status:N", scale=color_scale),
                tooltip=["Status", "Count"]
            )
            .properties(title="Status Distribution")
        )

        st.altair_chart(chart, use_container_width=True)

    # Display and save "Red" flagged accounts for termination
    red_data = df[df['Status'] == "Red"]

    if not red_data.empty:
        st.subheader("🚨 Termination Accounts")
        st.write(red_data)

        # Save red accounts to CSV
        terminate_file_path = "terminate.csv"
        red_data.to_csv(terminate_file_path, index=False)
        st.success(f"Red accounts saved to `{terminate_file_path}` ✅")
