import streamlit as st
import numpy as np
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
np.random.seed(0)

st.set_page_config(page_title="Julegaver 2025", layout="centered", page_icon="🎅")

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
st.markdown("""
Her er et lille ChatGPT-genereret juledigt til at varme op på:\n
Under træet lå en pakke, rund og lidt for tung,
nissen grined’ listigt, "det dér blir’ nok en gong!"
Rudolf snublede i sneen, tabte hele læsset,
og julemanden råbte: "Åh nej, hvor er min nissehuesnæsse!"
Men julen kom alligevel – med grin og klejneræsset!\n
Ho-ho-ho
""")

pin_input = st.text_input("Indtast din PIN (8 chiffre)", max_chars=8, help="Indtast kun tal, fx 12345678")

# Validate and display result
if st.button("Send for at se hvem du skal købe til"):
    if not pin_input.isdigit() or len(pin_input) != 8:
        st.error("PIN-koden du har fået er 8 chiffre")
    else:
        pin = str(pin_input)
        if pin in d:
            st.success(f"Du skal give en gave til: {d_out[pin]}")
        else:
            st.error("PIN kode ikke fundet, check igen - eller ring til Dennis")

st.image(os.path.join(BASE_DIR, "christmas_mood.png"))