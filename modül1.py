import streamlit as st
import time
import random

# Custom kalp yağmuru efekti
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
        z-index: 99999;
    }
    .heart-emoji {
        position: absolute;
        top: -10%;
        animation: fall linear forwards;
    }
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <div class="heart-container">
    """
    for _ in range(50):
        left = random.randint(0, 100)
        delay = random.uniform(0, 2)
        duration = random.uniform(3, 6)
        size = random.uniform(1.5, 3)
        heart_css += f'<div class="heart-emoji" style="left: {left}vw; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}rem;">❤️</div>'
    heart_css += "</div>"
    st.markdown(heart_css, unsafe_allow_html=True)

# Sayfa ayarları - Romantik ikon ve başlık
st.set_page_config(page_title="Seni Çok Seviyorum Ece", page_icon="❤️", layout="centered")

# CSS ile sayfayı romantik bir temaya büründürüyoruz (Açık pembe tonlar, yuvarlak butonlar)
st.markdown("""
<style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1, h2, h3 {
        color: #D63384 !important;
        font-family: 'Georgia', serif;
    }
    p, li {
        color: #4A4A4A;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        color: white;
        background-color: #FF4B4B;
        border-radius: 30px;
        border: none;
        padding: 10px 24px;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF1A1A;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .css-1d391kg {
        background-color: #FFE4E1;
    }
</style>
""", unsafe_allow_html=True)

# Ana Başlık
st.markdown("<h1 style='text-align: center;'>Dünyanın En Güzel Kadınına... 🌹</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Lütfen beni affet sevgilim, çünkü sensiz aldığım nefesin bile bir anlamı yok.</p>", unsafe_allow_html=True)

# YENİ EKLENEN KISIM: Sol menüyü gizleme, kaydırma (scroll) animasyonu ve tek sayfa akışı
st.markdown("""
<style>
    /* Sol menüyü ve açma tuşunu tamamen yok ediyoruz */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    header { display: none !important; } /* Üstteki gereksiz boşluğu alır */
    
    /* Aşağı kaydırdıkça elemanların belirmesi (Scroll Reveal Animation) */
    div.element-container {
        animation: fade-in-up 1.2s ease-out both;
        animation-timeline: view();
        animation-range: entry 5% cover 25%;
    }
    
    @keyframes fade-in-up {
        0% { opacity: 0; transform: translateY(120px); filter: blur(4px); }
        100% { opacity: 1; transform: translateY(0); filter: blur(0px); }
    }
    
    /* Bölümler arası uzun boşluklar (Scroll hissini artırmak için) */
    .spacer {
        height: 40vh; /* Ekranın %40'ı kadar boşluk */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 1
st.header("👤 Seni Her Şeyden Çok Seven O Çocuk")
st.write("Belki bazen seni kızdıran, saçmalayan, düşüncesizlik eden o şapşal adamım...")
st.write("Ama aynı zamanda;")
st.write("✨ Gözlerinin içine bakarken dünyanın durduğunu hisseden,")
st.write("✨ Senin bir gülüşünle bütün dertlerini unutan,")
st.write("✨ Hayatının geri kalanını sadece seninle, senin ellerini tutarak geçirmek isteyen o aşığım.")
st.info("Hatam ne olursa olsun, kalbimde senden başka hiçbir doğru yok. ❤️")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 2
st.header("🥺 Sensiz Bir Saniye Bile Geçmiyor")
st.write("Çünkü biz birbirimiz için yaratıldık. İki yarım elma değil, tam bir dünya olduk seninle.")
st.write("Sen bana küstüğünde renkler soluyor, gün aydınlanmıyor. Yaptığım eşşeklik için senden binlerce kez özür dilerim. Söz veriyorum, seni bir daha asla böyle üzmeyeceğim.")

st.write("---")
st.write("Lütfen o güzel kalbinle beni affeder misin?")
if st.button("Seni Affettim Sevgilim ❤️"):
    rain_hearts()
    st.success("Dünyalar benim oldu! Seni her şeyden, herkesten çok seviyorum! İyi ki varsın... 🥰")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 3
st.header("💍 Sonsuzluğumuz: Geleceğimiz")
st.write("Çünkü ben sabahları gözümü açtığımda ilk senin o güzel yüzünü görmek istiyorum.")
st.write("Çünkü ben yorucu bir günün ardından eve geldiğimde 'hoş geldin' diyen sesinle huzur bulmak istiyorum.")
st.write("Seninle yaşlanmak, beraber çocuklarımızı sevmek, saçlarımıza aklar düştüğünde bile el ele yürümek istiyorum.")
st.warning("Bu bir tekliften daha fazlası; bu sana adanmış bir ömrün sözüdür. ♾️")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 4
st.header("💞 Artılarımız ve Eksilerimiz")
col1, col2 = st.columns(2)
with col1:
    st.subheader("✨ Artılarımız")
    st.write("❤️ Dünyanın en güzel aşkını yaşamamız")
    st.write("🫂 Saatlerce birbirimize sarılıp susabilmemiz")
    st.write("😂 Beraberken çocuk gibi eğlenebilmemiz")
    st.write("🧿 Birbirimizin eksiklerini sevgiyle tamamlamamız")
with col2:
    st.subheader("🥀 Eksilerimiz")
    st.write("💔 Benim bazen seni istemeden de olsa kırmam")
    st.write("⏳ Sensiz geçen, boşa harcanmış her saniye")
    st.write("😔 Şu an yanımda olamaman ve sana sarılamamam...")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# BÖLÜM 5
st.header("📸 Birlikte Yazdığımız Masal")
st.write("Şu fotoğraflara bak... Biz yan yanayken o kadar güzeliz ki, hiçbir şeyin bunu bozmasına izin veremem.")

try:
    # Kendi yüklediğin fotoğrafları gösterir
    st.image("foto1.jpg", caption="Gözlerine bakmaya doyamadığım o an...", use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image("foto2.jpg", caption="İyi ki varsın, iyi ki benimsin.", use_column_width=True)
except:
    st.error("Biriciğim, fotoğraflarımız şu an yükleniyor (GitHub'a foto1.jpg ve foto2.jpg'yi atınca burada bizim o güzel yüzlerimiz çıkacak).")
    rain_hearts()

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #D63384; font-size: 36px; padding-bottom: 50px;'>Seni Çok Seviyorum... Sonsuza Dek. ❤️</h2>", unsafe_allow_html=True)
