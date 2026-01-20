import streamlit as st
import math

# --- LOGIKA CORE (Sama dengan sebelumnya) ---
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

# --- INTERFACE WEB (Streamlit) ---
st.set_page_config(page_title="LOL Crypto Web", page_icon="🎮")

st.title("🎮 LOL Champion Cryptography")
st.markdown("Aplikasi web untuk Enkripsi & Deskripsi berbasis data **League of Legends**.")

crypto = LOLChampionCryptography()
tab1, tab2 = st.tabs(["🔐 Enkripsi", "🔓 Deskripsi"])

# --- TAB ENKRIPSI ---
with tab1:
    st.header("Enkripsi Teks ke Biner")
    input_text = st.text_input("Masukkan Teks (Contoh: NIO ARDI)", placeholder="Tulis di sini...")
    
    if input_text:
        final_bins = []
        st.subheader("Detail Proses:")
        
        for char in input_text.upper():
            if char == " ":
                final_bins.append(crypto.SPACE_BINARY)
                st.write(f"**[Spasi]** ➔ `{crypto.SPACE_BINARY}`")
            elif char in crypto.table_t1:
                c_code, be = crypto.table_t1[char]
                h1 = crypto.t2_h1[c_code]
                h2 = crypto.get_h2(be)
                bin_h1 = crypto.to_6bit_bin(ord(h1)-64)
                bin_h2 = crypto.to_6bit_bin(ord(h2)-64)
                combined = bin_h1 + bin_h2
                final_bins.append(combined)
                st.write(f"**{char}** ➔ H1:{h1}, H2:{h2} ➔ `{combined}`")
        
        hasil = " ".join(final_bins)
        st.success("Hasil Biner Akhir:")
        st.code(hasil)

# --- TAB DESKRIPSI ---
with tab2:
    st.header("Deskripsi Biner ke Teks")
    input_bin = st.text_area("Masukkan Kode Biner (Pisahkan tiap blok dengan spasi)", placeholder="000011010010 ...")
    
    if st.button("Proses Deskripsi"):
        if input_bin:
            bins = input_bin.split()
            decoded_chars = []
            
            for b in bins:
                if b == crypto.SPACE_BINARY:
                    decoded_chars.append(" ")
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
                    decoded_chars.append(found)
                else:
                    decoded_chars.append("[Error: Bukan 12-bit]")
            
            st.info("Hasil Teks Asli:")
            st.subheader("".join(decoded_chars))
        else:
            st.warning("Masukkan kode biner terlebih dahulu!")