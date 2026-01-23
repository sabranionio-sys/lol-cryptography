import streamlit as st
import math
import base64
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Hextech Cryptography - League of Legends",
    page_icon="⚔️",
    layout="wide"
)

# --- FUNGSI ASSET ---
@st.cache_data # Cache agar file hanya dibaca sekali untuk mencegah delay
def get_base64(bin_file):
    try:
        if os.path.exists(bin_file):
            with open(bin_file, 'rb') as f:
                data = f.read()
            return base64.b64encode(data).decode()
    except Exception:
        return ""
    return ""

# PRE-LOAD ASSETS (Memuat semua file ke memori di awal)
VIDEO_DEFAULT = get_base64('my_video.mp4')
VIDEO_FAKER = get_base64('faker_video.mp4')
AUDIO_FAKER = get_base64('faker_voice.mp3')
BG_IMG = get_base64('bg.png')

def set_page_background():
    if BG_IMG:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{BG_IMG}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(1, 10, 19, 0.7);
            z-index: -1;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

set_page_background()

# --- CSS KHUSUS TAMPILAN ---
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
    .result-box {
        background-color: rgba(10, 50, 60, 0.8);
        border: 2px solid #c8aa6e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(200, 170, 110, 0.3);
        margin-top: 15px;
    }
    .circle-video {
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #c8aa6e;
        box-shadow: 0px 0px 25px rgba(200, 170, 110, 0.6);
        background-color: #010a13; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA KRIPTOGRAFI ---
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

crypto = LOLCryptography()

# --- HEADER & VIDEO ATAS ---
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 2, 1])
with col_logo_2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d8/League_of_Legends_2019_vector.svg", use_column_width=True)

st.markdown("### 🛡️ Hextech Cryptography Terminal")
st.markdown("<p class='header-text'>Gunakan kekuatan Champion untuk menyembunyikan pesan rahasiamu.</p>", unsafe_allow_html=True)

st.markdown("---")
vid_cols = st.columns(4)
vids = ["https://youtu.be/fX08jvwW-AY", "https://youtu.be/ePVscH1Yi3s", "https://youtu.be/S3F9CpeiSNE", "https://youtu.be/bDMqoIq1kjo"]
for i, col in enumerate(vid_cols):
    with col:
        st.video(vids[i])

st.markdown("<br>", unsafe_allow_html=True)

# --- FUNGSI RENDER KOMBINASI VIDEO & AUDIO ---
def render_faker_special():
    # Merender Video dan Audio secara bersamaan dalam satu blok HTML
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; padding: 10px;">
            <video key="faker_vid" width="380" height="380" autoplay loop muted playsinline class="circle-video">
                <source src="data:video/mp4;base64,{VIDEO_FAKER}" type="video/mp4">
            </video>
            <audio autoplay>
                <source src="data:audio/mp3;base64,{AUDIO_FAKER}" type="audio/mp3">
            </audio>
        </div>
    """, unsafe_allow_html=True)

def render_default_video():
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; padding: 10px;">
            <video key="default_vid" width="380" height="380" autoplay loop muted playsinline class="circle-video">
                <source src="data:video/mp4;base64,{VIDEO_DEFAULT}" type="video/mp4">
            </video>
        </div>
    """, unsafe_allow_html=True)

# --- TAB UTAMA ---
tab1, tab2 = st.tabs(["🔒 ENCODE MESSAGE", "🔓 DECODE CIPHER"])

with tab1:
    col_input, col_vid = st.columns([1.5, 1])
    with col_input:
        plaintext = st.text_input("Plaintext:", placeholder="Masukkan pesan...")
        
        is_faker = plaintext.lower() == "faker"
        if is_faker:
            st.warning("👑 UNKILLABLE DEMON KING DETECTED")

        if plaintext:
            res_bins = []
            for char in plaintext.upper():
                if char == " ": res_bins.append(crypto.SPACE_BINARY)
                elif char in crypto.table_t1:
                    c_code, be = crypto.table_t1[char]
                    h1, h2 = crypto.t2_h1[c_code], crypto.get_h2(be)
                    bin_combined = format(ord(h1)-64, '06b') + format(ord(h2)-64, '06b')
                    res_bins.append(bin_combined)
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.success("Biner Ciphertext:")
            st.code(" ".join(res_bins))
            st.markdown("</div>", unsafe_allow_html=True)
            
    with col_vid:
        if is_faker:
            render_faker_special() # Muncul bersamaan karena data sudah di memori
        else:
            render_default_video()

with tab2:
    col_input_2, col_vid_2 = st.columns([1.5, 1])
    with col_input_2:
        ciphertext = st.text_area("Biner (12-bit per blok):")
        if st.button("MULAI DEKRIPSI"):
            if ciphertext:
                bins = ciphertext.split()
                decoded = ""
                for b in bins:
                    if b == crypto.SPACE_BINARY: decoded += " "
                    elif len(b) == 12:
                        h1_val, h2_val = int(b[:6], 2), int(b[6:], 2)
                        h1_t, h2_t = chr(h1_val + 64), chr(h2_val + 64)
                        for char, (c_code, be) in crypto.table_t1.items():
                            if crypto.t2_h1[c_code] == h1_t and crypto.get_h2(be) == h2_t:
                                decoded += char
                                break
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.info("Pesan Terjemahan:")
                st.header(decoded)
                st.markdown("</div>", unsafe_allow_html=True)
    with col_vid_2:
        render_default_video()
