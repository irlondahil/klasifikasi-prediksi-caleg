# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:55:18 2024

@author: IRLON
"""

# Mengimpor library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import streamlit.components.v1 as components

# Load model
my_model = pickle.load(open('model_klasifikasi_caleg.pkl', 'rb'))

df = pd.read_excel('datapemilukpu.xlsx')

# Set page configuration
st.set_page_config(layout="wide")

# Create the sidebar menu
with st.sidebar:
    st.title("Klasifikasi Prediksi  Caleg Terpilih atau Tidak")
    components.html("""<hr>""", height=100)
    selected_option = option_menu(
        menu_title="Main Menu",
        options=["Home", "Exploratory Data Analysis (EDA) Visualization", "Matrix Korelasi","Prediksi Upload File", "Prediksi Input Data"],
        icons=["house", "bar-chart", "bar-chart", "upload", "keyboard"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )
  

if selected_option == "Home":
   st.title("Welcome")
   components.html("""<hr>""", height=100)
   st.write("Di aplikasi ini anda dapat memprediksi calon legeslatif terpilih atau tidak dengan memasukan berapa data yang diperlukan")
elif selected_option == "Exploratory Data Analysis (EDA) Visualization":
        sub_selected = option_menu(
            menu_title="EDA Menu",
            options=["Total Suara Partai Politik",
                     "Top 10 Calon dari total suara",
                     "Distribusi Jenis Kelamin Calon",
                     "Tingkat Keberhasilan Calon",
                     "Total Suara  Daerah Pemilihan",
                     "Distribusi Suara Sah per Partai"],
            icons=["bar-chart", "bar-chart","pie-chart", "pie-chart","bar-chart", "graph-up"],
            default_index=0,
            orientation="horizontal", 
            
        )
        if sub_selected == "Total Suara berdasarkan Partai Politik":
            st.subheader('Total Suara berdasarkan Partai Politik')
            components.html("""<hr>""", height=100)
            # Menghitung total suara per partai politik
            suara_per_partai = df.groupby('NAMA PARTAI POLITIK')['SUARA SAH PARTAI'].sum().sort_values(ascending=False)
            
            # Membuat plot bar menggunakan Seaborn
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=suara_per_partai.index, y=suara_per_partai.values, color='skyblue', ax=ax)
            
            # Menambahkan judul, label sumbu, dan rotasi label sumbu x
            ax.set_title('Total Suara berdasarkan Partai Politik')
            ax.set_ylabel('Total Suara')
            ax.set_xlabel('Partai Politik')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            
            # Menampilkan plot
            st.pyplot(fig)
        elif sub_selected == "Top 10 Calon berdasarkan Total Suara":
            # Menampilkan sub-judul
            st.subheader('Top 10 Calon berdasarkan Total Suara')
            components.html("""<hr>""", height=100)
            
            # Menghitung total suara untuk setiap calon legislatif
            suara_per_calon = df.groupby('NAMA CALON LEGESLATIF')['SUARA SAH CALEG'].sum().sort_values(ascending=False).head(10)
            
            # Membuat plot bar untuk menampilkan 10 calon dengan total suara terbanyak
            fig2, ax2 = plt.subplots(figsize=(12, 6))
            suara_per_calon.plot(kind='bar', color='orange', ax=ax2)
            
            # Menambahkan judul, label sumbu x dan y
            ax2.set_title('Top 10 Calon berdasarkan Total Suara')
            ax2.set_ylabel('Total Suara')
            ax2.set_xlabel('Calon')
            
            # Memutar label sumbu x agar lebih mudah dibaca
            ax2.set_xticklabels(suara_per_calon.index, rotation=45, ha='right')
            
            # Menampilkan plot di Streamlit
            st.pyplot(fig2)
        elif sub_selected == "Distribusi Jenis Kelamin Calon":
            st.subheader('Distribusi Jenis Kelamin Calon')
            components.html("""<hr>""", height=100)
            distribusi_jenis_kelamin = df['JENIS KELAMIN'].value_counts()
            fig3, ax3 = plt.subplots(figsize=(6, 6))
            distribusi_jenis_kelamin.plot(kind='pie', labels=['Laki-Laki', 'Perempuan'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140, ax=ax3)
            ax3.set_title('Distribusi Jenis Kelamin Calon')
            ax3.set_ylabel('')
            st.pyplot(fig3)
        elif sub_selected == "Tingkat Keberhasilan Calon":
            st.subheader('Tingkat Keberhasilan Calon')
            components.html("""<hr>""", height=100)
            tingkat_keberhasilan = df['TERPILIH ATAU TIDAK'].value_counts()
            fig4, ax4 = plt.subplots(figsize=(6, 6))
            tingkat_keberhasilan.plot(kind='pie', labels=['Tidak Terpilih', 'Terpilih'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140, ax=ax4)
            ax4.set_title('Tingkat Keberhasilan Calon')
            ax4.set_ylabel('')
            st.pyplot(fig4)           
        elif sub_selected == "Total Suara berdasarkan Daerah Pemilihan":
            st.subheader('Total Suara berdasarkan Daerah Pemilihan')
            components.html("""<hr>""", height=100)
            suara_per_dapil = df.groupby('DAERAH PEMILIHAN')['SUARA SAH PARTAI'].sum().sort_values(ascending=False)
            fig5, ax5 = plt.subplots(figsize=(10, 6))
            suara_per_dapil.plot(kind='bar', color='green', ax=ax5)
            ax5.set_title('Total Suara berdasarkan Daerah Pemilihan')
            ax5.set_ylabel('Total Suara')
            ax5.set_xlabel('Daerah Pemilihan')
            ax5.set_xticklabels(suara_per_dapil.index, rotation=45, ha='right')
            st.pyplot(fig5)
        elif sub_selected == "Distribusi Suara Sah per Partai":
            st.subheader('Distribusi Suara Sah per Partai')
            components.html("""<hr>""", height=100)
            fig1, ax1 = plt.subplots(figsize=(12, 6))
            sns.boxplot(x='NAMA PARTAI POLITIK', y='SUARA SAH CALEG', data=df, ax=ax1)
            ax1.set_title('Box Plot Suara Sah per Partai')
            ax1.set_ylabel('Suara Sah Caleg')
            ax1.set_xlabel('Partai Politik')
            ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
            st.pyplot(fig1)
elif selected_option  =="Matrix Korelasi":
        st.subheader('Matriks Korelasi')
        components.html("""<hr>""", height=100)
        df_numeric = df.select_dtypes(include=[float, int])
        
        # Menghitung matriks korelasi
        correlation_matrix = df_numeric.corr()
        
        # Membuat heatmap dengan Seaborn
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='Reds', ax=ax)
        ax.set_title('Matriks Korelasi')
        st.pyplot(fig)
elif selected_option  == "Prediksi Upload File":
        st.title("Halaman Prediksi Upload File")
        components.html("""<hr>""", height=100)
        # Mengupload file
        
        upload_file = st.file_uploader('Pilih file xlsx atau csv', type=['xlsx', 'csv'])

        if upload_file is not None:
            # Memeriksa jenis file
            if upload_file.name.endswith('.xlsx'):
                dataku = pd.read_excel(upload_file)
                st.write(dataku)
                st.success('File Excel berhasil diupload')
                hasil = my_model.predict(dataku)
                #st.write('Prediksi',hasil)
                # Keputusan
                for i in range(len(hasil)):
                    if hasil[i] == 1:
                          st.write('Calon Legeslatif',dataku['NAMA CALON LEGESLATIF'][i],'= TERPILIH')
                    else:
                          st.write('Calon Legeslatif',dataku['NAMA CALON LEGESLATIF'][i],'= TIDAK TERPILIH')
                
            elif upload_file.name.endswith('.csv'):
                dataku = pd.read_csv(upload_file)
                st.write(dataku)
                st.success('File CSV berhasil diupload')
                hasil = my_model.predict(dataku)
                #st.write('Prediksi',hasil)
                # Keputusan
                for i in range(len(hasil)):
                     if hasil[i] == 1:
                           st.write('Calon Legeslatif',dataku['NAMA CALON LEGESLATIF'][i],'= TERPILIH')
                     else:
                           st.write('Calon Legeslatif',dataku['NAMA CALON LEGESLATIF'][i],'= TIDAK TERPILIH')
            else:  
               st.error('Format file tidak dikenali, silakan pilih file xlsx atau csv yang valid')        

elif selected_option  == "Prediksi Input Data":
  st.title("Halaman Prediksi Input Data")
  components.html("""<hr>""", height=100)
  # Baris Pertama
  with st.container():
      col1, col2 = st.columns(2)
      # Ambil nilai unik dari kolom 'nama_field'
      unique_values = set(df['NAMA PARTAI POLITIK'])
      with col1:
          Nama_Partai = st.selectbox('Nama Partai',unique_values )
      with col2:
          Nama_Caleg = st.text_input('Nama Calon Legeslatif', value='Budi')

          
  # Baris Kedua
  with st.container():
      col1, col2 = st.columns(2)
      with col1:
          Jenis_Kelamin = st.selectbox('Jenis Kelamin', ['Laki-Laki','Perempuan'])
          if Jenis_Kelamin =='Laki-Laki':
              Jenis_Kelamin ='L'
          else:
             Jenis_Kelamin ='P'
      with col2:
          unique_values = set(df['KECAMATAN'])
          Kecamatan = st.selectbox('KECAMATAN',unique_values ) 

  # Baris Ketiga
  with st.container():
      col1, col2, col3 = st.columns(3)
      with col1:
          Suara_Sah_Partai = st.number_input('SUARA SAH PARTAI', value = 48)
      with col2:
          unique_values = set(df['JUML.PEROLEHAN KURSI'])
          Jumlah_Perolehan_Suara = st.selectbox('JUML.PEROLEHAN KURSI',unique_values )        
      with col3:
          unique_values = set(df['DAERAH PEMILIHAN'])
          Daerah_Pemilihan = st.selectbox('DAERAH PEMILIHAN',unique_values)    
          

  # Baris Keempat
  with st.container():
      col1, col2, col3 = st.columns(3)
      with col1:
          unique_values = set(df['NO.URUT CALEG'])
          No_Urut_Caleg = st.selectbox('No Urut Caleg',unique_values)
      with col2:
          Suara_Sah_Caleg = st.number_input('SUARA SAH CALEG', value = 48)
      
     # Menambah tombol
  if st.button('Prediksi'):

         data = {
                  'NAMA PARTAI POLITIK': Nama_Partai,
                  'NAMA CALON LEGESLATIF': Nama_Caleg,
                  'JENIS KELAMIN': Jenis_Kelamin,
                  'KECAMATAN': Kecamatan,
                  'SUARA SAH PARTAI': Suara_Sah_Partai,
                  'JUML.PEROLEHAN KURSI': Jumlah_Perolehan_Suara,
                  'DAERAH PEMILIHAN': Daerah_Pemilihan, 
                  'NO.URUT CALEG': No_Urut_Caleg,
                  'SUARA SAH CALEG': Suara_Sah_Caleg
                  }
        
          # Tabel data
         kolom = list(data.keys())
         df = pd.DataFrame([data.values()], columns=kolom)
          
          # Melakukan prediksi
         hasil = my_model.predict(df)
         keputusan = ''
         if hasil == 0:
             keputusan = 'Tidak Terpilih'
         else:
              keputusan = 'Terpilih'
        
          # Memunculkan hasil di Web 
          #st.write(hasil[0])
         st.write('<center><b><h3>Nama Calon Legeslatif', str(Nama_Caleg),'</b></h3>', unsafe_allow_html=True)
         st.write('<center><b><h3>Diprediksi = ', keputusan,'</b></h3>', unsafe_allow_html=True)
