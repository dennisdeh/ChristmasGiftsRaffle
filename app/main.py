import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="PIN Lookup", layout="centered")

# Simple mapping dict
d = {
    123456: "this is a message",
    111111: "hello there",
    222222: "another message",
    # ... add more mappings here
}

st.title("Enter Your 6‑Digit PIN")

pin_input = st.text_input("PIN (6 digits)", max_chars=6, help="Enter numbers only, e.g., 123456")

# Validate and display result
if st.button("Submit"):
    if not pin_input.isdigit() or len(pin_input) != 6:
        st.error("Please enter a valid 6-digit numeric PIN.")
    else:
        pin = int(pin_input)
        if pin in d:
            st.success(d[pin])
        else:
            st.error("PIN not found. Please check and try again.")