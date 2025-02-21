import streamlit as st

st.title("Home Page 🏠")
st.write("Welcome to the main page!")

st.sidebar.page_link("pages/deposit.py", label="Go to deposit")
#st.sidebar.page_link("pages/page2.py", label="Go to Page 2")


# Custom CSS for Styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .main-title {
        text-align: center;
        color: #4CAF50;
        font-size: 30px;
        font-weight: bold;
    }
    .balance-box {
        background: #fff;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #333;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .btn-custom {
        background-color: #4CAF50;
        color: white;
        padding: 8px 15px;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
    }
    .btn-custom:hover {
        background-color: #388E3C;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "balance" not in st.session_state:
    st.session_state.balance = 15000  # Initial balance

# Display Title
st.markdown('<h1 class="main-title">💰 Mpesa-Clone Interface 💳</h1>', unsafe_allow_html=True)

# Display Current Balance
st.markdown(f'<div class="balance-box">Current Balance: <br> <span style="color: #4CAF50;">KES {st.session_state.balance}</span></div>', unsafe_allow_html=True)

st.write("")  # Spacer

# Create Layout with Columns
col1, col2 = st.columns(2)

# Deposit Section
with col1:
    st.subheader("Deposit Money")
    deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, step=100.0)
    if st.button("Deposit", key="deposit", help="Click to deposit money"):
        if deposit_amount > 0:
            st.session_state.balance += deposit_amount
            st.success(f"You have deposited KES {deposit_amount}. Your new balance is: KES {st.session_state.balance}")
        else:
            st.error("Invalid deposit amount.")

# Withdraw Section
with col2:
    st.subheader("Withdraw Money")
    withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=100.0)
    if st.button("Withdraw", key="withdraw", help="Click to withdraw money"):
        if 0 < withdraw_amount <= st.session_state.balance:
            st.session_state.balance -= withdraw_amount
            st.success(f"You have withdrawn KES {withdraw_amount}. Your remaining balance is: KES {st.session_state.balance}")
        else:
            st.error("Invalid withdrawal amount or insufficient funds.")

# Display Updated Balance
st.markdown(f'<div class="balance-box">Updated Balance: <br> <span style="color: #4CAF50;">KES {st.session_state.balance}</span></div>', unsafe_allow_html=True)
