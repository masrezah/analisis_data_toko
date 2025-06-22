## Fitur Utama

* Ringkasan Data Interaktif: Menampilkan ikhtisar awal dari data penjualan.
* Filter Dinamis: Memungkinkan pengguna memfilter data berdasarkan wilayah dan jenis produk.
* Metrik Kunci (KPIs): Menampilkan angka-angka penting seperti Total Penjualan, Total Unit Terjual, dan jumlah produk unik.
* Visualisasi Tren: Grafik garis untuk melihat tren penjualan harian.
* Performa Produk: Grafik batang untuk menunjukkan jumlah unit terjual per produk.
* Detail Data: Opsi untuk melihat data mentah yang telah difilter.

 ## Teknologi yang Digunakan

* Python
* Streamlit: Untuk membangun aplikasi *web dashboard*.
* Pandas: Untuk manipulasi dan analisis data.
* Matplotlib & Seaborn: Untuk visualisasi data.

## Cara Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan *dashboard* ini di lingkungan lokal Anda:

1.  **Kloning Repositori:**
    Buka terminal atau *command prompt* Anda dan kloning repositori ini:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/analisis_data_python.git](https://github.com/YOUR_USERNAME/analisis_data_python.git)
    ```
    Ganti `YOUR_USERNAME` dengan nama pengguna GitHub Anda.

2.  **Masuk ke Direktori Proyek:**
    ```bash
    cd analisis_data_python
    ```

3.  **Buat dan Aktifkan Lingkungan Virtual:**
    Sangat disarankan untuk menggunakan lingkungan virtual untuk mengelola dependensi.
    ```bash
    python -m venv venv
    ```
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instal Dependensi:**
    Instal semua *library* yang diperlukan:
    ```bash
    pip install streamlit pandas matplotlib seaborn
    ```

5.  **Siapkan Data:**
    Pastikan *file* data Anda, `penjualan_produk.csv`, berada di direktori utama proyek (`analisis_data_python`). Jika belum ada, Anda bisa membuatnya dengan data contoh yang telah disediakan.

6.  **Jalankan Aplikasi Streamlit:**
    ```bash
    streamlit run dashboard_penjualan.py
    ```
    Aplikasi akan terbuka secara otomatis di *browser* *web* Anda (biasanya di `http://localhost:8501`).
