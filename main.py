import io
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="İslam ve Siyaset Üstünlük Rehberi | Islam & Beyond Politics",
    page_icon="📖",
    layout="wide"
)

# KOPYALAMA VE SEÇME KORUMASI (Anti-Copy / Anti-Select / Anti-RightClick)
st.markdown("""
<style>
    /* Metin seçilmesini, kopyalanmasını ve sağ tıklanmasını engelleyen CSS */
    body, html, .stApp {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .disclaimer-box {
        background-color: #FEF2F2;
        border-left: 5px solid #EF4444;
        padding: 1.2rem;
        border-radius: 6px;
        margin-bottom: 1.5rem;
        font-size: 0.9rem;
        color: #991B1B;
        line-height: 1.5;
    }
    .quote-card {
        background-color: #F8FAFC;
        border-left: 4px solid #0D9488;
        padding: 1.2rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    .source-tag {
        font-weight: 600;
        color: #0F766E;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>

<script>
    // JavaScript ile Sağ Tık, Kopyalama ve Metin Seçim Engeli
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        alert('Güvenlik ve Telif Koruma Nedeniyle Sağ Tık Devre Dışıktır.');
    });
    
    document.addEventListener('copy', function(e) {
        e.preventDefault();
        alert('Bu yazılımdaki içeriklerin kopyalanması ve çoğaltılması yasaktır.');
    });

    document.addEventListener('keydown', function(e) {
        // Ctrl+C, Ctrl+U, Ctrl+S, Ctrl+A engelleme
        if (e.ctrlKey && (e.key === 'c' || e.key === 'u' || e.key === 's' || e.key === 'a')) {
            e.preventDefault();
            alert('Bu işlem yasal ve teknik güvenlik protokolleri gereği engellenmiştir.');
        }
    });
</script>
""", unsafe_allow_html=True)

# Dil Seçimi
lang = st.sidebar.radio("🌐 DİL / LANGUAGE", ["Türkçe", "English"])

# Kapsamlı Hukuki Uyarılar ve Arayüz Metinleri (Tam Dil Ayrımı)
if lang == "Türkçe":
    st.markdown("""
    <div class="disclaimer-box">
        ⚖️ <b>HUKUKİ KORUMA, TELİF HAKLARI VE KULLANIM ŞARTLARI:</b><br>
        Bu yazılım, arayüz tasarımı, veritabanı yapısı ve içerdiği tüm metinsel/akademik derlemeler 5846 sayılı Fikir ve Sanat Eserleri Kanunu gereğince tamamen koruma altındadır. 
        <b>Yalnızca akademik araştırma, bireysel öğrenim ve bilgi paylaşımı amaçlıdır.</b> 
        Hiçbir surette ticari amaçla kullanılamaz, satılamaz, kopyalanamaz, başka platformlarda yayınlanamaz veya siyasi propaganda, parti propagandası ve benzeri maksatlarla araç yapılamaz. 
        İçeriklerin ve kaynakların kopyalanması, metin seçilmesi ve sağ tık işlemleri sistem tarafından hem hukuki hem de teknik olarak engellenmiştir. 
        Tüm hakları saklıdır.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-header">İslam Dini, Parti Siyaseti ve İstismar Üstünlüğü</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Detaylı Kaynak Künyeleri ve Bibliyografik Referanslarla Akademik İnceleme</div>', unsafe_allow_html=True)
    
    menu_label = "Konu Başlıkları ve Detaylı Kaynaklar"
    menu_options = [
        "Kur'an-ı Kerim Ayetleri (15)", 
        "Hadis-i Şerifler (15)", 
        "Bediüzzaman Said Nursî (15)", 
        "İslam Alimlerinin Görüşleri (15)", 
        "Karşılaştırmalı Analiz Matrisi"
    ]
    security_info = "🔒 *Güvenlik Koruma Aktif:* Metin seçimi, sağ tık ve kopyalama işlemleri yasal tedbirler gereği engellenmiştir."
    server_notice = (
        "💡 *Not:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
        "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir "
        "(ekranda 'Zzzz' simgesi çıkabilir).\n\n"
        "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
        " *'Yes, get this app back up!'* butonuna tıklayın ve uygulamanın "
        "yeniden uyanması için 15-30 saniye bekleyin."
    )
    footer_text = "© 2026 Akademik Eğitim ve Bilgi Paylaşım Platformu. Ticari Amaçla Kullanılamaz, Kopyalanamaz, Tüm Telif Hakları Saklıdır."
    footer_sub = "Non-Commercial, Strict Copyright & Anti-Copy Protection Enforced."

else:
    st.markdown("""
    <div class="disclaimer-box">
        ⚖️ <b>LEGAL PROTECTION, COPYRIGHTS & TERMS OF USE:</b><br>
        This software, interface design, database structure, and all textual/academic compilations contained herein are fully protected under intellectual property laws. 
        <b>Strictly for academic research, individual learning, and informational sharing purposes only.</b> 
        It cannot be used commercially, sold, copied, republished, or utilized for political propaganda or party agendas under any circumstances. 
        Copying content, text selection, and right-clicking are technically and legally restricted. 
        All rights reserved.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-header">Islam, Party Politics & Non-Instrumentalization</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Academic Review with Detailed Bibliographic References</div>', unsafe_allow_html=True)
    
    menu_label = "Topics & Detailed Sources"
    menu_options = [
        "Quranic Verses (15)", 
        "Hadiths (15)", 
        "Bediuzzaman Said Nursi (15)", 
        "Scholarly Views (15)", 
        "Comparative Analysis Matrix"
    ]
    security_info = "🔒 *Security Protection Active:* Text selection, right-click, and copying are disabled due to legal compliance."
    server_notice = (
        "💡 *Note:* This web app is hosted on free servers. "
        "If left idle for a long time, the app may go to sleep mode "
        "(you might see a 'Zzzz' icon).\n\n"
        "💤 If you encounter such a screen, click the blue "
        " *'Yes, get this app back up!'* button and wait 15-30 seconds for it to wake up."
    )
    footer_text = "© 2026 Academic Education and Information Sharing Platform. Non-Commercial, Uncopyable, All Copyrights Reserved."
    footer_sub = "Non-Commercial, Strict Copyright & Anti-Copy Protection Enforced."

# Her bir kategoriden tam 15'er adet detaylı referans içeren veritabanı
content_db = {
    "ayetler": [
        {
            "tr_title": "1. Dinde Fırkalaşma ve Gruplaşma Yasağı",
            "en_title": "1. Prohibition of Factionalism in Religion",
            "tr_source": "Kur'an-ı Kerim | Rûm Suresi, 31-32. Ayetler",
            "en_source": "Quran | Surah Ar-Rum, Verses 31-32",
            "tr_text": "Dinlerini parça parça eden, grup grup (parti parti) ayrılıp her grubun kendi elindeki menfaat veya anlayışla böbürlendiği kimselerden olmayın.",
            "en_text": "Do not be of those who divide their religion and become sects, every faction rejoicing in what it has."
        },
        {
            "tr_title": "2. Dini Değerlerin ve Ayetlerin Siyasi Çıkar Karşılığı Satılmaması",
            "en_title": "2. Not Trading Divine Signs for Political Capital",
            "tr_source": "Kur'an-ı Kerim | Bakara Suresi, 41. Ayet",
            "en_source": "Quran | Surah Al-Baqarah, Verse 41",
            "tr_text": "Ayetlerimi az bir dünya menfaati veya siyasi oy karşılığında satmayın ve yalnız benden korkun.",
            "en_text": "Do not exchange My verses for a small price (worldly gain or votes), and fear only Me."
        },
        {
            "tr_title": "3. Partizanlık ve Tarafgirliğe Karşı Mutlak Adalet İlkesi",
            "en_title": "3. Absolute Justice Over Partisan Bias",
            "tr_source": "Kur'an-ı Kerim | Mâide Suresi, 8. Ayet",
            "en_source": "Quran | Surah Al-Ma'idah, Verse 8",
            "tr_text": "Bir topluluğa duyduğunuz kin sizi adaletsizliğe yöneltmesin. Adil olun; bu takvaya en yakın olanıdır.",
            "en_text": "Do not let hatred for a people prevent you from being just. Be just; that is nearer to righteousness."
        },
        {
            "tr_title": "4. İlahi İpte Topluca Sarılmak ve Tefrikadan Sakınmak",
            "en_title": "4. Holding Fast to Allah's Rope and Avoiding Division",
            "tr_source": "Kur'an-ı Kerim | Âl-i İmrân Suresi, 103. Ayet",
            "en_source": "Quran | Surah Ali 'Imran, Verse 103",
            "tr_text": "Hep birlikte Allah'ın ipine sımsıkı sarılın, parçalanıp ayrılmayın. Zümresel ve siyasi kamplara bölünmek kardeşlik ruhunu zedeler.",
            "en_text": "Hold firmly to the rope of Allah all together and do not become divided. Factional divisions destroy spiritual brotherhood."
        },
        {
            "tr_title": "5. Hakikati Gizlemenin ve Dünyevi Menfaate Alet Etmenin Vebali",
            "en_title": "5. The Sin of Concealing Truth for Worldly Gain",
            "tr_source": "Kur'an-ı Kerim | Bakara Suresi, 174. Ayet",
            "en_source": "Quran | Surah Al-Baqarah, Verse 174",
            "tr_text": "Allah'ın indirdiği kitaptan bir şeyi gizleyip onu az bir pahaya (siyasi veya şahsi çıkara) satanlar, karınlarında ancak ateş yemiş olurlar.",
            "en_text": "Indeed, those who conceal what Allah has sent down of the Book and exchange it for a small price consume nothing into their bellies except fire."
        },
        {
            "tr_title": "6. İnsanları Gruplara Ayırarak Fitne Çıkarmanın Kötülüğü",
            "en_title": "6. The Evil of Dividing People and Spreading Discord",
            "tr_source": "Kur'an-ı Kerim | Kasas Suresi, 4. Ayet",
            "en_source": "Quran | Surah Al-Qasas, Verse 4",
            "tr_text": "Firavun yeryüzünde büyüklük taslamış ve halkını çeşitli zümrelere ve partilere bölerek onları ezmek istemişti. Şüphesiz o bozgunculardandı.",
            "en_text": "Indeed, Pharaoh was haughty in the land and made its people into factions, oppressing a group among them. Indeed, he was of the corrupters."
        },
        {
            "tr_title": "7. Din Adamlarının veya Siyasetçilerin Çıkarları Rab Edinmesi",
            "en_title": "7. Taking Leaders and Authorities as Lords Beside Allah",
            "tr_source": "Kur'an-ı Kerim | Tevbe Suresi, 31. Ayet",
            "en_source": "Quran | Surah At-Tawbah, Verse 31",
            "tr_text": "Onlar hahamlarını ve rahiplerini Allah'ı bırakıp birer rab edindiler... Oysa hepsi ancak tek bir ilaha kulluk etmekle emrolunmuştu.",
            "en_text": "They have taken their scholars and monks as lords besides Allah... And they were not commanded except to worship one God."
        },
        {
            "tr_title": "8. Kalplerin Birleştirilmesi ve Tevhit Bilinci",
            "en_title": "8. Unification of Hearts and Consciousness of Oneness",
            "tr_source": "Kur'an-ı Kerim | Enfâl Suresi, 63. Ayet",
            "en_source": "Quran | Surah Al-Anfal, Verse 63",
            "tr_text": "Allah müminlerin kalplerini kendi rızasıyla birleştirdi. Sen yeryüzündeki tüm serveti harcasaydın yine de kalplerini birleştiremezdin.",
            "en_text": "And He brought together their hearts. If you had spent all that is in the earth, you could not have brought their hearts together."
        },
        {
            "tr_title": "9. Hüküm ve Yetkinin Yalnızca Hakka ve Adalete Dayanması",
            "en_title": "9. Authority and Judgment Resting Solely on Truth and Justice",
            "tr_source": "Kur'an-ı Kerim | En'âm Suresi, 57. Ayet",
            "en_source": "Quran | Surah Al-An'am, Verse 57",
            "tr_text": "De ki: Ben Rabbimden gelen apaçık bir belge üzerindeyim. Sizin acele istediğiniz hüküm benim elimde değildir. Hüküm ancak Allah'ındır.",
            "en_text": "Say: Indeed, I am on clear evidence from my Lord, and you have denied it. That which you are impatient for is not with me. Legislation is only for Allah."
        },
        {
            "tr_title": "10. Müminler Yalnızca Kardeştir İlkesi",
            "en_title": "10. The Principle That Believers Are But Brothers",
            "tr_source": "Kur'an-ı Kerim | Hucurât Suresi, 10. Ayet",
            "en_source": "Quran | Surah Al-Hujurat, Verse 10",
            "tr_text": "Müminler ancak kardeştirler. Öyleyse kardeşlerinizin arasını bulun ve Allah'tan sakının ki rahmete erişesiniz.",
            "en_text": "The believers are but brothers, so make settlement between your brothers. And fear Allah that you may receive mercy."
        },
        {
            "tr_title": "11. Bilginin ve Dinin Siyasi Çatışmalara Kurban Edilmemesi",
            "en_title": "11. Protecting Knowledge and Religion from Political Strife",
            "tr_source": "Kur'an-ı Kerim | Bakara Suresi, 159. Ayet",
            "en_source": "Quran | Surah Al-Baqarah, Verse 159",
            "tr_text": "İndirdiğimiz apaçık delilleri ve hidayeti kitapta insanlara açıklandıktan sonra gizleyenler var ya, işte onlara hem Allah lanet eder hem de lanet ediciler lanet eder.",
            "en_text": "Indeed, those who conceal what We sent down of clear proofs and guidance after We made it clear for the people in the Book - those are cursed by Allah."
        },
        {
            "tr_title": "12. Üstünlüğün Siyasi Zümrelerde Değil Takvada Olması",
            "en_title": "12. Superiority Rests in Piety, Not Factional Status",
            "tr_source": "Kur'an-ı Kerim | Hucurât Suresi, 13. Ayet",
            "en_source": "Quran | Surah Al-Hujurat, Verse 13",
            "tr_text": "Ey insanlar! Şüphesiz sizi bir erkek ile bir dişiden yarattık, tanışasınız diye sizi milletlere ve kabilelere ayırdık. Allah katında en değerli olanınız takvaca en ileri olanınızdır.",
            "en_text": "O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know one another. Indeed, the most noble of you in the sight of Allah is the most righteous of you."
        },
        {
            "tr_title": "13. İnsanları Aldatmak İçin Dini Söylemleri Kullanmanın Tehlikesi",
            "en_title": "13. The Danger of Using Religious Rhetoric to Deceive",
            "tr_source": "Kur'an-ı Kerim | Bakara Suresi, 204. Ayet",
            "en_source": "Quran | Surah Al-Baqarah, Verse 204",
            "tr_text": "İnsanlardan öylesi vardır ki, dünya hayatı hakkındaki sözü senin hoşuna gider ve kalbindekine Allah'ı şahit tutar; oysa o düşmanların en yamanıdır.",
            "en_text": "And of the people is he whose speech pleases you in this worldly life, and he calls Allah to witness as to what is in his heart, yet he is the fiercest of opponents."
        },
        {
            "tr_title": "14. Hakikatin Karşısında Çıkar Gruplarının Akıbeti",
            "en_title": "14. The Fate of Factional Groups Against the Truth",
            "tr_source": "Kur'an-ı Kerim | Mü'minûn Suresi, 53. Ayet",
            "en_source": "Quran | Surah Al-Mu'minun, Verse 53",
            "tr_text": "Ancak insanlar din işlerini aralarında parça parça edip fırkalara ayrıldılar. Her grup kendi elindeki sapkın ya da menfaatçi anlayışla sevinmektedir.",
            "en_text": "But the people divided their religion among them into sects, each faction rejoicing in what it has."
        },
        {
            "tr_title": "15. Ölçüde ve Tartıda (Hakkaniyette) Adaletin Korunması",
            "en_title": "15. Maintaining Absolute Balance and Fairness in Judgment",
            "tr_source": "Kur'an-ı Kerim | Rahmân Suresi, 9. Ayet",
            "en_source": "Quran | Surah Ar-Rahman, Verse 9",
            "tr_text": "Tartıyı adaletle tutun, teraziyi eksiltmeyin (haktan ve adaletten sapmayın).",
            "en_text": "And establish weight in justice and do not make deficient the balance."
        }
    ],
    "hadisler": [
        {
            "tr_title": "1. Dünyevi ve Siyasi Çıkarlar İçin Dinin Araç Yapılması",
            "en_title": "1. Using Religion for Worldly and Political Objectives",
            "tr_source": "Hadis Kaynağı: Tirmizî, Zühd, 60; Ahmed bin Hanbel, Müsned",
            "en_source": "Hadith Source: Tirmidhi, Zuhd 60; Musnad Ahmad",
            "tr_text": "Ahir zamanda dini değerleri dünyevi çıkarlar (makam, oy, şöhret) doğrultusunda kullanan kimselere karşı uyarılar yer alır.",
            "en_text": "Warnings regarding individuals who utilize religious appearances for worldly and political ambitions in later times."
        },
        {
            "tr_title": "2. Körükörüne Particilik ve Asabiyet Yasağı",
            "en_title": "2. Prohibition of Blind Partisanship and Asabiyyah",
            "tr_source": "Hadis Kaynağı: Ebu Davud, Edeb, 112; Müslim, İmâret, 53",
            "en_source": "Hadith Source: Abu Dawud, Adab 112; Muslim, Imarah 53",
            "tr_text": "Kendi grubunu veya partisini haklı çıkararak haksız dahi olsa tarafgirlik yapanların (asabiyet gütmek) İslam ruhundan uzak olduğu belirtilmiştir.",
            "en_text": "Those who promote blind partisanship or tribalism, defending their faction regardless of right or wrong, are distanced from the true spirit of Islam."
        },
        {
            "tr_title": "3. Kör Sancaklar Altında Yapılan Kabilevi ve Zümresel Siyaset",
            "en_title": "3. Tribal and Factional Politics Under Blind Banners",
            "tr_source": "Hadis Kaynağı: Müslim, İmâret, 57; Nesâî, Tahrîm, 28",
            "en_source": "Hadith Source: Muslim, Imarah 57; Nasai, Tahrim 28",
            "tr_text": "Hak ve batıl ölçüsü gözetmeksizin, körü körüne bir zümrenin, partinin veya liderin bayrağı altında asabiyet davası güdenlerin tutumu reddedilmiştir.",
            "en_text": "Warning against fighting or aligning under blind factional banners driven by partisanship rather than truth and justice."
        },
        {
            "tr_title": "4. Dini Değerleri Siyasi Sermaye Haline Getirmenin Tehlikesi",
            "en_title": "4. The Danger of Turning Religious Values into Political Capital",
            "tr_source": "Hadis Kaynağı: İbn Mâce, Fiten, 9; Dârimî, Mukaddime, 32",
            "en_source": "Hadith Source: Ibn Majah, Fitan 9; Darimi, Introduction 32",
            "tr_text": "İlmi ve dini payeleri kişisel çıkarlar, makam veya siyasi menfaatler için kullanan kimselerin ahiretteki veballerinin büyüklüğü bildirilmiştir.",
            "en_text": "Prophetic warnings regarding those who exploit sacred religious knowledge and appearances for personal political positions and temporal status."
        },
        {
            "tr_title": "5. Ümmetin Fırkalara Bölünmesi Üzerine Uyarılar",
            "en_title": "5. Warnings on the Division of the Ummah into Sects",
            "tr_source": "Hadis Kaynağı: Ebu Davud, Sünnet, 1; Tirmizî, İman, 18",
            "en_source": "Hadith Source: Abu Dawud, Sunnah 1; Tirmidhi, Iman 18",
            "tr_text": "Ümmetimin durumu geçmiş ümmetlerin durumuna benzer. Onlar da fırkalara ayrılmışlardı. Benim ümmetim de fırkalara bölünecektir; haktan sapmayanlar hariç.",
            "en_text": "My community will split into numerous factions. Those who hold firmly to the genuine path of unity and truth shall remain safe."
        },
        {
            "tr_title": "6. Alimlerin Siyasi Çıkar Peşine Düşmesinin Zararları",
            "en_title": "6. The Harm of Scholars Pursuing Political Interests",
            "tr_source": "Hadis Kaynağı: Dârimî, Mukaddime, 25; Hakim, Müstedrek",
            "en_source": "Hadith Source: Darimi, Introduction 25; Hakim, Mustadrak",
            "tr_text": "İlmini dünya menfaatine ve siyasi otoritelere yaranmak için satan kimselerin ahiret yurdunu mahvettiği rivayet edilmiştir.",
            "en_text": "Those who sell their religious knowledge for worldly benefits and political alignment ruin their spiritual hereafter."
        },
        {
            "tr_title": "7. Fesat Zamanında Toplumun Birliğini Korumak",
            "en_title": "7. Maintaining Community Unity in Times of Strife",
            "tr_source": "Hadis Kaynağı: Buhârî, Fiten, 2; Müslim, İmâret, 105",
            "en_source": "Hadith Source: Sahih al-Bukhari, Fitan 2; Sahih Muslim, Imarah 105",
            "tr_text": "Fitne ve kargaşa zamanlarında tarafgir kavgalara katılmaktansa evinde oturmayı, dili ve eliyle zarar vermemeyi tercih etmek daha hayırlıdır.",
            "en_text": "During times of civil strife and political chaos, keeping aloof from partisan conflicts is safer and more righteous than joining discord."
        },
        {
            "tr_title": "8. Haksızlık Karşısında Dahi Tarafgirlik Yapmamak",
            "en_title": "8. Refusing Partisanship Even in Favor of Allies",
            "tr_source": "Hadis Kaynağı: Ahmed bin Hanbel, Müsned; Taberânî",
            "en_source": "Hadith Source: Musnad Ahmad; Tabarani",
            "tr_text": "Kendi akrabanız veya grubunuz aleyhine de olsa adaletten şaşmayın. Hak her şeyin üzerindedir.",
            "en_text": "Stand firmly for justice, even if it goes against your own relatives, group, or political allies."
        },
        {
            "tr_title": "9. İnsanları Kamplara Ayıran Demagoji Siyaseti",
            "en_title": "9. Demagogic Politics Dividing People into Camps",
            "tr_source": "Hadis Kaynağı: İbn Mace, Zühd, 24",
            "en_source": "Hadith Source: Ibn Majah, Zuhd 24",
            "tr_text": "İnsanları kandırmak ve taraftar toplamak için hakikati çarpıtan hatib ve siyasetçilerden uzak durun.",
            "en_text": "Stay away from demagogic speakers and politicians who twist truth to deceive and gather partisan crowds."
        },
        {
            "tr_title": "10. Müminler Arasındaki Uhuvvetin Zedelenmesi",
            "en_title": "10. The Erosion of Brotherhood Among Believers",
            "tr_source": "Hadis Kaynağı: Buhârî, Edeb, 57; Müslim, Birr, 24",
            "en_source": "Hadith Source: Sahih al-Bukhari, Adab 57; Sahih Muslim, Birr 24",
            "tr_text": "Mümin müminin kardeşidir; ona zulmetmez, onu yalnız bırakmaz ve hakir görmez. Partisel hırslar bu kardeşliği yok edemez.",
            "en_text": "A believer is the brother of another believer; he does not oppress him, abandon him, or belittle him."
        },
        {
            "tr_title": "11. Hakikati Savunmanın Zorluğu ve Tarafsızlık",
            "en_title": "11. The Difficulty of Defending Truth and Impartiality",
            "tr_source": "Hadis Kaynağı: Tirmizî, Fiten, 7",
            "en_source": "Hadith Source: Tirmidhi, Fitan 7",
            "tr_text": "Öyle bir zaman gelecek ki, kişi dinini korumak için dağdan dağa kaçacak veya fitne ortamından uzak duracaktır.",
            "en_text": "A time will come when preserving one's faith requires withdrawing from factional turmoil and societal polarization."
        },
        {
            "tr_title": "12. Amellerin Siyasi ve Şahsi Niyetlere Göre Değer Kazanması",
            "en_title": "12. Actions Judged by Political and Personal Intentions",
            "tr_source": "Hadis Kaynağı: Buhârî, Bed'ül-Vahy, 1; Müslim, İmâret, 155",
            "en_source": "Hadith Source: Sahih al-Bukhari, Bad' al-Wahy 1",
            "tr_text": "Ameller ancak niyetlere göredir. Herkese niyet ettiği şey vardır. Kimin davası dünya veya makam ise o ona kalır.",
            "en_text": "Actions are judged by intentions, and every person will get what they intended. Whoever migrated for worldly gain or office gets that."
        },
        {
            "tr_title": "13. İnsanları Kamplara Bölerek Üstünlük Taslama",
            "en_title": "13. Claiming Superiority by Dividing People into Camps",
            "tr_source": "Hadis Kaynağı: Ebu Davud, Edeb, 120",
            "en_source": "Hadith Source: Abu Dawud, Adab 120",
            "tr_text": "Cahiliye devri taassubuyla hareket eden, parti veya soy üstünlüğü iddia eden kimseler ümmetin birliğini paramparça eder.",
            "en_text": "Those who act with pre-Islamic tribal arrogance and claim party or lineage superiority shatter community unity."
        },
        {
            "tr_title": "14. Zenginlik ve Makam Tutkusunun Dine Zararı",
            "en_title": "14. The Harm of Greed for Wealth and Office on Religion",
            "tr_source": "Hadis Kaynağı: Tirmizî, Zühd, 26",
            "en_source": "Hadith Source: Tirmidhi, Zuhd 26",
            "tr_text": "İki aç kurdun bir sürüye saldırmasından daha tehlikelisi, kişinin mal ve makam (siyasi koltuk) hırsının dinine verdiği zarardır.",
            "en_text": "The damage caused to a person's religion by the greed for wealth and political status is worse than two hungry wolves let loose on a flock."
        },
        {
            "tr_title": "15. Hakiki Alimlerin Siyaset Çatışmalarından Uzak Duruşu",
            "en_title": "15. True Scholars Staying Clear of Political Clashes",
            "tr_source": "Hadis Kaynağı: İbn Hibbân, Sahih; Beyhakî",
            "en_source": "Hadith Source: Sahih Ibn Hibban; Bayhaqi",
            "tr_text": "Hakiki alimler ve önderler, fitne kapılarını açan siyasi çekişmelere bulaşmadıkları sürece ümmetin güven ve huzur teminatıdır.",
            "en_text": "True scholars remain anchors of peace and security for the community as long as they stay clear of polarizing political strife."
        }
    ],
    "bediuzzaman": [
        {
            "tr_title": "1. Siyasetin Kutuplaştırıcı Doğasından Uzak Durma İlkesi",
            "en_title": "1. The Principle of Abstaining from the Polarizing Nature of Politics",
            "tr_source": "Bediüzzaman Said Nursî | Mektubat, On Üçüncü Mektup",
            "en_source": "Bediuzzaman Said Nursi | The Letters (13th Letter)",
            "tr_text": "Siyaset çekişmelerinin müminler arasındaki kardeşlik bağlarını zedelediği, parti taraftarlığının haksızlıkları aklamaya yol açabildiği vurgulanmıştır.",
            "en_text": "Emphasizing that political disputes damage bonds of brotherhood among believers, making it necessary to abstain from political chaos."
        },
        {
            "tr_title": "2. İslamiyet'in Elmas Hakikatleri ile Siyasi Partilerin Konumu",
            "en_title": "2. The Diamond Truths of Islam vs. Political Party Platforms",
            "tr_source": "Bediüzzaman Said Nursî | Divan-ı Harb-i Örfî",
            "en_source": "Bediuzzaman Said Nursi | Trial of the Martial Court",
            "tr_text": "İslamiyet'in hakikatleri elmas gibidir. Bu kutsal değerlerin kırılgan ve geçici siyasi parti programlarına kurban edilemeyeceği belirtilmiştir.",
            "en_text": "Islam's truths are like diamonds and cannot be subordinated to fragile, temporary political party tools."
        },
        {
            "tr_title": "3. Müspet Hareket ve Siyasi Çekişmelerin Dindeki Yeri",
            "en_title": "3. Positive Action vs. Destructive Political Strife",
            "tr_source": "Bediüzzaman Said Nursî | Hutbe-i Şamiye",
            "en_source": "Bediuzzaman Said Nursi | Damascus Sermon",
            "tr_text": "Müminlerin vazifesinin iman hakikatlerini ihya etmek olduğu; siyasetin tarafgir ve yıkıcı cereyanlarının uhuvveti parçaladığı ifade edilmiştir.",
            "en_text": "Believers' primary duty is reviving faith truths; political factionalism shatters brotherhood, making it essential to keep faith above politics."
        },
        {
            "tr_title": "4. Parti Taraftarlığının Hakikati Perdelemesi",
            "en_title": "4. How Partisan Affiliation Obscures the Truth",
            "tr_source": "Bediüzzaman Said Nursî | Lem'alar (İhlas Risalesi)",
            "en_source": "Bediuzzaman Said Nursi | The Flashes (Treatise on Sincerity)",
            "tr_text": "Partiçilik hissiyatı, insana haksızı haklı gösterecek derecede basiretini kapatır. Hak ve hakikat taraftarlığı dar parti kalıplarının üstündedir.",
            "en_text": "Partisanship blinds individuals to the extent of viewing wrong as right. Allegiance to absolute truth transcends narrow party frameworks."
        },
        {
            "tr_title": "5. Siyasetin Yalan ve Propaganda Üzerine Kurulması",
            "en_title": "5. Politics Built on Deception and Propaganda",
            "tr_source": "Bediüzzaman Said Nursî | Emirdağ Lahikası",
            "en_source": "Bediuzzaman Said Nursi | Emirdag Letters",
            "tr_text": "Gündelik siyaset çoğunlukla garaz, tarafgirlik, aldatma ve demagoji üzerine kurulduğundan iman ehli bu gürültüden uzak durmalıdır.",
            "en_text": "Everyday politics is mostly built on bias, deception, and demagogy; people of faith must keep their distance from this noise."
        },
        {
            "tr_title": "6. Dinin Siyasi Propaganda Malzemesi Yapılması",
            "en_title": "6. Using Religion as Political Propaganda Material",
            "tr_source": "Bediüzzaman Said Nursî | Kastamonu Lahikası",
            "en_source": "Bediuzzaman Said Nursi | Kastamonu Letters",
            "tr_text": "Mukaddes İslamiyet'in siyasete alet edilmesi, dine en büyük haksızlıktır ve manevi değerleri aşındırır.",
            "en_text": "Instrumentalizing sacred Islam for political ends is the greatest injustice to religion and erodes spiritual values."
        },
        {
            "tr_title": "7. Tarafgirlik Hastalığının Akli Melekeleri Örtmesi",
            "en_title": "7. The Disease of Partisanship Clouding Rational Faculties",
            "tr_source": "Bediüzzaman Said Nursî | Mektubat",
            "en_source": "Bediuzzaman Said Nursi | The Letters",
            "tr_text": "Tarafgirlik zihniyeti şeytanı bile alkışlatacak bir körlük yaratır; haklıyı haksız, haksızı haklı ilan eder.",
            "en_text": "Partisan mentality creates a blindness that would applaud even evil; making wrong appear right and right appear wrong."
        },
        {
            "tr_title": "8. İman Hizmetinin Siyasetler Üstü Konumu",
            "en_title": "8. The Supra-Political Stature of Faith Service",
            "tr_source": "Bediüzzaman Said Nursî | Şualar",
            "en_source": "Bediuzzaman Said Nursi | The Rays",
            "tr_text": "İman ve Kur'an hizmeti bütün siyasilerin ve partilerin fevkindedir, hiçbir partinin inhisarına verilemez.",
            "en_text": "The service of faith and Quran is above all politicians and political parties; it cannot be monopolized by any party."
        },
        {
            "tr_title": "9. Müminlerin Kardeşliğini Koruma Zarureti",
            "en_title": "9. The Necessity of Protecting the Brotherhood of Believers",
            "tr_source": "Bediüzzaman Said Nursî | Barla Lahikası",
            "en_source": "Bediuzzaman Said Nursi | Barla Letters",
            "tr_text": "Siyasi cereyanlar yüzünden mümin kardeşlerin birbirine düşmesi, ehli imanın en büyük zararıdır.",
            "en_text": "Believer brothers falling out due to political currents is the greatest damage inflicted upon the people of faith."
        },
        {
            "tr_title": "10. Hakikat Mesleğinde Siyasetin Yeri Olmaması",
            "en_title": "10. The Absence of Politics in the Path of Truth",
            "tr_source": "Bediüzzaman Said Nursî | Tarihçe-i Hayat",
            "en_source": "Bediuzzaman Said Nursi | History of Life",
            "tr_text": "Ben siyasetten ázâdeyüm ve siyaset bataklığından Kur'anın nuruyla kurtuldum.",
            "en_text": "I am entirely free from politics and have been saved from the quagmire of politics through the light of the Quran."
        },
        {
            "tr_title": "11. Siyasetin Zalimleri Alkışlatma Tehlikesi",
            "en_title": "11. The Danger of Politics Praising Tyrants",
            "tr_source": "Bediüzzaman Said Nursî | Divan-ı Harb-i Örfî",
            "en_source": "Bediuzzaman Said Nursi | Trial of the Martial Court",
            "tr_text": "Siyaset, bazen taraftarlık hırsıyla zalimi mazlum, mazlumu zalim göstererek vicdanları yaralar.",
            "en_text": "Politics sometimes portrays tyrants as oppressed and the oppressed as tyrants out of partisan ambition."
        },
        {
            "tr_title": "12. Üçyüz milyon İslam Kardeşliğini Partilere Feda Etmeme",
            "en_title": "12. Not Sacrificing Universal Islamic Brotherhood for Parties",
            "tr_source": "Bediüzzaman Said Nursî | Hutbe-i Şamiye",
            "en_source": "Bediuzzaman Said Nursi | Damascus Sermon",
            "tr_text": "Üçyüz milyon Müslüman kardeşliği dar partiçilik kavgasına feda edilemez.",
            "en_text": "The universal brotherhood of three hundred million Muslims cannot be sacrificed for narrow partisan squabbles."
        },
        {
            "tr_title": "13. İhlasın Zedelenmesi ve Siyasi Menfaatler",
            "en_title": "13. Compromising Sincerity for Political Interests",
            "tr_source": "Bediüzzaman Said Nursî | Lem'alar",
            "en_source": "Bediuzzaman Said Nursi | The Flashes",
            "tr_text": "Amellerde halis niyeti bozacak en tehlikeli şeylerden biri siyasi makam ve şöhret arzularıdır.",
            "en_text": "One of the most dangerous elements corrupting sincere intention in good deeds is the desire for political office and fame."
        },
        {
            "tr_title": "14. Akıl ve Kalbin Siyaset Çatışmalarıyla Yorulması",
            "en_title": "14. Exhausting Mind and Heart with Political Conflicts",
            "tr_source": "Bediüzzaman Said Nursî | Mektubat",
            "en_source": "Bediuzzaman Said Nursi | The Letters",
            "tr_text": "Siyasetin acı ve yorucu fırtınaları akıl ve kalbi manevi gıdasından mahrum bırakır.",
            "en_text": "The bitter and exhausting storms of politics deprive the mind and heart of their spiritual nourishment."
        },
        {
            "tr_title": "15. Hürriyet ve Adaletin Siyaset Üstü Esasları",
            "en_title": "15. Supra-Political Foundations of Freedom and Justice",
            "tr_source": "Bediüzzaman Said Nursî | Eski Said Dönemi Eserleri",
            "en_source": "Bediuzzaman Said Nursi | Early Period Works",
            "tr_text": "Hakiki hürriyet ve adalet, şeriatın ve ahlakın elmas esaslarıyla kaimdir; geçici siyasi rejimlere bağlanamaz.",
            "en_text": "True freedom and justice rest upon the diamond principles of divine law and ethics, not temporary political regimes."
        }
    ],
    "alimler": [
        {
            "tr_title": "1. Siyasi Fırkalaşmanın Ümmet Bilincine Etkisi",
            "en_title": "1. The Impact of Political Factionalism on Community Consciousness",
            "tr_source": "İmam-ı Rabbani | Mektûbât-ı Rabbani (3. Cilt)",
            "en_source": "Imam Rabbani | Maktubat-ı Rabbani (Vol. 3)",
            "tr_text": "İslam alimlerinin siyasi fırkalaşma kavgalarından uzak durması gerektiği, dar gruplara bağlanmanın ümmetin adalet duygusunu zedeleyeceği kaydedilmiştir.",
            "en_text": "Scholars and seekers of truth must stay away from political factionalism, as narrow affiliations damage universal justice."
        },
        {
            "tr_title": "2. Gündelik Siyasetin Demagoji Yapısı",
            "en_title": "2. The Demagogic Nature of Everyday Politics",
            "tr_source": "İmam Gazalî | İhyâu Ulûmi'd-Dîn",
            "en_source": "Imam Al-Ghazali | Ihya Ulum al-Din",
            "tr_text": "Siyasetin çoğunlukla iddia ve tarafgirlik eksenli işlediği; hakikat arayışında olan bir kişinin kalbini korumak için mesafeli durması gerekir.",
            "en_text": "Politics often operates on claims and bias; a seeker of truth must maintain distance from these conflict areas to preserve integrity."
        },
        {
            "tr_title": "3. Hakikatin Siyasi İktidarlardan Bağımsız Savunulması",
            "en_title": "3. Defending Truth Independently of Temporal Authorities",
            "tr_source": "Şah Veliyullah Dehlevi | Hüccetullahil Baliga",
            "en_source": "Shah Waliullah Dehlawi | Hujjat Allah al-Baligha",
            "tr_text": "İslam alimlerinin ümmeti birleştirici rol oynaması, günlük siyasi çalkantılara kapılmamasının ilmi dirayet için şart olduğu vurgulanmıştır.",
            "en_text": "Scholars must unify the community; getting caught up in daily political turbulence weakens intellectual rigor."
        },
        {
            "tr_title": "4. Nefsi Hesaplar ve Siyasi Makam Tutkusu",
            "en_title": "4. Egoistical Calculations and Passion for Political Office",
            "tr_source": "İmam Nevevî | Riyâzü's-Salihîn",
            "en_source": "Imam Nawawi | Riyadh as-Salihin",
            "tr_text": "Dini hizmetlerin ve ilmin arkasına saklanarak yapılan makam, şöhret ve siyasi çıkar hırslarının manevi tahribata yol açacağı belirtilmiştir.",
            "en_text": "Pursuing status, fame, and political ambition under the guise of religious service causes profound spiritual corruption."
        },
        {
            "tr_title": "5. Sultanların ve Siyasilerin Kapısından Uzak Durmak",
            "en_title": "5. Staying Away from the Doors of Sultans and Politicians",
            "tr_source": "İmam Ebu Hanife | Menâkıb-ı Ebu Hanife",
            "en_source": "Imam Abu Hanifa | Manaqib Abu Hanifa",
            "tr_text": "Alimlerin bağımsızlığını koruması için siyasi iktidarların saraylarından ve makam tekliflerinden uzak durması ilke edinilmiştir.",
            "en_text": "To preserve intellectual and spiritual independence, scholars must avoid courting political power or accepting state office tied to agendas."
        },
        {
            "tr_title": "6. Siyasi Çekişmelerin İlmi Hakikatleri Gölgelemesi",
            "en_title": "6. Political Strife Overshadowing Scholarly Truths",
            "tr_source": "İbn Teymiye | Minhâcü's-Sünne",
            "en_source": "Imam Ibn Taymiyyah | Minhaj as-Sunnah",
            "tr_text": "Partisel ve zümresel taassup, hakikatin inkişafını engeller ve müminler arasına nifak tohumları eker.",
            "en_text": "Partisan and factional fanaticism hinders the revelation of truth and sows seeds of hypocrisy among believers."
        },
        {
            "tr_title": "7. Siyasetin Ahlaki Temellerden Kopması",
            "en_title": "7. Politics Detached from Moral Foundations",
            "tr_source": "Mevlana Celaleddin-i Rumi | Mesnevi",
            "en_source": "Rumi | Mathnawi",
            "tr_text": "Nefsi hırslarla yapılan siyaset insanı hakikat yolundan saptırır; kalbi putlaştırır.",
            "en_text": "Politics driven by egoistic ambitions diverts humanity from the path of truth and idolizes the transient self."
        },
        {
            "tr_title": "8. Alimlerin Siyasi Çatışmalarda Hakem Olması",
            "en_title": "8. Scholars Serving as Impartial Judges in Strife",
            "tr_source": "Kâdı İyâd | Şifâ-i Şerif",
            "en_source": "Qadi Iyad | Ash-Shifa",
            "tr_text": "Alimler tarafgir kavgalara taraf olmamalı, ümmetin adalet ve merhamet vicdanını temsil etmelidir.",
            "en_text": "Scholars should never take sides in partisan feuds; they must represent the collective conscience of justice and mercy."
        },
        {
            "tr_title": "9. İktidar Uğruna Dini Değerlerin Feda Edilmesi",
            "en_title": "9. Sacrificing Religious Values for Power",
            "tr_source": "Hasan-ı Basri | Zühd Risaleleri",
            "en_source": "Hasan al-Basri | Treatises on Zuhd",
            "tr_text": "Dünya menfaati ve siyasi iktidar için dinini satan kimse, hem dünyasını hem de ahiretini kaybedenlerin en şerlisidir.",
            "en_text": "Whoever sells their religion for worldly gain and political power is among the worst losers of both worlds."
        },
        {
            "tr_title": "10. Siyasi Demagoji ve Halkın Aldatılması",
            "en_title": "10. Political Demagogy and the Deception of the Public",
            "tr_source": "İbn Haldun | Mukaddime",
            "en_source": "Ibn Khaldun | The Muqaddimah",
            "tr_text": "Siyaset ve iktidar mücadelesi çoğunlukla etik sınırları zorlar; toplumsal asabiyeti körükleyerek kargaşaya yol açar.",
            "en_text": "Political and power struggles frequently push ethical boundaries, fueling social tribalism and leading to chaos."
        },
        {
            "tr_title": "11. Hakikatin Tekeline Siyasi Kimlik Giydirilemez",
            "en_title": "11. Truth Cannot Be Clothed in a Political Identity",
            "tr_source": "Süfyan es-Sevrî | Hilyetü'l-Evliyâ",
            "en_source": "Sufyan al-Thawri | Hilyat al-Awliya",
            "tr_text": "İlmi ve dini hakikatler kimseden yana veya aleyhte siyasi araç yapılamayacak kadar yücedir.",
            "en_text": "Scientific and religious truths are too exalted to be used as partisan political tools for or against anyone."
        },
        {
            "tr_title": "12. Ümmetin Birliğinin Siyasi Hırslardan Üstün Tutulması",
            "en_title": "12. Prioritizing Ummah Unity Over Political Ambitions",
            "tr_source": "İmam Şâfiî | er-Risâle",
            "en_source": "Imam Shafi'i | Al-Risala",
            "tr_text": "Müslümanların vahdetini ve huzurunu bozacak her türlü zümresel ve partisel ayrılıktan kaçınmak dinin temel emridir.",
            "en_text": "Avoiding all forms of factional and partisan division that threatens the unity and peace of Muslims is a fundamental command."
        },
        {
            "tr_title": "13. Siyasi Çatışmaların Kalpteki Nuru Söndürmesi",
            "en_title": "13. Political Conflicts Extinguishing the Light in the Heart",
            "tr_source": "Fudayl bin İyâd | Risaleler",
            "en_source": "Fudayl ibn Iyadh | Letters",
            "tr_text": "Gündelik siyasetin kavgası ve hırsı insanın kalbindeki ihlas nurunu söndürür, maneviyatını köreltir.",
            "en_text": "The quarrels and ambition of daily politics extinguish the light of sincerity in the human heart and dull spirituality."
        },
        {
            "tr_title": "14. Adaletin Siyasi Çıkar Sınırlarına Hapsedilememesi",
            "en_title": "14. Justice Cannot Be Confined to Political Interests",
            "tr_source": "Ömer b. Abdülazîz | Hutbeler ve Mektuplar",
            "en_source": "Umar ibn Abd al-Aziz | Sermons and Letters",
            "tr_text": "Adalet, siyasi aidiyetlere göre değişmez; hak, kimden gelirse gelsin ve kime karşı olursa olsun üstündür.",
            "en_text": "Justice does not change according to political affiliations; truth prevails regardless of whom it serves or opposes."
        },
        {
            "tr_title": "15. İlim Ehlinin Siyasi Bağımsızlığı ve Haysiyeti",
            "en_title": "15. Intellectual Independence and Dignity of Scholars",
            "tr_source": "Ahmed bin Hanbel | Mihnet Süreci ve Menakıb",
            "en_source": "Ahmad bin Hanbal | Trials and Biographies",
            "tr_text": "Alimlerin siyasi baskılar ve vaatler karşısında eğilmeden sadece hakikati savunması ümmetin haysiyet teminatıdır.",
            "en_text": "Scholars defending the truth without bowing to political pressures or promises is the guarantee of community dignity."
        }
    ]
}

# Yan Menü Navigasyon
menu = st.sidebar.selectbox(menu_label, menu_options)

st.sidebar.markdown("---")
st.sidebar.info(security_info)

# Uyku Modu ve Sunucu Bilgilendirmesi (Sidebar)
st.sidebar.markdown("---")
st.sidebar.info(server_notice)

def render_cards(items):
    for item in items:
        title = item["tr_title"] if lang == "Türkçe" else item["en_title"]
        source = item["tr_source"] if lang == "Türkçe" else item["en_source"]
        text = item["tr_text"] if lang == "Türkçe" else item["en_text"]
        
        st.markdown(f"""
        <div class="quote-card">
            <h4>{title}</h4>
            <p><i>"{text}"</i></p>
            <div class="source-tag">📌 {"Kaynak Künyesi" if lang == "Türkçe" else "Reference"}: {source}</div>
        </div>
        """, unsafe_allow_html=True)

if menu in ["Kur'an-ı Kerim Ayetleri (15)", "Quranic Verses (15)"]:
    header_title = "Kur'an-ı Kerim Ayetleri (15 Detaylı Referans)" if lang == "Türkçe" else "Quranic Verses (15 Detailed References)"
    st.subheader(f"📖 {header_title}")
    render_cards(content_db["ayetler"])

elif menu in ["Hadis-i Şerifler (15)", "Hadiths (15)"]:
    header_title = "Hadis-i Şerifler (15 Detaylı Rivayet)" if lang == "Türkçe" else "Hadiths (15 Detailed Narrations)"
    st.subheader(f"📜 {header_title}")
    render_cards(content_db["hadisler"])

elif menu in ["Bediüzzaman Said Nursî (15)", "Bediuzzaman Said Nursi (15)"]:
    header_title = "Bediüzzaman Said Nursî'nin Külliyat Referansları (15 Görüş)" if lang == "Türkçe" else "Views of Bediuzzaman Said Nursi (15 Corpus References)"
    st.subheader(f"💡 {header_title}")
    render_cards(content_db["bediuzzaman"])

elif menu in ["İslam Alimlerinin Görüşleri (15)", "Scholarly Views (15)"]:
    header_title = "İslam Alimlerinin Eserlerindeki Değerlendirmeler (15 Görüş)" if lang == "Türkçe" else "Evaluations from Islamic Scholars' Works (15 Views)"
    st.subheader(f"📚 {header_title}")
    render_cards(content_db["alimler"])

elif menu in ["Karşılaştırmalı Analiz Matrisi", "Comparative Analysis Matrix"]:
    header_title = "Kapsamlı Kaynak ve İstismar Analizi" if lang == "Türkçe" else "Comprehensive Source & Exploitation Analysis"
    st.subheader(f"📊 {header_title}")
    
    if lang == "Türkçe":
        st.table([
            {"Kategori / Alan": "İslam İnancı", "Siyasi Partiler / Siyaset": "Siyasi Yapı", "Risk ve İstismar Analizi": "Analiz"},
            {"Kategori / Alan": "Evrensel ve Kuşatıcı Hakikat", "Siyasi Partiler / Siyaset": "Bölücü, Fırkalaştırıcı Yapı", "Risk ve İstismar Analizi": "Dinin bir partiye indirgenmesi diğer kitleleri dışlar."},
            {"Kategori / Alan": "Mutlak Adalet ve Tarafsızlık", "Siyasi Partiler / Siyaset": "Görece Çıkar ve Oy Kaygısı", "Risk ve İstismar Analizi": "Siyasi beklentiler uğruna kutsal değerler zedelenir."},
            {"Kategori / Alan": "Bütün İnsanlığa Hitap", "Siyasi Partiler / Siyaset": "Zümresel ve Sınırlı Hedefler", "Risk ve İstismar Analizi": "Parti yıprandığında din olgusu da haksız yere hedef alınır."}
        ])
    else:
        st.table([
            {"Category / Domain": "Islamic Faith", "Political Parties / Politics": "Political Structure", "Risk & Exploitation Analysis": "Analysis"},
            {"Category / Domain": "Universal & Encompassing Truth", "Political Parties / Politics": "Divisive & Factional Structure", "Risk & Exploitation Analysis": "Reducing religion to a party alienates others."},
            {"Category / Domain": "Absolute Justice & Impartiality", "Political Parties / Politics": "Relative Interest & Votes", "Risk & Exploitation Analysis": "Sacred values are compromised for political goals."},
            {"Category / Domain": "Addresses All Humanity", "Political Parties / Politics": "Factions & Limited Targets", "Risk & Exploitation Analysis": "When a party fails, religion is unfairly blamed."}
        ])

# Alt Bilgi Footer (Genişletilmiş Hukuki Telif Bildirimi)
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #6B7280; font-size: 0.8rem; line-height: 1.4;">
    <b>{footer_text}</b><br>
    <i>{footer_sub}</i>
</div>
""", unsafe_allow_html=True)