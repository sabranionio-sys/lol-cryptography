import streamlit as st
import math
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Hextech Cryptography - League of Legends",
    page_icon="⚔️",
    layout="wide"
)

# --- FUNGSI UNTUK MENGAMBIL BACKGROUND LOKAL ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Jika kamu sudah upload file bernama bg.jpg ke GitHub, hapus tanda pagar (#) di bawah ini:
# set_png_as_page_bg('bg.jpg')

# --- CSS KUSTOM DEKORASI HEXTECH ---
st.markdown("""
    <style>
    /* Font & Warna Dasar */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    
    .main {
        color: #f0e6d2;
    }
    
    /* Overlay Gelap agar Teks Terbaca */
    .stApp {
        background: rgba(1, 10, 19, 0.7);
    }

    h1, h2, h3 {
        font-family: 'Cinzel', serif;
        color: #c8aa6e !important;
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }

    /* Kotak Input & Area Teks */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(30, 35, 40, 0.9) !important;
        color: #f0e6d2 !important;
        border: 2px solid #785a28 !important;
        border-radius: 5px;
    }

    /* Dekorasi Tombol Run */
    .stButton>button {
        background: linear-gradient(to bottom, #1e2328, #111);
        color: #c8aa6e;
        border: 2px solid #c8aa6e;
        font-weight: bold;
        width: 100%;
        letter-spacing: 2px;
    }
    
    .stButton>button:hover {
        border-color: #f0e6d2;
        color: #f0e6d2;
        box-shadow: 0px 0px 15px rgba(200, 170, 110, 0.5);
    }

    /* Container Hasil */
    .result-box {
        background-color: rgba(10, 50, 60, 0.6);
        border: 1px solid #0ac8b9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA CORE ---
class LOLCryptography:
    def __init__(self):
        self.table_t1 = {
            'A': ('TB', 1575), 'B': ('RC', 2400), 'C': ('NM', 225),  'D': ('NM', 2400),
            'E': ('NA', 675),  'F': ('RS', 2400), 'G': ('TJ', 225),  'H': ('TS', 1575),
            'I': ('RD', 1575), 'J': ('RC', 1234), 'K': ('TS', 2400), 'L': ('NM', 675),
            'M': ('YA', 3150), 'N': ('NA', 1575), 'O': ('DV', 2400), 'P': ('RD', 675),
            'Q': ('NA', 2400), 'R': ('RD', 2400), 'S': ('DV', 675),  'T': ('TS', 225),
            'U': ('TJ', 1575), 'V': ('YA', 1618), 'W': ('RD', 225),  'X': ('YA', 675),
            'Y': ('NM', 3150), 'Z': ('RS', 3150)
        }
        self.t2_h1 = {
            'NM': 'A', 'RD': 'B', 'NA': 'C', 'TS': 'D', 'YA': 'E',
            'RC': 'F', 'RS': 'G', 'TJ': 'H', 'DV': 'I', 'TB': 'J'
        }
        self.SPACE_BINARY = "000000000000"

    def get_h2(self, be):
        index = math.ceil(be / 200)
        return chr(ord('K') + index - 1)

    def to_6bit_bin(self, n):
        weights = [32, 16, 8, 4, 2, 1]
        res = ""
        for w in weights:
            if n >= w:
                res += "1"
                n -= w
            else:
                res += "0"
        return res

    def from_6bit_bin(self, b):
        weights = [32, 16, 8, 4, 2, 1]
        return sum(weights[i] for i, bit in enumerate(b) if bit == '1')

crypto = LOLCryptography()

# --- HEADER WEB ---
st.markdown("<h1 style='font-size: 50px;'>LEAGUE OF LEGENDS</h1>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/d/d8/League_of_Legends_2019_vector.svg", width=400)
st.markdown("### 🛡️ Hextech Cryptography Terminal")
st.write("<center>Gunakan kekuatan Champion untuk menyembunyikan pesan rahasiamu.</center>", unsafe_allow_html=True)

# --- TAMPILAN Champion Showcase ---
st.markdown("---")
cols = st.columns(4)
champs = [
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vi_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Caitlyn_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ekko_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg"
]
for i, col in enumerate(cols):
    col.image(champs[i], use_column_width=True)

# --- TAB ENKRIPSI & DESKRIPSI ---
tab1, tab2 = st.tabs(["🔒 ENCODE MESSAGE", "🔓 DECODE CIPHER"])

with tab1:
    st.markdown("### 📝 Masukkan Pesan")
    plaintext = st.text_input("Plaintext:", placeholder="CONTOH: NIO ARDI")
    
    if plaintext:
        res_bins = []
        for char in plaintext.upper():
            if char == " ":
                res_bins.append(crypto.SPACE_BINARY)
            elif char in crypto.table_t1:
                c_code, be = crypto.table_t1[char]
                h1, h2 = crypto.t2_h1[c_code], crypto.get_h2(be)
                bin_combined = crypto.to_6bit_bin(ord(h1)-64) + crypto.to_6bit_bin(ord(h2)-64)
                res_bins.append(bin_combined)
        
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.success("Biner Ciphertext:")
        st.code(" ".join(res_bins))
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### 🗝️ Masukkan Kode Biner")
    ciphertext = st.text_area("Biner (12-bit per blok):")
    
    if st.button("MULAI DEKRIPSI"):
        if ciphertext:
            bins = ciphertext.split()
            decoded = ""
            for b in bins:
                if b == crypto.SPACE_BINARY:
                    decoded += " "
                elif len(b) == 12:
                    h1_t = chr(crypto.from_6bit_bin(b[:6]) + 64)
                    h2_t = chr(crypto.from_6bit_bin(b[6:]) + 64)
                    for char, (c_code, be) in crypto.table_t1.items():
                        if crypto.t2_h1[c_code] == h1_t and crypto.get_h2(be) == h2_t:
                            decoded += char
                            break
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.info("Pesan Terjemahan:")
            st.header(decoded)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br><center>© 2026 LOL Champion Cryptography Project | Created by Sabranio Widiyanto</center>", unsafe_allow_html=True)
