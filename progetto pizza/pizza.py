import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# 1. Configurazione pagina (Cambiata l'icona in pizza)
st.set_page_config(page_title="Serata Pizza?", page_icon="🍕")

# Funzione per caricare animazioni
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 2. Nuova animazione: Una pizza che balla o viene sfornata
# Ho sostituito il link con uno a tema pizza
lottie_pizza = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_j9Y0Zl.json") 

# --- INTERFACCIA ---
st.title("Ho una proposta per te... 🍕")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def click_button():
    st.session_state.button_clicked = True

# Bottone iniziale
if not st.session_state.button_clicked:
    st.write("Ho una voglia matta di qualcosa di buono...")
    st.button("Cosa mangiamo stasera? 🤔", on_click=click_button)
else:
    # Mostra l'animazione della pizza
    st_lottie(lottie_pizza, height=300, key="pizza_anim")
    
    # Messaggio che appare gradualmente
    placeholder = st.empty()
    # 3. Frase personalizzata per la pizza
    full_text = "Stasera ordiniamo una bella pizza? Scelgo io o scegli tu? 🍕❤️"
    
    displayed_text = ""
    for char in full_text:
        displayed_text += char
        placeholder.subheader(displayed_text)
        time.sleep(0.07) # Leggermente più veloce per non annoiare
    
    # Palloncini finali (puoi anche toglierli se vuoi solo la pizza)
    st.balloons() 
    
    # Un piccolo tocco extra: un selettore per la pizza!
    st.write("---")
    gusto = st.selectbox("Quale prendiamo?", ["Margherita Classica", "Diavola", "Bufala", "Pistacchio e Mortazza", "Quella che vuoi tu!"])
    if st.button("Conferma Ordine! ✅"):
        st.success(f"Ottima scelta! La {gusto} sta già arrivando (nella mia testa)!")