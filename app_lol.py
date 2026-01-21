import streamlit as st
import math

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="LOL Champion Cryptography", 
    page_icon="⚔️", 
    layout="centered"
)

# --- CSS KUSTOM UNTUK DEKORASI ---
# Menggunakan tema Hextech: Biru Gelap, Emas, dan Efek Glow
st.markdown("""
    <style>
    .main {
        background-color: #010a13;
        color: #cdbe91;
    }
    .stApp {
        background: linear-gradient(rgba(1, 10, 19, 0.8), rgba(1, 10, 19, 0.8)), 
                    url("https://images.contentstack.io/v3/assets/blt731eb9a2ad37914/blt8094892591636c0d/6196ecf73449331139f4007d/LoL_Social_Share.jpg");
        background-size: cover;
    }
    h1, h2, h3 {
        color: #f0e6d2 !important;
        text-shadow: 2px 2px #0a323c;
        font-family: 'Beaufort for LoL', serif;
    }
    .stButton>button {
        background-color: #1e2328;
        color: #cdbe91;
        border: 2px solid #785a28;
        border-radius: 0px;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #32281e;
        border-color: #c89b3c;
        color: #f0e6d2;
    }
    .stTextInput>div>div>input {
        background-color: #1e2328;
        color: #f0e6d2;
        border: 1px solid #785a28;
    }
    .stTabs [data-baseweb="tab"] {
        color: #a09b8c;
    }
    .stTabs [aria-selected="true"] {
        color: #c8aa6e !important;
        border-bottom-color: #c8aa6e !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA CORE ---
class LOLChampionCryptography:
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
        temp = n
        for w in weights:
            if temp >= w:
                res += "1"
                temp -= w
            else:
                res += "0"
        return res

    def from_6bit_bin(self, b):
        weights = [32, 16, 8, 4, 2, 1]
        total = 0
        for i in range(len(b)):
            if b[i] == '1':
                total += weights[i]
        return total

crypto = LOLChampionCryptography()

# --- TAMPILAN HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/commons/d/d8/League_of_Legends_2019_vector.svg", width=300)
st.title("🛡️ Hextech Cryptography")
st.write("Sembunyikan pesanmu di balik kode rahasia para Champion League of Legends.")

# --- TAMPILAN TAB ---
tab1, tab2 = st.tabs(["🔒 Encode Message", "🔓 Decode Cipher"])

with tab1:
    st.markdown("### Enkripsi Karakter ke 12-Bit")
    input_text = st.text_input("Plaintext:", placeholder="CONTOH: AKU KAYA").upper()
    
    if input_text:
        final_bins = []
        st.info("🔄 Proses Konversi Hextech...")
        
        cols = st.columns(len(input_text) if len(input_text) > 0 else 1)
        for i, char in enumerate(input_text):
            if char == " ":
                final_bins.append(crypto.SPACE_BINARY)
                st.write("🌌 Spasi terdeteksi")
            elif char in crypto.table_t1:
                c_code, be = crypto.table_t1[char]
                h1 = crypto.t2_h1[c_code]
                h2 = crypto.get_h2(be)
                bin_h1 = crypto.to_6bit_bin(ord(h1)-64)
                bin_h2 = crypto.to_6bit_bin(ord(h2)-64)
                combined = bin_h1 + bin_h2
                final_bins.append(combined)
                st.markdown(f"**{char}** : `{combined}`")
        
        hasil = " ".join(final_bins)
        st.subheader("Biner Ciphertext:")
        st.code(hasil, language="text")

with tab2:
    st.markdown("### Deskripsi 12-Bit ke Karakter")
    input_bin = st.text_area("Ciphertext (Biner):", placeholder="000011010010...")
    
    if st.button("RUN DECODER"):
        if input_bin:
            bins = input_bin.split()
            decoded_text = []
            
            for b in bins:
                if b == crypto.SPACE_BINARY:
                    decoded_text.append(" ")
                    continue
                
                if len(b) == 12:
                    val_h1 = crypto.from_6bit_bin(b[:6])
                    val_h2 = crypto.from_6bit_bin(b[6:])
                    h1_t = chr(val_h1 + 64)
                    h2_t = chr(val_h2 + 64)
                    
                    found = "?"
                    for char, (c_code, be) in crypto.table_t1.items():
                        if crypto.t2_h1[c_code] == h1_t and crypto.get_h2(be) == h2_t:
                            found = char
                            break
                    decoded_text.append(found)
                else:
                    decoded_text.append("?")
            
            st.success("Pesan Terjemahan:")
            st.header("".join(decoded_chars if 'decoded_chars' in locals() else decoded_text))
        else:
            st.error("Masukkan kode biner Hextech!")

st.markdown("---")
st.caption("© 2026 LOL Champion Cryptography Project | Created by Sabranio Widiyanto")


