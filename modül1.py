import streamlit as st
import random
import time

# Sayfa ayarları
st.set_page_config(page_title="Dünyanın En Güzel Kadınına...", page_icon="❤️", layout="centered")

# Custom CSS - Full Glassmorphism, Google Fonts ve Kalpli Arkaplan
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
    
    /* Arka plan kalpli pattern */
    .stApp {
        background-color: #ffe6e6;
        background-image: url("data:image/svg+xml,%3Csvg width='52' height='26' viewBox='0 0 52 26' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%3E%3Cpath d='M10 10c0-2.21-1.79-4-4-4-3.314 0-6 2.686-6 6 0 4.02 5.05 8.16 10 12.5 4.95-4.34 10-8.48 10-12.5 0-3.314-2.686-6-6-6-2.21 0-4 1.79-4 4zm26 0c0-2.21-1.79-4-4-4-3.314 0-6 2.686-6 6 0 4.02 5.05 8.16 10 12.5 4.95-4.34 10-8.48 10-12.5 0-3.314-2.686-6-6-6-2.21 0-4 1.79-4 4z' fill='%23ffb3b3' fill-opacity='0.4'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }

    /* Buzlu Cam (Glassmorphism) Konteyneri - Yazıların arkası bembeyaz ve okunaklı olacak */
    .glass-container {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 8px 32px 0 rgba(255, 100, 150, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #d81b60;
        text-align: center;
    }
    
    p, li {
        font-family: 'Montserrat', sans-serif !important;
        color: #4a4a4a;
        font-size: 16px;
        line-height: 1.8;
    }

    /* Şelale boşlukları */
    .spacer {
        height: 10vh;
    }

    /* Kalp yağmuru animasyonu için CSS */
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg) scale(1); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg) scale(0.5); opacity: 0.2; }
    }
    
    .rain-heart {
        position: fixed;
        top: -10vh;
        z-index: 99999;
        font-size: 2rem;
        animation: fall linear forwards;
        pointer-events: none;
    }

    /* Header gizleme */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Kalp Yağmuru Fonksiyonu
def make_it_rain_hearts():
    hearts_html = ""
    for _ in range(70): # 70 tane kalp yağacak
        left_pos = random.randint(0, 100)
        duration = random.uniform(3, 6)
        delay = random.uniform(0, 2)
        size = random.uniform(1, 3)
        hearts_html += f'<div class="rain-heart" style="left: {left_pos}vw; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}rem;">❤️</div>'
    
    st.markdown(f"<div>{hearts_html}</div>", unsafe_allow_html=True)


# İÇERİK BAŞLIYOR (Glass Container İçinde)
st.markdown('<div class="glass-container">', unsafe_allow_html=True)

st.markdown("<h1>Dünyanın En Güzel Kadınına... 🌹</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Lütfen beni affet sevgilim, çünkü sensiz aldığım nefesin bile bir anlamı yok.</p>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

st.markdown("<h2>🥺 Sensiz Bir Saniye Bile Geçmiyor</h2>", unsafe_allow_html=True)
st.markdown("<p>Çünkü biz birbirimiz için yaratıldık. İki yarım elma değil, tam bir dünya olduk seninle.</p>", unsafe_allow_html=True)
st.markdown("<p>Sen bana küstüğünde renkler soluyor, gün aydınlanmıyor. Yaptığım eşşeklik için senden binlerce kez özür dilerim. Söz veriyorum, seni bir daha asla böyle üzmeyeceğim.</p>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

st.markdown("<h2>Seni Her Şeyden Çok Seven O Çocuk</h2>", unsafe_allow_html=True)
st.markdown("<p>Belki bazen seni kızdıran, saçmalayan, düşüncesizlik eden o şapşal adamım...</p>", unsafe_allow_html=True)
st.markdown("<p>Ama aynı zamanda;</p>", unsafe_allow_html=True)
st.markdown("<ul>", unsafe_allow_html=True)
st.markdown("<li>✨ Gözlerinin içine bakarken dünyanın durduğunu hisseden,</li>", unsafe_allow_html=True)
st.markdown("<li>✨ Senin bir gülüşünle bütün dertlerini unutan,</li>", unsafe_allow_html=True)
st.markdown("<li>✨ Hayatının geri kalanını sadece seninle, senin ellerini tutarak geçirmek isteyen o aşığım.</li>", unsafe_allow_html=True)
st.markdown("</ul>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

st.markdown("<h2>👨‍👩‍👧 En Büyük Hayalimiz: Su</h2>", unsafe_allow_html=True)
st.markdown("<p>Şimdi gözlerini kapat ve düşün sevgilim... İleride evimizde minik ayak sesleri yankılanacak. Dünyalar güzeli bir kızımız olacak, adını <b>Su</b> koyacağız.</p>", unsafe_allow_html=True)
st.markdown("<p>Senin o güzel kalbini, o güzel gözlerini alacak. Evin içinde paytak paytak koşarken biz birbirimize bakıp ne kadar şanslı olduğumuzu hissedeceğiz. Su düştüğünde beraber kaldıracağız, ona bu dünyadaki en güzel sevgiyi, <i>bizim sevgimizi</i> öğreteceğiz.</p>", unsafe_allow_html=True)
st.markdown("<p>Ben o geleceği, Su'yu kucağımıza alacağımız o günü sadece seninle yaşamak istiyorum.</p>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

st.markdown("<h2>📸 Bizim Hikayemiz</h2>", unsafe_allow_html=True)
try:
    st.image("foto1.jpg", caption="Gülüşüne dünyaları sığdırdığım anlar...", use_column_width=True)
    st.image("foto2.jpg", caption="Ellerimiz hiç ayrılmasın.", use_column_width=True)
except:
    st.info("Birlikte çekildiğimiz o efsane fotoğraflarımız burada olacaktı (Sisteme yüklemeyi unutmuşum şapşallığımdan 🙈)")

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Lütfen o güzel kalbinle beni affeder misin?</h3>", unsafe_allow_html=True)

# Butonu ortalamak için kolonları kullanıyoruz
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Seni Affettim Sevgilim 💖", use_container_width=True):
        make_it_rain_hearts()
        st.success("Dünyanın en mutlu adamı yaptın beni! Seni çok seviyorum! Su'ya da selamlar! 🥰👶")
        time.sleep(5) # Kalpler yağarken ekranda mesaj kalsın diye

st.markdown('</div>', unsafe_allow_html=True) # Glass container bitişi
