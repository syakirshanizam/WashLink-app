import streamlit as st
from datetime import datetime, timedelta

# Title and Header
st.title("🚗 WashLink - Book a Car Wash")
st.markdown("Welcome to **WashLink**, your on-demand car wash booking platform.")

# Step 1: User Info
st.header("1. Customer Information")
name = st.text_input("Full Name")
phone = st.text_input("Phone Number")

# Step 2: Choose Service Package
st.header("2. Select Service Package")
service_options = {
    "Basic Wash - RM20": "Exterior only, quick 20-minute clean",
    "Deluxe Wash - RM35": "Exterior + interior, 40 minutes",
    "Full Detailing - RM70": "Deep clean + wax, up to 90 minutes"
}
service = st.selectbox("Choose a package", list(service_options.keys()))
st.caption(service_options[service])

# Step 3: Select Date and Time
st.header("3. Schedule Booking")
date = st.date_input("Select a date", min_value=datetime.today())
time = st.time_input("Preferred time", value=(datetime.now() + timedelta(hours=1)).time())

# Step 4: Enter Location
st.header("4. Service Location")
location = st.text_area("Enter your car location (e.g. home, office address)")

# Step 5: Confirm Booking
st.header("5. Confirm Your Booking")
if st.button("Confirm Booking"):
    if name and phone and location:
        st.success("✅ Booking Confirmed!")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Phone:** {phone}")
        st.markdown(f"**Service:** {service}")
        st.markdown(f"**Date & Time:** {date} at {time}")
        st.markdown(f"**Location:** {location}")
        st.info("You will receive an SMS confirmation shortly. Thank you for using WashLink!")
    else:
        st.warning("Please complete all required fields.")

# Footer
st.markdown("---")
st.caption("Prototype for WashLink • Streamlit Demo • 2025")
