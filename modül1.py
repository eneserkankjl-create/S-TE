import streamlit as st
import time
import random

# Custom kalp yağmuru efekti (Premium versiyon)
def rain_hearts():
    heart_css = """
    <style>
    .heart-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 999999;
    }
    .heart-emoji {
        position: absolute;
        top: -10%;
        animation: fall linear forwards;
        text-shadow: 0 0 10px rgba(255,0,0,0.5);
    }
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg) scale(1); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg) scale(1.5); opacity: 0; }
    }
    </style>
    <div class="heart-container">
    """
    for _ in range(60):
        left = random.randint(0, 100)
        delay = random.uniform(0, 1.5)
        duration = random.uniform(2.5, 5)
        size = random.uniform(1.2, 3.5)
        heart_css += f'<div class="heart-emoji" style="left: {left}vw; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}rem;">❤️</div>'
    heart_css += "</div>"
    st.markdown(heart_css, unsafe_allow_html=True)

# Sayfa ayarları
st.set_page_config(page_title="Seni Çok Seviyorum Ece", page_icon="❤️", layout="centered")

# PREMIUM CSS: Google Fonts, Glassmorphism, Kalpli Pattern
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap');

    /* Özel Kalpli ve Soft Arka Plan */
    .stApp {
        background-color: #fff0f5;
        background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 45.5L11.2 26.7C7.3 22.8 7.3 16.5 11.2 12.6C15.1 8.7 21.4 8.7 25.3 12.6L30 17.3L34.7 12.6C38.6 8.7 44.9 8.7 48.8 12.6C52.7 16.5 52.7 22.8 48.8 26.7L30 45.5Z' fill='%23ffb6c1' fill-opacity='0.25' fill-rule='evenodd'/%3E%3C/svg%3E"), 
        linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
        background-attachment: fixed;
    }

    /* Ana İçerik Kutusu (Glassmorphism) - Okunabilirliği %100 Yapar */
    .block-container {
        background: rgba(255, 255, 255, 0.90) !important; /* Yazıların arkasını belirginleştirdik */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 3rem !important;
        box-shadow: 0 10px 40px rgba(255, 182, 193, 0.6);
        border: 2px solid rgba(255, 255, 255, 1);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* Font Ayarları */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #900C3F !important; /* Premium Bordo/Kırmızı */
        text-align: center;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }
    
    p, li, .stMarkdown {
        font-family: 'Montserrat', sans-serif !important;
        color: #2C3E50 !important;
        font-size: 1.1rem;
        line-height: 1.8;
    }

    /* Gizlemeler ve iPhone uyumlu Animasyonlar */
    [data-testid="stSidebar"], [data-testid="collapsedControl"], header { display: none !important; }
    
    /* Sayfa açılışında yumuşakça belirme efekti (Her telefonda çalışır) */
    .block-container {
        animation: fade-in-up 1.2s ease-out forwards;
    }
    
    @keyframes fade-in-up {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .spacer { height: 60px; } /* Ara boşlukları ideal seviyeye çektik */

    /* Buton Tasarımı - Premium & Glowing */
    .stButton>button {
        background: linear-gradient(45deg, #ff0844 0%, #ffb199 100%);
        color: white !important;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 1.3rem !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600;
        box-shadow: 0 10px 20px rgba(255, 8, 68, 0.3);
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto;
        animation: pulse 2s infinite;
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 25px rgba(255, 8, 68, 0.5);
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 8, 68, 0.4); }
        70% { box-shadow: 0 0 0 20px rgba(255, 8, 68, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 8, 68, 0); }
    }

    /* Info ve Warning kutuları uyumu */
    .stAlert {
        border-radius: 15px !important;
        border: none !important;
        background: rgba(255, 255, 255, 0.8) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
</style>
""", unsafe_allow_html=True)

# ANA BAŞLIK
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1>Dünyanın En Güzel Kadınına... 🌹</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; font-size: 1.2rem; color: #7f8c8d;'>Lütfen beni affet sevgilim, çünkü sensiz aldığım nefesin bile bir anlamı yok.</p>", unsafe_allow_html=True)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 1
st.header("Seni Her Şeyden Çok Seven O Çocuk")
st.write("Belki bazen seni kızdıran, saçmalayan, düşüncesizlik eden o şapşal adamım...")
st.write("Ama aynı zamanda;")
st.write("✨ Gözlerinin içine bakarken dünyanın durduğunu hisseden,")
st.write("✨ Senin bir gülüşünle bütün dertlerini unutan,")
st.write("✨ Hayatının geri kalanını sadece seninle, senin ellerini tutarak geçirmek isteyen o aşığım.")
st.info("Hatam ne olursa olsun, kalbimde senden başka hiçbir doğru yok. ❤️")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 2
st.header("Sensiz Bir Saniye Bile Geçmiyor")
st.write("Çünkü biz birbirimiz için yaratıldık. İki yarım elma değil, tam bir dünya olduk seninle.")
st.write("Sen bana küstüğünde renkler soluyor, gün aydınlanmıyor. Yaptığım eşşeklik için senden binlerce kez özür dilerim. Söz veriyorum, seni bir daha asla böyle üzmeyeceğim.")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 3
st.header("Sonsuzluğumuz: Geleceğimiz")
st.write("Çünkü ben sabahları gözümü açtığımda ilk senin o güzel yüzünü görmek istiyorum.")
st.write("Çünkü ben yorucu bir günün ardından eve geldiğimde 'hoş geldin' diyen sesinle huzur bulmak istiyorum.")
st.write("Seninle yaşlanmak, beraber çocuklarımızı sevmek, saçlarımıza aklar düştüğünde bile el ele yürümek istiyorum.")
st.warning("Bu bir tekliften daha fazlası; bu sana adanmış bir ömrün sözüdür. ♾️")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 4
st.header("Artılarımız ve Eksilerimiz")
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='font-size: 1.5rem; text-align: left;'>✨ Artılarımız</h3>", unsafe_allow_html=True)
    st.write("❤️ Dünyanın en güzel aşkını yaşamamız")
    st.write("🫂 Saatlerce birbirimize sarılıp susabilmemiz")
    st.write("😂 Beraberken çocuk gibi eğlenebilmemiz")
    st.write("🧿 Birbirimizin eksiklerini sevgiyle tamamlamamız")
with col2:
    st.markdown("<h3 style='font-size: 1.5rem; text-align: left;'>🥀 Eksilerimiz</h3>", unsafe_allow_html=True)
    st.write("💔 Benim bazen seni istemeden de olsa kırmam")
    st.write("⏳ Sensiz geçen, boşa harcanmış her saniye")
    st.write("😔 Şu an yanımda olamaman ve sana sarılamamam...")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 5
st.header("Birlikte Yazdığımız Masal")
st.write("Şu fotoğraflara bak... Biz yan yanayken o kadar güzeliz ki, hiçbir şeyin bunu bozmasına izin veremem.")

try:
    st.image("foto1.jpg", caption="Gözlerine bakmaya doyamadığım o an...", use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image("foto2.jpg", caption="İyi ki varsın, iyi ki benimsin.", use_column_width=True)
except:
    st.error("Biriciğim, fotoğraflarımız şu an yükleniyor (Sevgilin fotoğrafları siteye eklemeyi unutmuş olabilir ama kalbine kazıdığı kesin).")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# FİNAL BÖLÜMÜ - BUTON EN ALTTA
st.markdown("<h2 style='font-size: 2.5rem; color: #ff0844 !important;'>Tüm Bunların Işığında...</h2>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Lütfen o güzel kalbinle beni affeder misin?</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Ortalanmış büyük buton container'ı
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("Seni Affettim Sevgilim ❤️", use_container_width=True):
        rain_hearts()
        st.success("Dünyalar benim oldu! Seni her şeyden, herkesten çok seviyorum! İyi ki varsın... 🥰")

st.markdown("<br><br><br><br>", unsafe_allow_html=True)
