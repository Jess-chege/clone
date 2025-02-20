import streamlit as st
import random
import time

# Simulated user database (for Streamlit app)
users_db = {}

# Simulate User Registration
def register_user(name, phone_number):
    user_id = random.randint(1000, 9999)
    users_db[user_id] = {"name": name, "phone_number": phone_number, "balance": 0}
    return user_id

# Simulate a Cash Deposit Request
def request_cash_pickup(user_id, amount):
    if user_id not in users_db:
        return "User not found!"
   
    user = users_db[user_id]
    time.sleep(2)  # Simulate time delay
    return confirm_pickup(user_id, amount)

# Admin/Agent Confirms Pickup
def confirm_pickup(user_id, amount):
    success = random.choice([True, False])  # Randomly decide if the pickup is successful
    if success:
        return deposit_cash(user_id, amount)
    else:
        return "Pickup failed. Please try again later."

# Simulate the cash deposit
def deposit_cash(user_id, amount):
    user = users_db[user_id]
    user['balance'] += amount
    return f"Cash deposit successful! {user['name']} has received KSh {amount}. New balance: KSh {user['balance']}."

# Streamlit App Interface
def main():
    st.title("M-Pesa Home Deposit Service")
    st.sidebar.title("Menu")

    # User Registration Section
    with st.sidebar:
        st.subheader("Register")
        name = st.text_input("Name")
        phone_number = st.text_input("Phone Number")
        if st.button("Register"):
            if name and phone_number:
                user_id = register_user(name, phone_number)
                st.success(f"User {name} registered successfully with ID {user_id}.")
            else:
                st.error("Please fill in both name and phone number.")

    # Cash Pickup Request Section
    st.subheader("Request Cash Pickup")
    if 'user_id' in locals():
        amount_to_deposit = st.number_input("Amount to Deposit", min_value=1, max_value=10000, value=500)
        if st.button("Request Pickup"):
            response = request_cash_pickup(user_id, amount_to_deposit)
            st.info(response)
    else:
        st.warning("Please register first to request a cash pickup.")

# Run the app
if __name__ == "__main__":
    main()

