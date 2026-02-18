import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Proposta Speciale 🍕", page_icon="🍕")

# Funzione per caricare le animazioni da LottieFiles
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Carichiamo l'animazione della pizza (Link testato e funzionante)
lottie_pizza = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_j9Y0Zl.json")

# 2. GESTIONE DELLO STATO (Per non far sparire tutto al click)
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def click_button():
    st.session_state.button_clicked = True

# --- INTERFACCIA UTENTE ---

st.title("Ehilà! Ho un messaggio per te... 💌")

if not st.session_state.button_clicked:
    # Schermata iniziale
    st.write("Clicca sul pulsante qui sotto per scoprire di cosa si tratta!")
    st.button("Clicca qui! 🍕", on_click=click_button)
else:
    # Schermata dopo il click
    
    # Creiamo dei contenitori separati per evitare errori di rendering nel browser
    container_pizza = st.container()
    container_testo = st.empty()
    
    # Mostriamo la pizza in alto
    with container_pizza:
        if lottie_pizza:
            st_lottie(lottie_pizza, height=300, key="pizza_animation")
        else:
            st.write("🍕 (Immagina una pizza deliziosa qui!)")

    # Effetto scrittura a macchina per il testo
    testo_finale = "Stasera ordiniamo una bella pizza? 🍕"
    scrittura = ""
    
    for carattere in testo_finale:
        scrittura += carattere
        container_testo.subheader(scrittura)
        time.sleep(0.06) # Velocità della "macchina da scrivere"

    # Pioggia di palloncini finale
    st.balloons()
    
    # Bonus: Scelta del gusto
    st.write("---")
    scelta = st.selectbox("Quale gusto preferisci?", 
                          ["Margherita", "Diavola", "Bufala", "Crostino", "Scegli tu, mi fido!"])
    
    if st.button("Conferma Scelta! ✅"):
        st.success(f"Ottimo! Allora aggiudicato: {scelta}! 🚀")
