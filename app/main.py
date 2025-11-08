import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(0)
np.random.randint(10000000)


st.set_page_config(page_title="Julegaver 2025", layout="centered")

# Simple mapping dict
d = {
    "08325804": "Dennis",
    "14844050": "Marie",
    "02215104": "Lone",
    "51507699": "Palle",
    "06739698": "Michael",
    "58534601": "Kim",
    "76044169": "Jacob",
    "82220403": "Lisa",
}
# output:
ls_out =list(d.values())
np.random.shuffle(ls_out)
d_out = dict(zip(d.keys(),ls_out))

st.title("Indtast dit 8‑ciffer PIN for at se hvem du skal købe gaver til!")
st.markdown("Ho-ho-ho")

pin_input = st.text_input("PIN (8 chiffre)", max_chars=8, help="Indtast kun tal, fx 12345678")

# Validate and display result
if st.button("Send"):
    if not pin_input.isdigit() or len(pin_input) != 8:
        st.error("Du skal indtast et 8-cifre PIN.")
    else:
        pin = str(pin_input)
        if pin in d:
            st.success(d_out[pin])
        else:
            st.error("PIN kode ikke fundet, check igen eller ring til Dennis")