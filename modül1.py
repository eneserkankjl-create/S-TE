import streamlit as st
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Dünyanın En Güzel Kadınına...", page_icon="🌹", layout="centered")

# --- CSS HACK & TASARIM ---
st.markdown("""
    <style>
    /* Fontları çekiyoruz */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
    
    /* 1. Arka planı kalpli pattern yapıyoruz */
    .stApp {
        background-color: #ffe6e6 !important;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 50 50'%3E%3Cpath fill='%23ff9999' fill-opacity='0.6' d='M25 39.7l-1.5-1.4C18.2 33.6 14 29.8 14 25c0-3.9 3.1-7 7-7 2.2 0 4.3 1 5.6 2.6 1.3-1.6 3.4-2.6 5.6-2.6 3.9 0 7 3.1 7 7 0 4.8-4.2 8.6-9.5 13.3L25 39.7z'/%3E%3C/svg%3E") !important;
        background-size: 80px 80px !important;
    }

    /* 2. Streamlit'in ANA KONTEYNERİNİ cam karta çeviriyoruz (TEMA KAYMASINA KESİN ÇÖZÜM) */
    [data-testid="stAppViewBlockContainer"] {
        background: rgba(255, 255, 255, 0.90) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border-radius: 30px !important;
        padding: 3rem 2rem !important;
        margin-top: 5vh !important;
        margin-bottom: 5vh !important;
        box-shadow: 0 10px 40px rgba(216, 27, 96, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        max-width: 650px !important;
    }

    /* Streamlit'in gereksiz header ve footer'ını gizle */
    [data-testid="stHeader"], footer { display: none !important; }

    /* 3. Yazı Tipleri ve Renkler */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #d81b60 !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }
    
    p, li, .stMarkdown {
        font-family: 'Montserrat', sans-serif !important;
        color: #4a4a4a !important;
        font-size: 17px !important;
        line-height: 1.8 !important;
        text-align: center !important;
    }
    
    ul {
        display: inline-block;
        text-align: left !important;
        margin: 0 auto;
    }

    /* 4. Butonları Güzelleştirme */
    .stButton > button {
        border-radius: 20px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
    }
    
    /* İleri/Geri butonları (Secondary) */
    .stButton > button[kind="secondary"] {
        background-color: #ffe6e6 !important;
        color: #d81b60 !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background-color: #ffb3b3 !important;
        transform: scale(1.05);
    }

    /* Affet butonu (Primary) */
    .stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #ff4b8b, #d81b60) !important;
        color: white !important;
        padding: 15px 30px !important;
        font-size: 20px !important;
        border-radius: 30px !important;
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.4) !important;
        animation: pulse 2s infinite !important;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    /* Kalp Yağmuru CSS */
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    .rain-heart {
        position: fixed;
        top: -10vh;
        z-index: 99999;
        animation: fall linear forwards;
        pointer-events: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- STATE YÖNETİMİ (Hikaye Akışı İçin) ---
if 'slide' not in st.session_state:
    st.session_state.slide = 0
if 'forgiven' not in st.session_state:
    st.session_state.forgiven = False

# Kalp Yağmuru Fonksiyonu
def make_it_rain_hearts():
    hearts_html = ""
    for _ in range(80):
        left_pos = random.randint(0, 100)
        duration = random.uniform(3, 6)
        delay = random.uniform(0, 2)
        size = random.uniform(1.5, 3)
        hearts_html += f'<div class="rain-heart" style="left: {left_pos}vw; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}rem;">❤️</div>'
    st.markdown(f"<div>{hearts_html}</div>", unsafe_allow_html=True)

# --- İÇERİK VERİLERİ ---
slides_content = [
    {
        "title": "Dünyanın En Güzel Kadınına... 🌹",
        "text": "Lütfen beni affet sevgilim, çünkü sensiz aldığım nefesin bile bir anlamı yok.<br><br><i>(Hikayemizi okumak için aşağıdaki butona tıkla 👇)</i>"
    },
    {
        "title": "🥺 Sensiz Bir Saniye Bile Geçmiyor",
        "text": "Çünkü biz birbirimiz için yaratıldık. İki yarım elma değil, tam bir dünya olduk seninle.<br><br>Sen bana küstüğünde renkler soluyor, gün aydınlanmıyor. Yaptığım eşşeklik için senden binlerce kez özür dilerim. Söz veriyorum, seni bir daha asla böyle üzmeyeceğim."
    },
    {
        "title": "Seni Her Şeyden Çok Seven O Çocuk",
        "text": "Belki bazen seni kızdıran, saçmalayan, düşüncesizlik eden o şapşal adamım... Ama aynı zamanda;<br><br>✨ Gözlerinin içine bakarken dünyanın durduğunu hisseden,<br>✨ Senin bir gülüşünle bütün dertlerini unutan,<br>✨ Hayatının geri kalanını sadece seninle, senin ellerini tutarak geçirmek isteyen o aşığım."
    },
    {
        "title": "👨‍👩‍👧 En Büyük Hayalimiz: Su",
        "text": "Şimdi gözlerini kapat ve düşün sevgilim... İleride evimizde minik ayak sesleri yankılanacak. Dünyalar güzeli bir kızımız olacak, adını <b>Su</b> koyacağız.<br><br>Senin o güzel kalbini, o güzel gözlerini alacak. Evin içinde paytak paytak koşarken biz birbirimize bakıp ne kadar şanslı olduğumuzu hissedeceğiz. Su düştüğünde beraber kaldıracağız, ona bu dünyadaki en güzel sevgiyi, <i>bizim sevgimizi</i> öğreteceğiz.<br><br>Ben o geleceği, Su'yu kucağımıza alacağımız o günü sadece seninle yaşamak istiyorum."
    }
]

# --- EKRAN RENDER KISMI ---

if st.session_state.forgiven:
    # ---------------- BÜYÜK FİNAL (HER ŞEY ALT ALTA) ----------------
    make_it_rain_hearts()
    st.markdown("<h1>Dünyanın En Mutlu Adamı Yaptın Beni! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; font-weight: 600; color:#d81b60;'>Seni çok seviyorum! Su'ya da selamlar! 🥰👶</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Tüm içerikleri alt alta basıyoruz
    for slide in slides_content[1:]: # İlk giriş sayfasını atla
        st.markdown(f"<h2>{slide['title']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>{slide['text']}</p>", unsafe_allow_html=True)
        st.write("---")
        
    st.markdown("<h2>📸 Bizim Hikayemiz</h2>", unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", caption="Gülüşüne dünyaları sığdırdığım anlar...", use_column_width=True)
        st.image("foto2.jpg", caption="Ellerimiz hiç ayrılmasın.", use_column_width=True)
    except:
        st.info("Birlikte çekildiğimiz o efsane fotoğraflarımız kalbimde kazılı. ❤️")

else:
    # ---------------- SLAYT (HİKAYE) MODU ----------------
    current = st.session_state.slide
    
    # 1. Slide 0,1,2,3 ise Yazıları Göster
    if current < 4:
        st.markdown(f"<h1>{slides_content[current]['title']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p>{slides_content[current]['text']}</p>", unsafe_allow_html=True)
    
    # 2. Slide 4 ise Fotoğrafları Göster
    elif current == 4:
        st.markdown("<h2>📸 Bizim Hikayemiz</h2>", unsafe_allow_html=True)
        try:
            st.image("foto1.jpg", caption="Gülüşüne dünyaları sığdırdığım anlar...", use_column_width=True)
            st.image("foto2.jpg", caption="Ellerimiz hiç ayrılmasın.", use_column_width=True)
        except:
            st.info("Birlikte çekildiğimiz o efsane fotoğraflarımız burada olacaktı (Sisteme yüklemeyi unutmuşum şapşallığımdan 🙈 ama sen hayal et!)")

    # 3. Slide 5 ise Final ve Affet Butonu
    elif current == 5:
        st.markdown("<h1>Lütfen o güzel kalbinle beni affeder misin? 🥺</h1>", unsafe_allow_html=True)
        st.markdown("<p>Geleceğimiz için, Su için, bizim için...</p>", unsafe_allow_html=True)
        st.write("") # Boşluk
        
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            if st.button("Seni Affettim Sevgilim 💖", type="primary", use_container_width=True):
                st.session_state.forgiven = True
                st.rerun() # Sayfayı yenile ve finali göster
                
    st.write("") # Boşluk
    st.write("")
    
    # --- İLERİ / GERİ BUTONLARI (Navigasyon) ---
    nav_col1, nav_col2, nav_col3 = st.columns([2, 1, 2])
    
    with nav_col1:
        if current > 0:
            if st.button("⬅️ Önceki", use_container_width=True):
                st.session_state.slide -= 1
                st.rerun()
                
    with nav_col3:
        if current < 5:
            if st.button("Sonraki ➡️", use_container_width=True):
                st.session_state.slide += 1
                st.rerun()
