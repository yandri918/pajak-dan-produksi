import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="TaxPro Indonesia - Kalkulator Pajak & Biaya Produksi",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 2rem;
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 1.5rem;
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.95;
    }
    
    /* Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #6366f1;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1rem 2rem;
        color: white;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        color: #6366f1 !important;
    }
    
    /* Success/Info Boxes */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Result Cards */
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .result-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }
    
    .result-value {
        font-size: 2rem;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 💼 TaxPro Indonesia")
    st.markdown("---")
    
    page = st.radio(
        "Navigasi",
        ["🏠 Beranda", "💰 Kalkulator Pajak", "🏭 Biaya Produksi", "📞 Kontak"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Info Cepat")
    st.info("**Tarif PPN:** 11%")
    st.info("**PPh Badan:** 22%")
    st.info("**Update:** UU HPP 2021")
    
    st.markdown("---")
    st.markdown("### 🔗 Link Penting")
    st.markdown("[DJP Online](https://www.pajak.go.id)")
    st.markdown("[Peraturan Pajak](https://www.pajak.go.id/id/peraturan)")

# Main Content
if page == "🏠 Beranda":
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>💼 TaxPro Indonesia</h1>
        <p>Konsultan Digital Pajak & Manajemen Biaya Produksi</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
            <h3>Kalkulator Pajak Lengkap</h3>
            <p>PPh 21, PPh 23, PPN, PPh Badan sesuai regulasi terbaru</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🏭</div>
            <h3>Analisis Biaya Produksi</h3>
            <p>Break-even point, margin keuntungan, dan harga jual optimal</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
            <h3>Sesuai Regulasi DJP</h3>
            <p>Update UU HPP 2021 dan peraturan perpajakan Indonesia</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Welcome Section
    st.markdown("""
    <div class="glass-card">
        <h2>Selamat Datang di TaxPro Indonesia</h2>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            Platform digital terpercaya untuk perhitungan pajak dan manajemen biaya produksi perusahaan Anda.
            Kami menyediakan kalkulator pajak yang akurat sesuai dengan peraturan perpajakan Indonesia terbaru,
            serta tools analisis biaya produksi untuk membantu Anda menentukan harga jual yang optimal.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Services
    st.markdown("<div class='glass-card'><h2>Layanan Kami</h2></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📄 Pelaporan SPT")
        st.write("Bantuan pelaporan SPT Tahunan dan Masa")
        
        st.markdown("#### ⚖️ Tax Planning")
        st.write("Perencanaan pajak yang efisien")
    
    with col2:
        st.markdown("#### 🔍 Tax Review")
        st.write("Review dan audit internal perpajakan")
        
        st.markdown("#### 🎓 Pelatihan Pajak")
        st.write("Workshop untuk tim finance")
    
    with col3:
        st.markdown("#### 🤝 Pendampingan Pemeriksaan")
        st.write("Pendampingan saat pemeriksaan DJP")
        
        st.markdown("#### 📊 Pembukuan & Akuntansi")
        st.write("Jasa pembukuan dan laporan keuangan")

elif page == "💰 Kalkulator Pajak":
    st.markdown("""
    <div class="main-header">
        <h1>💰 Kalkulator Pajak</h1>
        <p>Hitung pajak Anda dengan akurat sesuai peraturan perpajakan Indonesia</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tax Type Tabs
    tax_tab = st.tabs(["PPh 21", "PPh 23", "PPN", "PPh Badan"])
    
    # PPh 21 Calculator
    with tax_tab[0]:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📊 Kalkulator PPh 21 - Pajak Penghasilan Karyawan")
        st.caption("Hitung pajak penghasilan karyawan berdasarkan UU HPP 2021")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Input Data Karyawan")
            
            gaji_bruto = st.number_input(
                "Gaji Bruto per Bulan (Rp)",
                min_value=0,
                value=10000000,
                step=100000,
                format="%d"
            )
            
            status = st.selectbox(
                "Status Pernikahan",
                ["TK/0 - Tidak Kawin, Tanpa Tanggungan",
                 "TK/1 - Tidak Kawin, 1 Tanggungan",
                 "TK/2 - Tidak Kawin, 2 Tanggungan",
                 "TK/3 - Tidak Kawin, 3 Tanggungan",
                 "K/0 - Kawin, Tanpa Tanggungan",
                 "K/1 - Kawin, 1 Tanggungan",
                 "K/2 - Kawin, 2 Tanggungan",
                 "K/3 - Kawin, 3 Tanggungan"]
            )
            
            bonus = st.number_input(
                "Bonus/THR Tahunan (Rp)",
                min_value=0,
                value=0,
                step=100000,
                format="%d"
            )
            
            potongan = st.number_input(
                "Potongan (BPJS, Pensiun) per Bulan (Rp)",
                min_value=0,
                value=0,
                step=10000,
                format="%d"
            )
            
            if st.button("🧮 Hitung PPh 21", use_container_width=True):
                # PTKP Calculation
                ptkp_map = {
                    "TK/0": 54000000,
                    "TK/1": 58500000,
                    "TK/2": 63000000,
                    "TK/3": 67500000,
                    "K/0": 58500000,
                    "K/1": 63000000,
                    "K/2": 67500000,
                    "K/3": 72000000
                }
                
                status_code = status.split(" - ")[0]
                ptkp = ptkp_map[status_code]
                
                # Annual Calculation
                gaji_tahunan = (gaji_bruto - potongan) * 12
                penghasilan_bruto = gaji_tahunan + bonus
                penghasilan_netto = penghasilan_bruto
                pkp = max(0, penghasilan_netto - ptkp)
                
                # Progressive Tax Calculation (UU HPP 2021)
                pajak = 0
                if pkp > 0:
                    if pkp <= 60000000:
                        pajak = pkp * 0.05
                    elif pkp <= 250000000:
                        pajak = 60000000 * 0.05 + (pkp - 60000000) * 0.15
                    elif pkp <= 500000000:
                        pajak = 60000000 * 0.05 + 190000000 * 0.15 + (pkp - 250000000) * 0.25
                    elif pkp <= 5000000000:
                        pajak = 60000000 * 0.05 + 190000000 * 0.15 + 250000000 * 0.25 + (pkp - 500000000) * 0.30
                    else:
                        pajak = 60000000 * 0.05 + 190000000 * 0.15 + 250000000 * 0.25 + 4500000000 * 0.30 + (pkp - 5000000000) * 0.35
                
                pajak_bulanan = pajak / 12
                gaji_netto_bulanan = gaji_bruto - pajak_bulanan
                
                # Store in session state
                st.session_state.pph21_result = {
                    'gaji_bruto': gaji_bruto,
                    'potongan': potongan,
                    'gaji_tahunan': gaji_tahunan,
                    'bonus': bonus,
                    'penghasilan_bruto': penghasilan_bruto,
                    'ptkp': ptkp,
                    'pkp': pkp,
                    'pajak_tahunan': pajak,
                    'pajak_bulanan': pajak_bulanan,
                    'gaji_netto': gaji_netto_bulanan
                }
        
        with col2:
            st.markdown("#### Hasil Perhitungan")
            
            if 'pph21_result' in st.session_state:
                result = st.session_state.pph21_result
                
                # Display Results
                st.metric("Gaji Bruto/Bulan", f"Rp {result['gaji_bruto']:,.0f}")
                st.metric("PPh 21/Bulan", f"Rp {result['pajak_bulanan']:,.0f}", 
                         delta=f"{(result['pajak_bulanan']/result['gaji_bruto']*100):.2f}%")
                st.metric("Gaji Netto/Bulan", f"Rp {result['gaji_netto']:,.0f}")
                
                st.markdown("---")
                st.markdown("##### Detail Perhitungan Tahunan")
                
                detail_df = pd.DataFrame({
                    'Keterangan': [
                        'Penghasilan Bruto',
                        'PTKP',
                        'Penghasilan Kena Pajak (PKP)',
                        'PPh 21 Tahunan'
                    ],
                    'Jumlah (Rp)': [
                        f"{result['penghasilan_bruto']:,.0f}",
                        f"{result['ptkp']:,.0f}",
                        f"{result['pkp']:,.0f}",
                        f"{result['pajak_tahunan']:,.0f}"
                    ]
                })
                
                st.dataframe(detail_df, use_container_width=True, hide_index=True)
                
                # Download Button
                st.download_button(
                    "📥 Download Hasil (CSV)",
                    detail_df.to_csv(index=False).encode('utf-8'),
                    "hasil_pph21.csv",
                    "text/csv",
                    use_container_width=True
                )
            else:
                st.info("👈 Masukkan data dan klik tombol Hitung untuk melihat hasil")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # PPh 23 Calculator
    with tax_tab[1]:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📊 Kalkulator PPh 23 - Pajak Potong Pungut")
        st.caption("Hitung pajak potong pungut untuk jasa dan dividen")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Input Data")
            
            jenis_penghasilan = st.selectbox(
                "Jenis Penghasilan",
                ["Jasa Teknik, Manajemen, Konsultan (2%)",
                 "Sewa Selain Tanah/Bangunan (2%)",
                 "Dividen (15%)",
                 "Royalti (15%)",
                 "Bunga (15%)",
                 "Hadiah & Penghargaan (15%)"]
            )
            
            jumlah_bruto = st.number_input(
                "Jumlah Bruto (Rp)",
                min_value=0,
                value=10000000,
                step=100000,
                format="%d"
            )
            
            punya_npwp = st.checkbox("Penerima Memiliki NPWP", value=True)
            st.caption("⚠️ Tanpa NPWP, tarif dinaikkan 100%")
            
            if st.button("🧮 Hitung PPh 23", use_container_width=True):
                # Determine rate
                if "2%" in jenis_penghasilan:
                    tarif_dasar = 0.02
                else:
                    tarif_dasar = 0.15
                
                # Adjust for NPWP
                tarif_final = tarif_dasar if punya_npwp else tarif_dasar * 2
                
                # Calculate tax
                pph23 = jumlah_bruto * tarif_final
                jumlah_netto = jumlah_bruto - pph23
                
                st.session_state.pph23_result = {
                    'jenis': jenis_penghasilan,
                    'bruto': jumlah_bruto,
                    'tarif': tarif_final * 100,
                    'pph23': pph23,
                    'netto': jumlah_netto,
                    'npwp': punya_npwp
                }
        
        with col2:
            st.markdown("#### Hasil Perhitungan")
            
            if 'pph23_result' in st.session_state:
                result = st.session_state.pph23_result
                
                st.metric("Jumlah Bruto", f"Rp {result['bruto']:,.0f}")
                st.metric("Tarif PPh 23", f"{result['tarif']:.1f}%")
                st.metric("PPh 23", f"Rp {result['pph23']:,.0f}")
                st.metric("Jumlah Netto", f"Rp {result['netto']:,.0f}")
                
                if not result['npwp']:
                    st.warning("⚠️ Tarif dinaikkan 100% karena tidak memiliki NPWP")
                
                st.markdown("---")
                
                detail_df = pd.DataFrame({
                    'Keterangan': ['Jenis Penghasilan', 'Jumlah Bruto', 'Tarif', 'PPh 23', 'Jumlah Netto'],
                    'Nilai': [
                        result['jenis'],
                        f"Rp {result['bruto']:,.0f}",
                        f"{result['tarif']:.1f}%",
                        f"Rp {result['pph23']:,.0f}",
                        f"Rp {result['netto']:,.0f}"
                    ]
                })
                
                st.dataframe(detail_df, use_container_width=True, hide_index=True)
            else:
                st.info("👈 Masukkan data dan klik tombol Hitung untuk melihat hasil")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # PPN Calculator
    with tax_tab[2]:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📊 Kalkulator PPN - Pajak Pertambahan Nilai")
        st.caption("Hitung Pajak Pertambahan Nilai 11%")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Input Data")
            
            jenis_hitung = st.radio(
                "Jenis Perhitungan",
                ["Harga Belum Termasuk PPN", "Harga Sudah Termasuk PPN"]
            )
            
            jumlah = st.number_input(
                "Jumlah (Rp)",
                min_value=0,
                value=10000000,
                step=100000,
                format="%d"
            )
            
            tarif_ppn = st.selectbox(
                "Tarif PPN",
                ["11% (Tarif Standar 2022-sekarang)", "12% (Rencana 2025)"]
            )
            
            if st.button("🧮 Hitung PPN", use_container_width=True):
                tarif = 0.11 if "11%" in tarif_ppn else 0.12
                
                if jenis_hitung == "Harga Belum Termasuk PPN":
                    dpp = jumlah
                    ppn = dpp * tarif
                    harga_total = dpp + ppn
                else:
                    harga_total = jumlah
                    dpp = harga_total / (1 + tarif)
                    ppn = harga_total - dpp
                
                st.session_state.ppn_result = {
                    'jenis': jenis_hitung,
                    'tarif': tarif * 100,
                    'dpp': dpp,
                    'ppn': ppn,
                    'total': harga_total
                }
        
        with col2:
            st.markdown("#### Hasil Perhitungan")
            
            if 'ppn_result' in st.session_state:
                result = st.session_state.ppn_result
                
                st.metric("DPP (Dasar Pengenaan Pajak)", f"Rp {result['dpp']:,.0f}")
                st.metric("PPN", f"Rp {result['ppn']:,.0f}", delta=f"{result['tarif']:.0f}%")
                st.metric("Harga Total", f"Rp {result['total']:,.0f}")
                
                # Visualization
                fig = go.Figure(data=[go.Pie(
                    labels=['DPP', 'PPN'],
                    values=[result['dpp'], result['ppn']],
                    hole=.4,
                    marker_colors=['#667eea', '#764ba2']
                )])
                
                fig.update_layout(
                    title="Komposisi Harga",
                    height=300,
                    showlegend=True
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("👈 Masukkan data dan klik tombol Hitung untuk melihat hasil")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # PPh Badan Calculator
    with tax_tab[3]:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📊 Kalkulator PPh Badan - Pajak Perusahaan")
        st.caption("Hitung pajak penghasilan perusahaan")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Input Data Keuangan")
            
            omzet = st.number_input(
                "Omzet/Peredaran Bruto Tahunan (Rp)",
                min_value=0,
                value=1000000000,
                step=10000000,
                format="%d"
            )
            
            biaya = st.number_input(
                "Biaya Operasional (Rp)",
                min_value=0,
                value=500000000,
                step=10000000,
                format="%d"
            )
            
            penghasilan_lain = st.number_input(
                "Penghasilan Lain (Rp)",
                min_value=0,
                value=0,
                step=1000000,
                format="%d"
            )
            
            koreksi_fiskal = st.number_input(
                "Koreksi Fiskal (Rp)",
                value=0,
                step=1000000,
                format="%d",
                help="Positif untuk menambah, negatif untuk mengurangi"
            )
            
            is_umkm = st.checkbox("UMKM (Omzet < 4.8 Miliar)", value=False)
            
            if st.button("🧮 Hitung PPh Badan", use_container_width=True):
                # Calculate taxable income
                laba_kotor = omzet - biaya + penghasilan_lain
                laba_fiskal = laba_kotor + koreksi_fiskal
                
                # Calculate tax
                if is_umkm and omzet <= 4800000000:
                    # UMKM gets special rate
                    if laba_fiskal <= 500000000:
                        pph_badan = laba_fiskal * 0.11
                    else:
                        pph_badan = 500000000 * 0.11 + (laba_fiskal - 500000000) * 0.22
                else:
                    pph_badan = laba_fiskal * 0.22
                
                laba_netto = laba_fiskal - pph_badan
                
                st.session_state.pph_badan_result = {
                    'omzet': omzet,
                    'biaya': biaya,
                    'laba_kotor': laba_kotor,
                    'koreksi': koreksi_fiskal,
                    'laba_fiskal': laba_fiskal,
                    'pph_badan': pph_badan,
                    'laba_netto': laba_netto,
                    'is_umkm': is_umkm
                }
        
        with col2:
            st.markdown("#### Hasil Perhitungan")
            
            if 'pph_badan_result' in st.session_state:
                result = st.session_state.pph_badan_result
                
                st.metric("Laba Kotor", f"Rp {result['laba_kotor']:,.0f}")
                st.metric("Laba Fiskal (PKP)", f"Rp {result['laba_fiskal']:,.0f}")
                st.metric("PPh Badan", f"Rp {result['pph_badan']:,.0f}",
                         delta=f"{(result['pph_badan']/result['laba_fiskal']*100):.2f}%" if result['laba_fiskal'] > 0 else "0%")
                st.metric("Laba Netto", f"Rp {result['laba_netto']:,.0f}")
                
                if result['is_umkm']:
                    st.success("✅ Mendapat fasilitas tarif UMKM")
                
                st.markdown("---")
                
                # Breakdown
                detail_df = pd.DataFrame({
                    'Keterangan': [
                        'Omzet',
                        'Biaya Operasional',
                        'Laba Kotor',
                        'Koreksi Fiskal',
                        'Laba Fiskal',
                        'PPh Badan',
                        'Laba Netto'
                    ],
                    'Jumlah (Rp)': [
                        f"{result['omzet']:,.0f}",
                        f"({result['biaya']:,.0f})",
                        f"{result['laba_kotor']:,.0f}",
                        f"{result['koreksi']:,.0f}",
                        f"{result['laba_fiskal']:,.0f}",
                        f"({result['pph_badan']:,.0f})",
                        f"{result['laba_netto']:,.0f}"
                    ]
                })
                
                st.dataframe(detail_df, use_container_width=True, hide_index=True)
            else:
                st.info("👈 Masukkan data dan klik tombol Hitung untuk melihat hasil")
        
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "🏭 Biaya Produksi":
    st.markdown("""
    <div class="main-header">
        <h1>🏭 Manajemen Biaya Produksi</h1>
        <p>Analisis biaya produksi dan tentukan harga jual yang optimal</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Input Biaya Produksi")
        
        st.markdown("#### 📦 Biaya Bahan Baku Langsung")
        bahan_baku = st.number_input("Bahan Baku (Rp)", min_value=0, value=0, step=1000)
        kemasan = st.number_input("Kemasan (Rp)", min_value=0, value=0, step=1000)
        
        st.markdown("#### 👷 Biaya Tenaga Kerja Langsung")
        upah = st.number_input("Upah Tenaga Kerja (Rp)", min_value=0, value=0, step=1000)
        
        st.markdown("#### ⚙️ Biaya Overhead Pabrik")
        listrik = st.number_input("Listrik & Air (Rp)", min_value=0, value=0, step=1000)
        sewa = st.number_input("Sewa Pabrik (Rp)", min_value=0, value=0, step=1000)
        pemeliharaan = st.number_input("Pemeliharaan Mesin (Rp)", min_value=0, value=0, step=1000)
        depresiasi = st.number_input("Depresiasi (Rp)", min_value=0, value=0, step=1000)
        
        st.markdown("#### 📊 Target & Volume")
        volume = st.number_input("Volume Produksi (Unit)", min_value=1, value=100, step=1)
        target_margin = st.number_input("Target Margin Keuntungan (%)", min_value=0, max_value=100, value=30, step=1)
        
        if st.button("🧮 Hitung Biaya Produksi", use_container_width=True):
            # Calculate costs
            total_bahan_baku = bahan_baku + kemasan
            total_tenaga_kerja = upah
            total_overhead = listrik + sewa + pemeliharaan + depresiasi
            
            total_biaya = total_bahan_baku + total_tenaga_kerja + total_overhead
            biaya_per_unit = total_biaya / volume if volume > 0 else 0
            
            harga_jual = biaya_per_unit * (1 + target_margin/100)
            keuntungan_per_unit = harga_jual - biaya_per_unit
            keuntungan_total = keuntungan_per_unit * volume
            
            st.session_state.production_result = {
                'bahan_baku': total_bahan_baku,
                'tenaga_kerja': total_tenaga_kerja,
                'overhead': total_overhead,
                'total_biaya': total_biaya,
                'volume': volume,
                'biaya_per_unit': biaya_per_unit,
                'margin': target_margin,
                'harga_jual': harga_jual,
                'keuntungan_per_unit': keuntungan_per_unit,
                'keuntungan_total': keuntungan_total
            }
    
    with col2:
        st.markdown("### 📊 Hasil Analisis")
        
        if 'production_result' in st.session_state:
            result = st.session_state.production_result
            
            # Key Metrics
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Total Biaya Produksi", f"Rp {result['total_biaya']:,.0f}")
                st.metric("Biaya per Unit", f"Rp {result['biaya_per_unit']:,.0f}")
            
            with col_b:
                st.metric("Harga Jual Optimal", f"Rp {result['harga_jual']:,.0f}")
                st.metric("Keuntungan Total", f"Rp {result['keuntungan_total']:,.0f}")
            
            st.markdown("---")
            
            # Cost Breakdown Chart
            st.markdown("#### Breakdown Biaya")
            
            fig = go.Figure(data=[go.Pie(
                labels=['Bahan Baku', 'Tenaga Kerja', 'Overhead'],
                values=[result['bahan_baku'], result['tenaga_kerja'], result['overhead']],
                hole=.4,
                marker_colors=['#667eea', '#764ba2', '#f093fb']
            )])
            
            fig.update_layout(
                height=300,
                showlegend=True,
                margin=dict(t=0, b=0, l=0, r=0)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed Table
            st.markdown("#### Detail Biaya")
            detail_df = pd.DataFrame({
                'Kategori': ['Bahan Baku', 'Tenaga Kerja', 'Overhead', 'Total Biaya', 'Biaya/Unit', 'Harga Jual', 'Keuntungan/Unit'],
                'Jumlah (Rp)': [
                    f"{result['bahan_baku']:,.0f}",
                    f"{result['tenaga_kerja']:,.0f}",
                    f"{result['overhead']:,.0f}",
                    f"{result['total_biaya']:,.0f}",
                    f"{result['biaya_per_unit']:,.0f}",
                    f"{result['harga_jual']:,.0f}",
                    f"{result['keuntungan_per_unit']:,.0f}"
                ]
            })
            
            st.dataframe(detail_df, use_container_width=True, hide_index=True)
            
            # Download
            st.download_button(
                "📥 Download Analisis (CSV)",
                detail_df.to_csv(index=False).encode('utf-8'),
                "analisis_biaya_produksi.csv",
                "text/csv",
                use_container_width=True
            )
        else:
            st.info("👈 Masukkan data biaya dan klik tombol Hitung untuk melihat analisis")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "📞 Kontak":
    st.markdown("""
    <div class="main-header">
        <h1>📞 Hubungi Kami</h1>
        <p>Konsultasi gratis untuk kebutuhan perpajakan Anda</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 📍 Informasi Kontak")
        
        st.markdown("""
        **📞 Telepon**  
        +62 812-3456-7890
        
        **📧 Email**  
        konsultasi@taxpro.id
        
        **📍 Alamat**  
        Jakarta, Indonesia
        
        **🕐 Jam Operasional**  
        Senin - Jumat: 09.00 - 17.00 WIB
        """)
        
        st.markdown("### 🔗 Media Sosial")
        col_a, col_b, col_c, col_d = st.columns(4)
        with col_a:
            st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6281234567890)")
        with col_b:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)")
        with col_c:
            st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com)")
        with col_d:
            st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com)")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### ✉️ Kirim Pesan")
        
        with st.form("contact_form"):
            nama = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            telepon = st.text_input("Nomor Telepon")
            subjek = st.selectbox("Subjek", ["Konsultasi Pajak", "Pelaporan SPT", "Pembukuan", "Lainnya"])
            pesan = st.text_area("Pesan", height=150)
            
            submitted = st.form_submit_button("📤 Kirim Pesan", use_container_width=True)
            
            if submitted:
                if nama and email and telepon and pesan:
                    st.success("✅ Pesan Anda telah terkirim! Kami akan menghubungi Anda segera.")
                else:
                    st.error("❌ Mohon lengkapi semua field")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: white;'>
    <p style='font-size: 0.9rem; opacity: 0.8;'>
        © 2026 TaxPro Indonesia. All rights reserved.<br>
        <small>Disclaimer: Kalkulator ini adalah alat bantu estimasi. Untuk perhitungan resmi, silakan konsultasikan dengan konsultan pajak profesional.</small>
    </p>
</div>
""", unsafe_allow_html=True)
