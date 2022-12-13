import streamlit as st 
import numpy as np
import joblib
def run_ml_app() :
    st.subheader('자동차 금액 예측')
    
    # 성별,나이,연봉,카드빛,자산을 유저에게 입력받아
    # 자동차 구매 금액을 예측하시오
    input1 = st.number_input('성별을 입력하시오',0,1)
    st.text('여자는 0')
    input2 = st.number_input('나이을 입력하시오',1,1000000)
    input3 = st.number_input('연봉을 입력하시오',1,1000000)
    input4 = st.number_input('카드빛을 입력하시오',1,1000000)
    input5 = st.number_input('자산을 입력하시오',1,1000000)
    
    new_data = np.array([input1 , input2 ,input3 , input4 , input5])
    new_data = new_data.reshape(1,5)
    regressor = joblib.load('regressor.pkl')
    st.subheader('예측값')
    st.text(regressor.predict(new_data))