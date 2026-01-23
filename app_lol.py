import streamlit as st
import math
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Hextech Cryptography Terminal",
    page_icon="🛡️",
    layout="wide"
)

# --- FUNGSI ASSET ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

def set_page_background(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    if bin_str:
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp::before {{
            content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(1, 10, 19, 0.75); z-index: -1;
        }}
        </style>
        """, unsafe_allow_html=True)

set_page_background('bg.jpg') # Pastikan file ini ada di GitHub

# --- CSS KUSTOM ---
st.markdown("""
    <style>
    iframe {
        border-radius: 50% !important; /* Video Lingkaran Sempurna */
        aspect-ratio: 1 / 1;
        border: 3px solid #c8aa6e !important;
    }
    .stButton>button {
        background: linear-gradient(to bottom, #1e2328, #111);
        color: #c8aa6e;
        border: 1px solid #c8aa6e;
        width: 100%;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background: #c8aa6e; color: #1e2328;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAGIAN ATAS: SHOWCASE 4 VIDEO ---
st.markdown("<h3 style='text-align: center; color: #c8aa6e;'>🛡️ Hextech Cryptography Terminal</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #f0e6d2;'>Gunakan kekuatan Champion untuk menyembunyikan pesan rahasiamu.</p>", unsafe_allow_html=True)

ch_cols = st.columns(4)
champs_vids = [
    "https://www.youtube.com/watch?v=fX08jvwW-AY",
    "https://www.youtube.com/watch?v=vzHrjOMfHPY",
    "https://www.youtube.com/watch?v=0h59fTf08S8",
    "https://www.youtube.com/watch?v=TAsX2hGatX0"
]
for i, col in enumerate(ch_cols):
    with col:
        st.video(champs_vids[i]) # Menampilkan 4 video di baris atas

st.markdown("---")

# --- BAGIAN BAWAH: TERMINAL UTAMA ---
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("<h2 style='color: #c8aa6e;'>HEXTECH CRYPTOGRAPHY</h2>", unsafe_allow_html=True)
    st.write("Sembunyikan pesan rahasiamu di balik kekuatan Hextech.")
    
    if 'menu' not in st.session_state:
        st.session_state.menu = 'encode'

    # Tombol Berdampingan
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        if st.button("🔒 ENCODE MESSAGE"): st.session_state.menu = 'encode'
    with b_col2:
        if st.button("🔓 DECODE CIPHER"): st.session_state.menu = 'decode'

with col_right:
    # Video Lingkaran Sempurna di Kanan
    st.video("https://www.youtube.com/watch?v=fX08jvwW-AY")

# --- LOGIKA KRIPTOGRAFI (INPUT & OUTPUT) ---
# (Gunakan class LOLCryptography dari kode sebelumnya di sini)
# ... [Logika Enkripsi/Dekripsi tetap sama seperti sebelumnya] ...
