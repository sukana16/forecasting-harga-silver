import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('prediksiopen.sav', 'rb'))

df = pd.read_excel("opendate.xlsx")
df['Date'] = pd.to_datetime(df['Date'], format='%Y')
df.set_index(['Date'], inplace=True)

st.title('Prediksi Harga Silver')
year = st.slider("Tentukan Tahun",1,30, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['Open'], index=pd.date_range(start=df.index[-1], periods=year, freq='Y'))

if st.button("Prediksi"):
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['Open'].plot(style="--", color='gray', legend=True, label='known')
        pred['Open'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)
plt.show()