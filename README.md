# 💼 TaxPro Indonesia - Kalkulator Pajak & Biaya Produksi

Platform digital konsultan pajak untuk perhitungan pajak dan manajemen biaya produksi perusahaan di Indonesia.

## 🌟 Fitur Utama

### 💰 Kalkulator Pajak
- **PPh 21** - Pajak Penghasilan Karyawan
  - Perhitungan dengan PTKP sesuai status pernikahan
  - Tarif progresif sesuai UU HPP 2021 (5%, 15%, 25%, 30%, 35%)
  - Perhitungan bonus dan THR
  - Export hasil ke CSV

- **PPh 23** - Pajak Potong Pungut
  - Jasa teknik, manajemen, konsultan (2%)
  - Dividen, royalti, bunga, hadiah (15%)
  - Penyesuaian tarif untuk non-NPWP (100% lebih tinggi)

- **PPN** - Pajak Pertambahan Nilai
  - Tarif 11% (standar 2022-sekarang)
  - Tarif 12% (rencana 2025)
  - Perhitungan DPP (Dasar Pengenaan Pajak)
  - Visualisasi komposisi harga

- **PPh Badan** - Pajak Penghasilan Perusahaan
  - Tarif standar 22%
  - Fasilitas UMKM (11% untuk PKP ≤ 500 juta)
  - Koreksi fiskal
  - Analisis laba netto

### 🏭 Manajemen Biaya Produksi
- Input biaya bahan baku, tenaga kerja, dan overhead
- Perhitungan biaya per unit
- Analisis break-even point
- Kalkulator margin keuntungan
- Rekomendasi harga jual optimal
- Visualisasi breakdown biaya
- Export analisis ke CSV

## 🚀 Cara Menjalankan

### Instalasi

1. Clone repository:
```bash
git clone https://github.com/yandri918/pajak-dan-produksi.git
cd pajak-dan-produksi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
streamlit run app.py
```

4. Buka browser di `http://localhost:8501`

## 📋 Requirements

- Python 3.8+
- Streamlit 1.31.0
- Pandas 2.1.4
- Plotly 5.18.0
- openpyxl 3.1.2

## 🎨 Desain

Aplikasi menggunakan desain modern dengan:
- **Glassmorphism UI** - Efek kaca transparan yang elegan
- **Gradient Background** - Warna gradasi purple-blue yang profesional
- **Responsive Layout** - Tampilan optimal di berbagai ukuran layar
- **Interactive Charts** - Visualisasi data dengan Plotly
- **Custom Styling** - CSS kustom untuk pengalaman pengguna premium

## 📊 Regulasi Pajak

Semua perhitungan pajak mengikuti peraturan perpajakan Indonesia terbaru:
- **UU HPP 2021** (Undang-Undang Harmonisasi Peraturan Perpajakan)
- **PMK terkait PTKP** (Penghasilan Tidak Kena Pajak)
- **Peraturan DJP** (Direktorat Jenderal Pajak)

## 🔗 Link Referensi

- [DJP Online](https://www.pajak.go.id)
- [Peraturan Perpajakan](https://www.pajak.go.id/id/peraturan)
- [UU HPP 2021](https://peraturan.go.id/id/uu-no-7-tahun-2021)

## ⚠️ Disclaimer

Kalkulator ini adalah alat bantu estimasi perhitungan pajak. Untuk perhitungan resmi dan konsultasi mendalam, silakan hubungi konsultan pajak profesional atau kantor pajak terdekat.

## 📞 Kontak

- **Email**: konsultasi@taxpro.id
- **Telepon**: +62 812-3456-7890
- **Website**: [TaxPro Indonesia](https://github.com/yandri918/pajak-dan-produksi)

## 📄 Lisensi

© 2026 TaxPro Indonesia. All rights reserved.

---

**Dibuat dengan ❤️ untuk memudahkan perhitungan pajak dan biaya produksi di Indonesia**
