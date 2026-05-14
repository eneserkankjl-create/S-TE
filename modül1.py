import streamlit as st
import time

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
st.write("---")

st.sidebar.title("💌 Kalbimin Sesi")
menu = ["Ben Kimim?", "Neden Barışmalıyız?", "Neden Evlenmeliyiz?", "Bizim Dünyamız", "En Güzel Anlarımız"]
choice = st.sidebar.radio("Lütfen birini seç biriciğim:", menu)

if choice == "Ben Kimim?":
    st.header("👤 Seni Her Şeyden Çok Seven O Çocuk")
    st.write("Belki bazen seni kızdıran, saçmalayan, düşüncesizlik eden o şapşal adamım...")
    st.write("Ama aynı zamanda;")
    st.write("✨ Gözlerinin içine bakarken dünyanın durduğunu hisseden,")
    st.write("✨ Senin bir gülüşünle bütün dertlerini unutan,")
    st.write("✨ Hayatının geri kalanını sadece seninle, senin ellerini tutarak geçirmek isteyen o aşığım.")
    st.info("Hatam ne olursa olsun, kalbimde senden başka hiçbir doğru yok. ❤️")

elif choice == "Neden Barışmalıyız?":
    st.header("🥺 Sensiz Bir Saniye Bile Geçmiyor")
    st.write("Çünkü biz birbirimiz için yaratıldık. İki yarım elma değil, tam bir dünya olduk seninle.")
    st.write("Sen bana küstüğünde renkler soluyor, gün aydınlanmıyor. Yaptığım eşşeklik için senden binlerce kez özür dilerim. Söz veriyorum, seni bir daha asla böyle üzmeyeceğim.")
    
    st.write("---")
    st.write("Lütfen o güzel kalbinle beni affeder misin?")
    if st.button("Seni Affettim Sevgilim ❤️"):
        st.balloons()
        st.success("Dünyalar benim oldu! Seni her şeyden, herkesten çok seviyorum! İyi ki varsın... 🥰")

elif choice == "Neden Evlenmeliyiz?":
    st.header("💍 Sonsuzluğumuz: Geleceğimiz")
    st.write("Çünkü ben sabahları gözümü açtığımda ilk senin o güzel yüzünü görmek istiyorum.")
    st.write("Çünkü ben yorucu bir günün ardından eve geldiğimde 'hoş geldin' diyen sesinle huzur bulmak istiyorum.")
    st.write("Seninle yaşlanmak, beraber çocuklarımızı sevmek, saçlarımıza aklar düştüğünde bile el ele yürümek istiyorum.")
    st.warning("Bu bir tekliften daha fazlası; bu sana adanmış bir ömrün sözüdür. ♾️")

elif choice == "Bizim Dünyamız":
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

elif choice == "En Güzel Anlarımız":
    st.header("📸 Birlikte Yazdığımız Masal")
    st.write("Şu fotoğraflara bak... Biz yan yanayken o kadar güzeliz ki, hiçbir şeyin bunu bozmasına izin veremem.")
    
    # Animasyonlu yükleme efekti
    with st.spinner('Aşkımız yükleniyor...'):
        time.sleep(2)
    
    try:
        # Fotoğraf isimlerini aynen koruduk, sen kendi fotolarını eklersin
        st.image("foto1.jpg", caption="Gözlerine bakmaya doyamadığım o an...", use_column_width=True)
        st.image("foto2.jpg", caption="İyi ki varsın, iyi ki benimsin.", use_column_width=True)
    except:
        st.error("Biriciğim, fotoğraflarımız şu an yükleniyor (GitHub'a foto1.jpg ve foto2.jpg'yi atınca burada bizim o güzel yüzlerimiz çıkacak).")
        # Fotoğraflar yoksa bile romantik bir kalp yağmuru yağsın
        st.snow()
