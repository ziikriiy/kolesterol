import streamlit as st

# Mengatur warna latar belakang dan gaya font
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f3e9df;  /* Warna latar belakang baru */
        color: #c99548;             /* Warna teks baru */
        font-size: 18px;            /* Ukuran font tetap */
    }
    .css-1d391kg {
        color: #c99548;             /* Mengatur warna teks untuk elemen tertentu */
    }
    table {
        border: 2px solid #fb8e54;  /* Garis tabel dengan warna baru */
    }
    th {
        background-color: #fb8e54;  /* Warna latar untuk header tabel */
        color: white;               /* Warna teks untuk header tabel */
    }
    td {
        background-color: #f3e9df;  /* Warna latar untuk sel tabel */
        color: black;               /* Warna teks untuk sel tabel */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menentukan nilai kolesterol dalam bahan pangan
cholesterol_values = {
    'Daging dan Unggas': {'Daging kambing': 71, 'Daging sapi': 70, 'Daging ayam': 63, 'Daging bebek': 65, 'Daging babi': 80,
                          'Daging anjing': 44.4, 'Daging kalkun': 77, 'Daging unta': 61},
    'Ikan': {'Ikan tuna': 45, 'Ikan salmon': 48, 'Ikan lele': 60, 'Ikan mujair': 55, 'Ikan tongkol': 60, 'Ikan gurame': 66,
             'Ikan patin': 39},
    'Susu dan Telur': {'Susu sapi': 250, 'Telur': 155, 'Mentega': 215, 'Yogurt': 45, 'Kuning telur': 550, 'Keju': 140},
    'Makanan lainnya': {'Sosis daging': 150, 'Hamburger': 47, 'Seblak': 121, 'Bakso': 74, 'Kebab': 79, 'Coklat': 290}
}

# Fungsi untuk menghitung kolesterol
def calculate_cholesterol(jenis_makanan, nama_makanan, bobot):
    if jenis_makanan in cholesterol_values and nama_makanan in cholesterol_values[jenis_makanan]:
        cholesterol_per_100g = cholesterol_values[jenis_makanan][nama_makanan]
        total_cholesterol = (cholesterol_per_100g / 100) * bobot
        return total_cholesterol
    else:
        return f"Tidak ada data kolesterol untuk {nama_makanan} dalam kategori {jenis_makanan}."

# Fungsi untuk evaluasi resiko kolesterol
def evaluate_risk(total_cholesterol):
    if total_cholesterol < 200:
        return "Risiko kolesterol rendah."
    elif 200 <= total_cholesterol < 240:
        return "Risiko kolesterol sedang."
    else:
        return "Risiko kolesterol tinggi."

# Bagian Depan Aplikasi
st.title('Cholesterol Calculator For Foods🥩')  

st.markdown('''Cholesterol Calculator For Foods digunakan untuk menyajikan tabel makanan beserta jumlah kolesterol, menghitung kandungan kolesterol berdasarkan bobot makanan,
             serta memberikan saran makanan sehat.
            ☆: .｡. o(≧▽≦)o .｡.:☆''')
st.markdown('---')

# Sidebar navigation
with st.sidebar:
    selected = st.sidebar.selectbox('Menu', ['Perkenalan', 'Penjelasan Singkat', 'Daftar Makanan', 'Perhitungan Kolesterol', 'Menu Interaktif','Resep Sehat'])
if selected == 'Perkenalan':
    st.header('KELOMPOK 7 (1E-PMIP):')
    image_path = 'kerkom_7.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='dokumentasi kerkom 7')
    st.write('''
    Kelompok 7 merupakan tim mahasiswa Program Studi Penjaminan Mutu Industri Pangan yang berkolaborasi dalam pengembangan aplikasi ini. Berikut adalah anggota tim beserta NIM masing-masing:
    
    1. Kalisa Khatelya (NIM: 2320532) 
    2. Nayla Shafa Aulia (NIM: 2320541) 
    3. Selvi Wardayanti (NIM: 2320555) 
    4. Syifa Aprilya (NIM: 2320558) 
    5. Zikri (NIM: 2320562) 
    
    Aplikasi ini dibuat dengan harapan dapat memberikan manfaat bagi pengguna dalam memahami dan mengelola asupan kolesterol mereka, serta mendukung gaya hidup sehat. Kami mengucapkan terima kasih atas dukungan yang diberikan!
    ''')




if selected == 'Penjelasan Singkat':
    st.header('💡 Tahukah Anda??', divider='rainbow')
    image_path = 'makanan berkolesterol.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='kolesterol')
    st.write('''
            Bahwa sama sekali tidak ada kolesterol dalam makanan nabati apa pun, 
            termasuk sereal, buah-buahan, sayuran, dan biji-bijian? 
            Kolesterol hanya berasal dari makanan hewani🐓🐄''')
    st.write('''
                Kalkulator kolesterol adalah alat yang dapat membantu kita untuk mengetahui berapa 
                banyak kolesterol dalam makanan yang kita makan. Dengan kalkulator kolesterol ini, 
                kita dapat dengan cepat menentukan asupan kolesterol harian dan melacaknya. Seseorang 
                yang berisiko terkena penyakit jantung harus menjaga konsumsi kolesterol hariannya 
                sekitar 200 mg.
                
                Kolesterol bisa berasal dari dua sumber utama yaitu :
                1. Makanan : Kolesterol terutama ditemukan dalam makanan hewani, seperti daging, telur, dan produk susu.
                2. Produksi Tubuh : Hati Anda juga memproduksi kolesterol untuk memenuhi kebutuhan tubuh.
                Meskipun kolesterol penting bagi tubuh, memiliki kadar kolesterol yang tinggi dalam darah dapat meningkatkan risiko penyakit jantung dan stroke. 
                Oleh karena itu, penting untuk mengelola asupan kolesterol melalui pola makan sehat dan gaya hidup aktif.''')

elif selected == 'Daftar Makanan':
    st.header('🧀🍖Daftar Makanan🍔🥚')
    image_path = 'Kolesterol.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='daftar makanan')
    st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
    st.markdown('''Menu ini menyajikan daftar makanan beserta jumlah kolesterolnya setiap bobot per 100 gram dalam satuan mg. Tabel Makanan ini berfungsi untuk memberikan informasi
             kepada pengguna tentang berapa jumlah kolesterol dalam bahan pangan, ini disajikan dalam bobot per 100 gram makanan.
             Untuk mengetahui jumlah kolesterol dalam bobot makanan yang kalian inginkan, silahkan klik menu perhitungan kolesterol ya!!''')
    jenis_makanan = st.selectbox("Pilih Bahan Pangan:", ["Daging dan Unggas", "Ikan", "Susu dan Telur", "Makanan Lainnya"])
    if jenis_makanan == "Daging dan Unggas":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Daging Kambing|71                    |
                |Daging Sapi   |70                    |
                |Daging Ayam   |63                    |
                |Daging Bebek  |65                    |
                |Daging Babi   |80                    |
                |Daging Anjing |44,4                  |
                |Daging Kalkun |77                    |
                |Daging Unta   |61                    |
                  ''')  
    if jenis_makanan == "Ikan":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Ikan Tuna     |45                    |
                |Ikan Salmon   |48                    |
                |Ikan Lele     |60                    |
                |Ikan Mujair   |55                    |
                |Ikan Tongkol  |60                    |
                |Ikan Gurame   |66                    |
                |Ikan Patin    |39                    |         
                ''')
    if jenis_makanan == "Susu dan Telur":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Susu Sapi     |250                   |
                |Telur         |155                   |
                |Mentega       |215                   |
                |Yoghurt       |45                    |
                |Kuning Telur  |550                   |
                |Keju          |140                   |        
                ''')
    if jenis_makanan == "Makanan Lainnya":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Sosis Daging  |150                   |
                |Hamburger     |47                    |
                |Seblak        |121                   |
                |Bakso         |74                    |
                |Kebab         |79                    |
                |Coklat        |290                   |        
                ''')    

elif selected == 'Perhitungan Kolesterol':
    st.header('Perhitungan Kolesterol Dalam Makanan🧮🍳', divider='red')
    image_path = 'Pengukur.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption=' ')
    st.markdown('Nah, di sini Anda dapat memilih jenis bahan pangan, jenis makanan, serta bobot yang ingin Anda ketahui jumlah kolesterolnya dalam makanan tersebut.')
    st.markdown('---')
    jenis_makanan = st.selectbox('Pilih Jenis Bahan Pangan', list(cholesterol_values.keys()))
    makanan_list = list(cholesterol_values[jenis_makanan].keys()) # List makanan berdasarkan jenis makanan yang dipilih
    nama_makanan = st.selectbox('Pilih jenis makanan', makanan_list)
    bobot = st.number_input('Masukkan bobot yang diinginkan (gram)', min_value=1, value=100)

    if st.button('Hitung Kolesterol'):
        total_cholesterol = calculate_cholesterol(jenis_makanan, nama_makanan, bobot)
        if isinstance(total_cholesterol, str):
            st.error(total_cholesterol)
        else:
            st.success(f'Perkiraan kolesterol dalam {nama_makanan} ({bobot}g): {total_cholesterol} mg')
            st.balloons()
            st.markdown('---')
            st.header('Saran Makanan', divider='blue')
            if total_cholesterol < 200:
                st.write("Hore! Kolesterol dalam makanan Anda rendah. Ini adalah beberapa saran untuk menjaga kesehatan dan mengatur pola makan Anda:")
                st.write("- Pilih lebih banyak buah-buahan dan sayuran segar untuk menu sehari-hari.")
                st.write("- Rasakan kelezatan ikan dan kacang-kacangan sebagai sumber protein yang lebih sehat.")
                st.write("- Batasi makanan olahan dan makanan cepat saji yang tinggi lemak.")
                st.write("- Tetap aktif! Berjalan-jalan, bersepeda, atau lakukan olahraga ringan setiap hari.")
            elif 200 <= total_cholesterol < 240:
                st.write("Hmm, kolesterol dalam makanan Anda sedang, tetap dijaga dan jangan makan secara berlebihan ya! Ini adalah beberapa saran untuk menjaga kesehatan dan mengatur pola makan Anda:")
                st.write("- Pilih makanan rendah lemak dan tinggi serat seperti oatmeal dan buah-buahan.")
                st.write("- Coba hidangkan ikan alih-alih daging merah untuk variasi yang lebih sehat.")
                st.write("- Tetap aktif! Lakukan aktivitas fisik yang Anda nikmati setiap hari.")
                st.write("- Jika Anda merasa perlu, konsultasikan dengan dokter untuk evaluasi lebih lanjut.")
            else:
                st.write("Oh tidak! Kolesterol dalam makanan Anda tinggi, kurangi porsi makanan ini ya! Bahaya loh jika dikonsumsi dalam jumlah yang banyak dengan waktu yang sering. Tapi jangan khawatir, ini adalah beberapa saran untuk membantu mengontrol pola makan Anda:")
                st.write("- Batasi makanan tinggi lemak jenuh seperti daging berlemak dan produk olahan susu.")
                st.write("- Cari sumber protein rendah lemak seperti tahu dan ayam tanpa kulit.")
                st.write("- Hindari makanan cepat saji dan camilan tinggi lemak.")
                st.write("- Aktivitas fisik adalah kunci! Cobalah berjalan kaki atau berenang untuk memulai.")
                st.write("- Jika perlu, temui dokter untuk rencana pengelolaan yang lebih spesifik.")


elif selected == 'Menu Interaktif':
    st.header('Menu Interaktif 🍽', divider='blue')
    st.subheader('Tes Pengetahuan 📝')
    image_path = 'tes kecerdasan.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption=' ')
    st.write('''Yuk, tes pengetahuan tentang kolesterol, ini akan mengasah pengetahuanmu tentang kesehatan! Ayo, kita jelajahi beberapa pertanyaan seru seputar kolesterol!''')
    # Pertanyaan 1
    st.write('1. Apa yang dimaksud dengan kolesterol HDL?')
    answer1 = st.radio('1.', options=['A. Kolesterol Baik', 'B. Kolesterol Jelek', 'C. Kolesterol Total'])
    # Pertanyaan 2
    st.write('2. Makanan mana yang mengandung kolesterol tinggi?')
    answer2 = st.radio('2.', options=['A. Buah-buahan', 'B. Sayuran', 'C. Daging merah'])
    # Pertanyaan 3
    st.write('3. Bagaimana cara menurunkan kolesterol LDL?')
    answer3 = st.radio('3.', options=['A. Mengonsumsi makanan tinggi lemak', 'B. Berolahraga secara teratur', 'C. Minum minuman bersoda'])
    # Pertanyaan 4
    st.write('4. Apa yang menjadi sumber kolesterol utama dalam makanan?')
    answer4 = st.radio('4.', options=['A. Buah-buahan', 'B. Daging', 'C. Sayuran'])
    # Pertanyaan 5
    st.write('5. Bagaimana cara menurunkan kolesterol secara alami?')
    answer5 = st.radio('5.', options=['A. Mengonsumsi makanan tinggi lemak', 'B. Berolahraga secara teratur', 'C. Minum minuman bersoda'])
    # Pertanyaan 6
    st.write('6. Apa arti dari singkatan LDL dalam kolesterol?')
    answer6 = st.radio('6.', options=['A. Low-Density Lipoprotein', 'B. High-Density Lipoprotein', 'C. Low-Density Liquid'])
    # Pertanyaan 7
    st.write('7. Mengonsumsi makanan apa yang dapat meningkatkan kolesterol HDL?')
    answer7 = st.radio('7.', options=['A. Makanan tinggi lemak', 'B. Buah-buahan dan sayuran', 'C. Minuman beralkohol'])
    # Pertanyaan 8
    st.write('8. Apa dampak kolesterol tinggi bagi kesehatan jantung?')
    answer8 = st.radio('8.', options=['A. Meningkatkan risiko penyakit jantung', 'B. Menurunkan tekanan darah', 'C. Meningkatkan fungsi jantung'])
    # Pertanyaan 9
    st.write('9. Apakah makanan yang mengandung serat dapat membantu menurunkan kolesterol?')
    answer9 = st.radio('9.', options=['A. Ya', 'B. Tidak', 'C. Tergantung jenis seratnya'])
    # Pertanyaan 10
    st.write('10. Bagaimana cara mengecek kadar kolesterol dalam tubuh?')
    answer10 = st.radio('10.', options=['A. Melakukan tes darah', 'B. Melakukan tes urine', 'C. Melakukan pemeriksaan mata'])
    
    if st.button('Submit'):
        score = 0
        # Hitung skor berdasarkan jawaban yang benar
        if answer1 == 'A. Kolesterol Baik':
            score += 1
        if answer2 == 'C. Daging merah':
            score += 1
        if answer3 == 'B. Berolahraga secara teratur':
            score += 1
        if answer4 == 'B. Daging':
            score += 1
        if answer5 == 'B. Berolahraga secara teratur':
            score += 1
        if answer6 == 'A. Low-Density Lipoprotein':
            score += 1
        if answer7 == 'B. Buah-buahan dan sayuran':
            score += 1
        if answer8 == 'A. Meningkatkan risiko penyakit jantung':
            score += 1
        if answer9 == 'A. Ya':
            score += 1
        if answer10 == 'A. Melakukan tes darah':
            score += 1
        st.write(f'Nilai Anda: {score}/10')
        if score <= 5:
            st.write('Wah nilai mu cukup kurang, Pelajari lebih banyak lagi ya tentang kolesterol!')
        else:
            st.write('Hebat! kamu sudah memiliki pemahaman yang baik tentang kolesterol, terus tingkatkan ya!')
            st.balloons()
    st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
    
if selected == 'Resep Sehat':
    st.subheader('Resep Sehat 🥗')
    image_path = 'resep sehat.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption=' ')
    st.write('Ingin mencoba resep sehat rendah kolesterol? Lihat resep berikut ini:')
    st.markdown('''
            1. Sayuran Panggang dengan Bumbu Rempah
            
            Bahan:
            - 500 gram sayuran (wortel, kentang, brokoli, paprika)
            - 2 sendok makan minyak zaitun
            - 1 sendok teh bawang putih bubuk
            - 1 sendok teh merica
            - 1 sendok teh serbuk paprika
            - Garam secukupnya
                
            Cara membuat:
            - Potong sayuran sesuai selera.
            - Campurkan sayuran dengan minyak zaitun, bawang putih bubuk, merica, paprika, dan garam dalam mangkuk besar. Aduk hingga sayuran terbalut rata dengan bumbu.
            - Panggang dalam oven pada suhu 200°C selama 20-25 menit atau hingga sayuran matang dan agak kecokelatan.
            
            2. Salad Buah Segar
            
            Bahan:
            - 2 buah apel, potong dadu
            - 1 buah pir, potong dadu
            - 1 mangga, potong dadu
            - 1 jeruk nipis, peras airnya
            - Madu secukupnya
            - Daun mint segar (opsional)
                
            Cara membuat:
            - Campurkan semua buah dalam sebuah mangkuk besar.
            - Peras air jeruk nipis di atas buah-buahan.
            - Tambahkan madu sesuai selera.
            - Taburkan daun mint segar untuk penyajian jika diinginkan.
            
            3. Puding Chia dengan Buah-buahan
            
            Bahan:
            - 3 sendok makan biji chia
            - 1 gelas susu almond (atau susu rendah lemak lainnya)
            - 1 sendok makan madu atau pemanis alami lainnya
            - Buah-buahan potong (strawberi, blueberry, kiwi)
                
            Cara membuat:
            - Campurkan biji chia, susu almond, dan madu dalam sebuah mangkuk. Aduk rata dan biarkan selama 10 menit.
            - Aduk kembali campuran tersebut dan biarkan dalam lemari es semalaman atau minimal 4 jam.
            - Sebelum disajikan, tambahkan potongan buah-buahan di atas puding chia.
            
            4. Sup Sayur Bayam
            
            Bahan:
            - 200 gram bayam segar
            - 1 buah wortel, potong dadu kecil
            - 1 batang seledri, iris tipis
            - 1 liter kaldu sayuran
            - 2 siung bawang putih, cincang halus
            Garam dan merica secukupnya
            
            Cara membuat:
            - Rebus kaldu sayuran hingga mendidih.
            - Tambahkan wortel, seledri, dan bayam. Masak hingga sayuran matang.
            - Bumbui dengan garam dan merica sesuai selera.
            
            5. Tofu Stir-fry
            
            Bahan:
            - 200 gram tahu, potong dadu
            - 1 wortel, iris tipis
            - 1 paprika, potong dadu
            - 100 gram kacang polong
            - 2 sendok makan saus tiram
            - 1 sendok makan kecap manis
            Minyak sayur secukupnya untuk menumis
            
            Cara membuat:
            - Panaskan minyak dalam wajan. Tumis bawang putih hingga harum.
            - Masukkan wortel, paprika, dan kacang polong. Tumis hingga sayuran setengah matang.
            - Tambahkan tahu dan saus tiram. Masak hingga semua bahan tercampur rata.
            
            6. Salad Sayur Segar
            
            Bahan:
            - 1 wortel, potong julienne
            - 1 mentimun, potong dadu
            - 1 tomat, potong dadu
            - 50 gram kacang polong
            - 1 sendok makan minyak zaitun
            - 1 sendok makan cuka apel
            - Garam dan merica secukupnya
            
            Cara membuat:
            - Campurkan semua sayuran dalam sebuah mangkuk besar.
            - Tambahkan minyak zaitun, cuka apel, garam, dan merica. Aduk hingga rata.
            
            7.Oatmeal Pisang
            
            Bahan:
            - 1/2 cup oatmeal
            - 1 buah pisang, potong-potong
            - 1 sendok makan madu
            - 1/2 cup susu almond
            - Secubit kayu manis
            
            Cara membuat:
            - Rebus oatmeal dalam susu almond hingga matang.
            - Tambahkan pisang dan madu. Aduk rata.
            - Taburi dengan kayu manis sebelum disajikan.
            
            8.Tumis Buncis
            
            Bahan:
            - 200 gram buncis, potong-potong
            - 2 siung bawang putih, cincang halus
            - 1 sendok makan minyak sayur
            - Garam dan merica secukupnya
            
            Cara membuat:
            - Panaskan minyak dalam wajan. Tumis bawang putih hingga harum.
            - Masukkan buncis dan tumis hingga matang.
            - Bumbui dengan garam dan merica sesuai selera.
            
            9. Smoothie Pepaya
            
            Bahan:
            - 1/2 buah pepaya, buang bijinya dan potong dadu
            - 1 buah pisang
            - 1/2 cup yoghurt plain
            - 1/2 cup air
            - Es batu secukupnya
            
            Cara membuat:
            - Campur semua bahan dalam blender.
            - Blender hingga halus dan konsisten.
            - Sajikan dengan es batu.
            
            10. Tahu Tumis Bawang Putih
            
            Bahan:
            - 200 gram tahu, potong dadu
            - 4 siung bawang putih, cincang halus
            - 1 sendok makan saus tiram
            - 1 sendok makan kecap manis
            - Minyak sayur secukupnya untuk menumis
            
            Cara membuat:
            - Panaskan minyak dalam wajan. Tumis bawang putih hingga harum.
            - Masukkan tahu dan tumis hingga matang.
            - Tambahkan saus tiram dan kecap manis. Aduk hingga rata.
                            
            Makanan ini rendah kolesterol karena bahan utamanya adalah sayuran, buah-buahan, dan tidak menggunakan lemak jenuh atau minyak yang tinggi kolesterol.
            Selain itu, resep ini juga memperhatikan penggunaan pemanis alami dan minyak sehat.''')
