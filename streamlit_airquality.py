import pickle
import streamlit as st
import tensorflow as tf
from tensorflow import keras

def load_model() :
    model = tf.keras.model.load_model("airqualityml.hdf5")
    return model
with st.spinner ("loading model"):
    model = load_model()

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)
    
#judul web
st.title ("Prediksi Dampak Kualitas Udara terhadap Kesehatan")

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Air_Quality_Index = st.text_input ('Berapakah AQI (Air Quality Index) atau Indeks Kualitas Udara?')

with col2 :
    PM10 = st.text_input('Berapakah PM10 atau partikel udara yang berukuran lebih kecil dari 10 mikron(μg/m³)?')

with col1 :
    PM2_5 = st.text_input('Berapakah PM2.5 atau  partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5 mikron (μg/m³)?')

with col2 :
    NO2 = st.text_input("Berapakah konsentrasi dari Nitrogen Dioksida (ppb)?)")

with col1 :
    SO2 = st.text_input("Berapakah konsentrasi dari Sulfur Dioksida (ppb)??")

with col2 :
    O3 = st.text_input("Berapakah konsentrasi dari Ozone (ppb)??")

with col1 :
    Temp = st.text_input("Berapakah temperatur saat ini dalam Celcius?")

with col2 :
    Hum = st.text_input("Berapakah persentase kelembapan udara?")
    
with col1 :
    Wind = st.text_input("Berapakah kecepatan udara dalam meter/detik (m/s)?")

with col2 :
    Rep = st.text_input("Berapakah jumlah kasus penyakit pernapasan yang dilaporkan?")

with col1 :
    Cardio = st.text_input("Berapakah jumlah kasus penyakit cardiovascular yang dilaporkan?")

with col2 :
    HosAd = st.text_input("Berapakah Jumlah pasien rawat inap yang dilaporkan?") 


# code untuk prediksi
airq_diagnosis = ''

#membuat tombol untuk prediksi
if st.button ('Test Prediksi Dampak Kualtas Udara'):
    airq_diagnosis = model.predict([[Air_Quality_Index, PM10, PM2_5, NO2, SO2, O3, Temp, Hum, Wind, Rep, Cardio, HosAd]])

    if(airq_diagnosis[0] == 0) :
        airq_diagnosis = 'Kualitas Udara berdampak Sangat Buruk untuk kesehatan anda'
    elif(airq_diagnosis[0] == 1) :
        airq_diagnosis = 'Kualitas Udara berdampak Buruk untuk kesehatan anda'
    elif(airq_diagnosis[0] == 2) :
        airq_diagnosis = 'Kualitas Udara berdampak Sedang untuk kesehatan anda'
    elif(airq_diagnosis[0] == 3) :
        airq_diagnosis = 'Kualitas Udara berdampak Rendah untuk kesehatan anda'
    else :
        airq_diagnosis = 'Kualitas Udara berdampak Sangat Rendah untuk kesehatan anda'

    st.success(airq_diagnosis)


