import streamlit as st

# Set page config
st.set_page_config(page_title="WashLink", page_icon="🚘", layout="centered")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# Simulated pages
def show_home():
    st.title("🚘 WashLink")
    st.subheader("Find Washers near you now")
    if st.button("Get Started"):
        go_to("login")

def show_login():
    st.title("🔐 Sign In")
    st.selectbox("Account Type", ["Customer", "Cleaner"])
    st.text_input("Email Address")
    st.text_input("Password", type="password")
    if st.button("Login"):
        go_to("main_menu")
    st.markdown("Don't have an account?")
    if st.button("Sign Up"):
        go_to("signup")

def show_signup():
    st.title("📝 Sign Up")
    st.text_input("Name")
    st.text_input("Email Address")
    st.text_input("Contact Number")
    st.text_input("Password", type="password")
    if st.button("Create Account"):
        go_to("main_menu")

def show_main_menu():
    st.title("🏠 Home")
    st.write("🚗 No Current Activity")
    st.button("Car Profile", on_click=lambda: go_to("car_profile"))
    st.button("Address Book", on_click=lambda: go_to("address"))
    st.button("Select Time", on_click=lambda: go_to("schedule"))
    st.button("Wash Type", on_click=lambda: go_to("wash_type"))
    st.button("Proceed to Payment", on_click=lambda: go_to("payment"))

def show_address():
    st.title("📍 Address Book")
    st.text_input("Address 1", "12A, Jalan Damai")
    st.text_input("Address 2", "No. 8, Taman Setia")
    if st.button("Save and Go Back"):
        go_to("main_menu")

def show_car_profile():
    st.title("🚘 Car Profile")
    st.text_input("Car Type", "Proton X70")
    st.text_input("Car Plate", "ABC 1234")
    st.text_input("Car Color", "Silver")
    if st.button("Save Car Info"):
        go_to("main_menu")

def show_schedule():
    st.title("🕒 Select Time")
    st.date_input("Pick a date")
    st.time_input("Pick a time")
    if st.button("Save Time"):
        go_to("main_menu")

def show_wash_type():
    st.title("🧼 Choose Wash Type")
    wash = st.radio("Select", ["Basic", "Deluxe", "Full Detailing"])
    st.success(f"{wash} selected")
    if st.button("Save & Back"):
        go_to("main_menu")

def show_payment():
    st.title("💳 Payment")
    st.write("Car Profile: Proton X70")
    st.write("Wash Type: Deluxe")
    st.write("Location: 12A, Jalan Damai")
    st.radio("Payment Method", ["QR Payment", "Online Banking (FPX)", "Cash"])
    if st.button("Proceed to Booking"):
        go_to("processing")

def show_processing():
    st.title("🔎 Searching For Washers...")
    st.info("Searching based on your booking...")
    if st.button("Simulate Match"):
        go_to("complete")

def show_complete():
    st.title("✅ Wash Complete")
    st.success("Thank you for using WashLink!")
    if st.button("Finish"):
        go_to("rating")

def show_rating():
    st.title("🌟 Rate Your Washer")
    st.slider("Rating", 1, 5, 4)
    st.text_area("Review")
    if st.button("Submit Review"):
        st.success("Thank you for your feedback!")
        go_to("main_menu")

# Routing system
pages = {
    "home": show_home,
    "login": show_login,
    "signup": show_signup,
    "main_menu": show_main_menu,
    "address": show_address,
    "car_profile": show_car_profile,
    "schedule": show_schedule,
    "wash_type": show_wash_type,
    "payment": show_payment,
    "processing": show_processing,
    "complete": show_complete,
    "rating": show_rating,
}

# Run the selected page
pages[st.session_state.page]()
