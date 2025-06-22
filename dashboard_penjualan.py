import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Konfigurasi Halaman (Lebih Profesional) ---
st.set_page_config(
    page_title="Dashboard Analisis Penjualan Produk",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': "# Dashboard Analisis Penjualan Produk Sederhana\n\n Ini adalah contoh dashboard yang dibuat dengan Streamlit."
    }
)

# Opsional: Atur tema warna default Seaborn
sns.set_theme(style="whitegrid", palette="viridis") # Bisa juga "pastel", "dark", dll.

# --- 2. Judul Dashboard ---
st.title('Dashboard Analisis Penjualan Produk 📈')
st.markdown('Aplikasi interaktif untuk melihat tren dan performa penjualan berdasarkan filter.')

# --- 3. Muat Data ---
file_path = 'penjualan_produk.csv'
try:
    df = pd.read_csv(file_path)
    df['tanggal'] = pd.to_datetime(df['tanggal'])
except FileNotFoundError:
    st.error(f"Error: File '{file_path}' tidak ditemukan. Pastikan CSV ada di folder yang sama.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error(f"Error: File '{file_path}' kosong atau tidak memiliki kolom.")
    st.stop()

# --- 4. Filter Interaktif (Sidebar) ---
st.sidebar.header('Filter Data Penjualan')

# Filter berdasarkan Wilayah
all_wilayah = ['Semua Wilayah'] + sorted(list(df['wilayah'].unique())) # Sorted agar urut
selected_wilayah = st.sidebar.selectbox('Pilih Wilayah:', all_wilayah)

# Filter berdasarkan Produk
all_produk = ['Semua Produk'] + sorted(list(df['produk'].unique())) # Sorted agar urut
selected_produk = st.sidebar.selectbox('Pilih Produk:', all_produk)

# Terapkan Filter
filtered_df = df.copy()

if selected_wilayah != 'Semua Wilayah':
    filtered_df = filtered_df[filtered_df['wilayah'] == selected_wilayah]

if selected_produk != 'Semua Produk':
    filtered_df = filtered_df[filtered_df['produk'] == selected_produk]

# --- 5. Tampilkan Metrik Kunci (KPIs) ---
st.subheader('Metrik Penjualan Utama')

# Pastikan filtered_df tidak kosong sebelum menghitung metrik
if not filtered_df.empty:
    total_penjualan_keseluruhan = filtered_df['total_penjualan'].sum()
    total_jumlah_terjual_keseluruhan = filtered_df['jumlah_terjual'].sum()
    jumlah_produk_unik = filtered_df['produk'].nunique()
    jumlah_wilayah_unik = filtered_df['wilayah'].nunique()

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4) # Menambah 1 kolom lagi

    with metric_col1:
        st.metric(label="Total Penjualan", value=f"${total_penjualan_keseluruhan:,.2f}") # Format mata uang

    with metric_col2:
        st.metric(label="Total Unit Terjual", value=f"{total_jumlah_terjual_keseluruhan:,.0f}") # Format tanpa desimal

    with metric_col3:
        st.metric(label="Jumlah Produk Unik", value=f"{jumlah_produk_unik}")

    with metric_col4:
        st.metric(label="Jumlah Wilayah Terpilih", value=f"{jumlah_wilayah_unik}")
else:
    st.info("Tidak ada data untuk kombinasi filter yang dipilih. Silakan sesuaikan filter.")


# --- 6. Visualisasi (Menggunakan Kolom) ---
st.header('Tren Penjualan & Performa Produk')

if filtered_df.empty:
    st.warning("Tidak ada data yang tersedia untuk visualisasi berdasarkan filter yang dipilih.")
else:
    # Menggunakan kolom untuk layout grafik
    col_chart1, col_chart2 = st.columns(2) # 2 kolom untuk grafik

    with col_chart1:
        st.subheader('Tren Total Penjualan Harian')
        penjualan_harian = filtered_df.groupby('tanggal')['total_penjualan'].sum().reset_index()
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        sns.lineplot(x='tanggal', y='total_penjualan', data=penjualan_harian, marker='o', ax=ax1)
        ax1.set_title('Tren Total Penjualan Harian')
        ax1.set_xlabel('Tanggal')
        ax1.set_ylabel('Total Penjualan ($)')
        ax1.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45) # Rotasi label x-axis agar tidak tumpang tindih
        plt.tight_layout() # Mengatur layout agar pas
        st.pyplot(fig1)
        plt.close(fig1) # Tutup figur Matplotlib

    with col_chart2:
        st.subheader('Total Jumlah Terjual per Produk')
        jumlah_per_produk = filtered_df.groupby('produk')['jumlah_terjual'].sum().reset_index()
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.barplot(x='produk', y='jumlah_terjual', data=jumlah_per_produk, ax=ax2)
        ax2.set_title('Total Jumlah Terjual per Produk')
        ax2.set_xlabel('Produk')
        ax2.set_ylabel('Jumlah Terjual (Unit)')
        ax2.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout() # Mengatur layout agar pas
        st.pyplot(fig2)
        plt.close(fig2) # Tutup figur Matplotlib

    st.markdown('---') # Garis pemisah

# --- 7. Detail Data (Opsional, dalam Expander) ---
with st.expander("Lihat Data Mentah & Informasi Detail"):
    st.subheader('Data Mentah (Difilter)')
    st.dataframe(filtered_df)
    st.write(f"Jumlah Baris Data: **{len(filtered_df)}**")

    st.subheader('Informasi Kolom')
    # Membuat string buffer untuk menangkap output df.info()
    from io import StringIO
    buffer = StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s) # Menampilkan info sebagai teks biasa