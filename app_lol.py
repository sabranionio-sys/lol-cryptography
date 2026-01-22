import streamlit as st
import math
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Hextech Cryptography - League of Legends",
    page_icon="⚔️",
    layout="wide"
)

# --- FUNGSI UNTUK MERENDER BACKGROUND GAMBAR ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

def set_page_background(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    if bin_str:
        # CSS untuk mengatur gambar latar belakang agar full screen dan tetap (fixed)
        page_bg_img = '''
        <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        
        /* Overlay transparan agar teks tetap kontras dan mudah dibaca */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%%;
            height: 100%%;
            background-color: rgba(1, 10, 19, 0.6); /* Gelapkan background 60%% */
            z-index: -1;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Pastikan file gambar Yasuo yang kamu unggah bernama 'bg.jpg' di repository GitHub
set_page_background('bg.png')

# --- CSS DEKORASI ELEMEN ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    
    h3 {
        font-family: 'Cinzel', serif;
        color: #c8aa6e !important;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(0,0,0,1);
    }

    .header-text {
        text-align: center;
        color: #f0e6d2;
        text-shadow: 1px 1px 5px rgba(0,0,0,1);
    }

    /* Gaya Kotak Hasil agar terlihat seperti UI Hextech */
    .result-box {
        background-color: rgba(10, 50, 60, 0.8);
        border: 2px solid #c8aa6e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(200, 170, 110, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- KODE LOGIKA & HEADER (SAMA SEPERTI SEBELUMNYA) ---
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
        self.t2_h1 = {'NM': 'A', 'RD': 'B', 'NA': 'C', 'TS': 'D', 'YA': 'E', 'RC': 'F', 'RS': 'G', 'TJ': 'H', 'DV': 'I', 'TB': 'J'}
        self.SPACE_BINARY = "000000000000"

    def get_h2(self, be):
        index = math.ceil(be / 200)
        return chr(ord('K') + index - 1)

    def to_6bit_bin(self, n):
        return format(n, '06b')

    def from_6bit_bin(self, b):
        return int(b, 2)

crypto = LOLCryptography()

# Layout Header Simetris
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d8/League_of_Legends_2019_vector.svg", use_column_width=True)

st.markdown("### 🛡️ Hextech Cryptography Terminal")
st.markdown("<p class='header-text'>Gunakan kekuatan Champion untuk menyembunyikan pesan rahasiamu.</p>", unsafe_allow_html=True)

# Showcase Champions
st.markdown("---")
ch_cols = st.columns(4)
champs = [
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vi_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Caitlyn_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ekko_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg"
]
for i, col in enumerate(ch_cols):
    col.image(champs[i], use_column_width=True)

# Bagian Utama: Tab Enkripsi & Deskripsi
tab1, tab2 = st.tabs(["🔒 ENCODE MESSAGE", "🔓 DECODE CIPHER"])

with tab1:
    plaintext = st.text_input("Plaintext:", placeholder="Masukkan pesan...")
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
    ciphertext = st.text_area("Biner (12-bit per blok):")
    if st.button("MULAI DEKRIPSI"):
        if ciphertext:
            bins = ciphertext.split()
            decoded = ""
            for b in bins:
                if b == crypto.SPACE_BINARY:
                    decoded += " "
                elif len(b) == 12:
                    h1_val = crypto.from_6bit_bin(b[:6])
                    h2_val = crypto.from_6bit_bin(b[6:])
                    h1_t, h2_t = chr(h1_val + 64), chr(h2_val + 64)
                    for char, (c_code, be) in crypto.table_t1.items():
                        if crypto.t2_h1[c_code] == h1_t and crypto.get_h2(be) == h2_t:
                            decoded += char
                            break
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.info("Pesan Terjemahan:")
            st.header(decoded)
            st.markdown("</div>", unsafe_allow_html=True)






