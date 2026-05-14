import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Ece A.Ş. Özür Raporu", page_icon="🥺", layout="centered")

# Kurumsal ama komik başlık
st.markdown("<h1 style='text-align: center; color: #E83E8C;'>Ece A.Ş. Resmi Özür ve Gelecek Vizyonu Portalı 📄</h1>", unsafe_allow_html=True)
st.write("---")

st.sidebar.title("📌 Kurumsal Navigasyon")
menu = ["Ben Kimim?", "Neden Barışmalıyız?", "Neden Evlenmeliyiz?", "Artılarımız & Eksilerimiz", "Anılar (Data Arşivi)"]
choice = st.sidebar.radio("Lütfen bir modül seçiniz:", menu)

if choice == "Ben Kimim?":
    st.header("👤 Profil Analizi: Ahmet Enes Erkan")
    st.write("Sayın Yönetim Kurulu Başkanı (Ece),")
    st.write("Aşağıda sunulan profil, bazen odunluk seviyesi yüksek olsa da özünde full size çalışan bir CEO'ya aittir.")
    st.info("Hata Kodu 404: Mantık bulunamadı, sadece aşk var. ❤️")
    st.write("- **Meslek:** Senin dertlerinle dertlenen, kargo ve lojistik problemleri çözer gibi ilişki krizlerini çözmeye çalışan bir garip girişimci.")
    st.write("- **Yetenekler:** Gereksiz inat, ama sonunda hep senin haklı olduğunu anlama kapasitesi.")

elif choice == "Neden Barışmalıyız?":
    st.header("🤝 Stratejik Ortaklık ve Barış Gerekçeleri")
    st.write("Bu küsme süreci, her iki tarafın da (özellikle benim) hisse senetlerinde ciddi düşüşe yol açmıştır.")
    
    if st.button("Barışma Talebini Değerlendir ve Onayla"):
        st.balloons()
        st.success("Tebrikler! Mantıklı bir karar verdiniz. Şirketimiz sizinle büyümeye devam edecek. 🎉")
        
    st.write("1. **Sürdürülebilirlik:** Sensiz benim sistem hata veriyor, hayattan api çekemiyorum man.")
    st.write("2. **Ekonomi:** Ayrı ayrı takılmak maliyetli, birleşip kar edebiliriz.")
    st.write("3. **Psikoloji:** Yüzüm gülmüyor, mental stoklar eridi, acil müdahalen lazım.")

elif choice == "Neden Evlenmeliyiz?":
    st.header("💍 Uzun Vadeli Yatırım Planı: Evlilik")
    st.write("Bu birleşme (merger), sektördeki en güçlü ikiliyi yaratacaktır.")
    st.warning("Dikkat: Bu teklif ömür boyu garanti ve sadakat içerir!")
    st.write("- Çünkü ben o yüzüğü o parmağa takmadan rahat etmicem.")
    st.write("- Evlenirsek her gün bu kurumsal şakaları dinlemek zorunda kalacaksın, amazing değil mi?")
    st.write("- Ortak bir şirket (yuva) kurup, tek yetkili CEO'luğa seni atayacağım.")

elif choice == "Artılarımız & Eksilerimiz":
    st.header("📊 İlişki SWOT Analizi")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("➕ Artılarımız")
        st.write("✅ Mükemmel uyum (Sen mükemmelsin, ben ayak uyduruyorum)")
        st.write("✅ Birlikte çok good time geçirmemiz")
        st.write("✅ Vibe'ımızın full match olması")
    with col2:
        st.subheader("➖ Eksilerimiz")
        st.write("❌ Benim bazen saçmalamam")
        st.write("❌ Senin haklı olman ama benim bunu geç processing etmem")
        st.write("❌ Şu an ayrı kalıp vakit kaybetmemiz")

elif choice == "Anılar (Data Arşivi)":
    st.header("📸 Anılar A.Ş. Görsel Arşivi")
    st.write("Burada eski ama altın değerindeki datalarımız mevcuttur.")
    
    # Animasyonlu yükleme efekti
    with st.spinner('Eski güzel günler yükleniyor...'):
        time.sleep(2)
    
    try:
        st.image("foto1.jpg", caption="Şirketimizin en mutlu anları vol.1", use_column_width=True)
        st.image("foto2.jpg", caption="Beraber dünyayı fethederken", use_column_width=True)
    except:
        st.error("Sistem Uyarısı: Fotoğraflar henüz yüklenmedi. Lütfen repo içine 'foto1.jpg' ve 'foto2.jpg' dosyalarını salınız.")
        st.snow()
