import streamlit as st
import math
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Hextech Cryptography - League of Legends",
    page_icon="⚔️",
    layout="wide"
)

# --- FUNGSI BACKGROUND & ASSET ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

def set_page_background(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    if bin_str:
        page_bg_img = '''
        <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .stApp::before {
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%%; height: 100%%;
            background-color: rgba(1, 10, 19, 0.7);
            z-index: -1;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Memanggil background (pastikan file bg.jpg ada di GitHub)
set_page_background('bg.jpg')

# --- CSS KUSTOM UNTUK VIDEO LINGKARAN & TOMBOL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Roboto:wght@400&display=swap');
    
    /* Styling Judul */
    .main-title {
        font-family: 'Cinzel', serif;
        color: #c8aa6e;
        font-size: 45px;
        text-align: left;
        margin-bottom: 0px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }
    .sub-title {
        color: #f0e6d2;
        font-family: 'Roboto', sans-serif;
        text-align: left;
        margin-bottom: 30px;
    }

    /* Video Lingkaran Sempurna */
    .video-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    iframe {
        border-radius: 50% !important; /* Membuat lingkaran sempurna */
        aspect-ratio: 1 / 1; /* Memastikan lebar dan tinggi sama */
        border: 4px solid #c8aa6e !important;
        box-shadow: 0px 0px 20px rgba(200, 170, 110, 0.5);
    }

    /* Styling Tombol Kiri */
    .stButton>button {
        background: linear-gradient(to bottom, #1e2328, #111);
        color: #c8aa6e;
        border: 2px solid #c8aa6e;
        padding: 15px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #c8aa6e;
        color: #1e2328;
        box-shadow: 0px 0px 15px #c8aa6e;
    }
    
    /* Kotak Hasil */
    .result-box {
        background-color: rgba(10, 50, 60, 0.8);
        border: 1px solid #0ac8b9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA KRIPTOGRAFI ---
class LOLCryptography:
    def __init__(self):
        self.table_t1 = {
            'A': ('TB', 1575), 'B': ('RC', 2400), 'C': ('NM', 225), 'D': ('NM', 2400),
            'E': ('NA', 675), 'F': ('RS', 2400), 'G': ('TJ', 225), 'H': ('TS', 1575),
            'I': ('RD', 1575), 'J': ('RC', 1234), 'K': ('TS', 2400), 'L': ('NM', 675),
            'M': ('YA', 3150), 'N': ('NA', 1575), 'O': ('DV', 2400), 'P': ('RD', 675),
            'Q': ('NA', 2400), 'R': ('RD', 2400), 'S': ('DV', 675), 'T': ('TS', 225),
            'U': ('TJ', 1575), 'V': ('YA', 1618), 'W': ('RD', 225), 'X': ('YA', 675),
            'Y': ('NM', 3150), 'Z': ('RS', 3150)
        }
        self.t2_h1 = {'NM': 'A', 'RD': 'B', 'NA': 'C', 'TS': 'D', 'YA': 'E', 'RC': 'F', 'RS': 'G', 'TJ': 'H', 'DV': 'I', 'TB': 'J'}
        self.SPACE_BINARY = "000000000000"

    def get_h2(self, be):
        index = math.ceil(be / 200)
        return chr(ord('K') + index - 1)

crypto = LOLCryptography()

# --- LAYOUT UTAMA (KIRI: TEKS & TOMBOL, KANAN: VIDEO LINGKARAN) ---
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown("<p class='main-title'>HEXTECH CRYPTOGRAPHY</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Sembunyikan pesan rahasiamu di balik kekuatan Hextech.</p>", unsafe_allow_html=True)
    
    # Inisialisasi state untuk berpindah menu
    if 'menu' not in st.session_state:
        st.session_state.menu = 'encode'

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("🔒 ENCODE MESSAGE"):
            st.session_state.menu = 'encode'
    with btn_col2:
        if st.button("🔓 DECODE CIPHER"):
            st.session_state.menu = 'decode'

with col_right:
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    # Video YouTube Champion (Dipotong lingkaran via CSS iframe di atas)
    st.video("https://youtu.be/fX08jvwW-AY?si=KrzXVxTOepmyrewO")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- AREA PROSES (MUNCUL DI BAWAH SESUAI TOMBOL YANG DIKLIK) ---
if st.session_state.menu == 'encode':
    st.subheader("Encryption Terminal")
    plaintext = st.text_input("Masukkan Pesan (Huruf A-Z):", placeholder="Contoh: VICTORY")
    if plaintext:
        res_bins = []
        for char in plaintext.upper():
            if char == " ":
                res_bins.append(crypto.SPACE_BINARY)
            elif char in crypto.table_t1:
                c_code, be = crypto.table_t1[char]
                h1, h2 = crypto.t2_h1[c_code], crypto.get_h2(be)
                bin_combined = format(ord(h1)-64, '06b') + format(ord(h2)-64, '06b')
                res_bins.append(bin_combined)
        
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.success("Biner Ciphertext:")
        st.code(" ".join(res_bins))
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.subheader("Decryption Terminal")
    ciphertext = st.text_area("Masukkan Kode Biner (12-bit per blok):")
    if st.button("MULAI DEKRIPSI"):
        if ciphertext:
            bins = ciphertext.split()
            decoded = ""
            for b in bins:
                if b == crypto.SPACE_BINARY:
                    decoded += " "
                elif len(b) == 12:
                    h1_t = chr(int(b[:6], 2) + 64)
                    h2_t = chr(int(b[6:], 2) + 64)
                    for char, (c_code, be) in crypto.table_t1.items():
                        if crypto.t2_h1[c_code] == h1_t and crypto.get_h2(be) == h2_t:
                            decoded += char
                            break
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.info("Pesan Terjemahan:")
            st.header(decoded)
            st.markdown("</div>", unsafe_allow_html=True)
