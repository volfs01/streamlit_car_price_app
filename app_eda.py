import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda_app() :
    df = pd.read_csv('data/Car_Purchasing_Data.csv' , encoding='iso-8859-1')
    
    st.subheader('데이터 프레임 확인')
    st.dataframe(df.head(2))
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())
    
    # 컬럼을 선택할 수 있게 한다. 하나의 컬럼으 선택하면 
    # 해당 컬럼의 최대값 ,최소값 데이터를 화면에 보여준다.
    st.subheader('최대/최소 데이터 확인하기')
    column_list = df.columns[4:]
    selected_coulmn = st.selectbox('컬럼을 선택하시오',column_list)
    df_max = df.loc[df[selected_coulmn] ==df[selected_coulmn].max() , : ]
    df_min = df.loc[df[selected_coulmn] ==df[selected_coulmn].min() , : ]
    
    st.text('최대 데이터')
    st.dataframe(df_max)
    st.text('최소 데이터')
    st.dataframe(df_min)
    
    st.subheader('컬럼별 히스토그램')
    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요' , column_list)
    bins_count = st.number_input('빈의 개수를 입력하세요' , 10 ,30 , value=10,step=1)
    
    fig1 = plt.figure()
    plt.hist(data=df , x=histogram_column , rwidth=0.8 ,bins=bins_count )
    plt.title(histogram_column + ' Histogram')
    plt.xlabel(histogram_column)
    plt.ylabel('count')
    st.pyplot(fig1)     
    
    st.subheader('상관 관계 분석')
    column_list2 = df.columns[3 : ]
    choice2 = st.multiselect('컬럼을 선택하시오' , column_list2)
    
    if len(choice2) > 1 :
        
        df_corr = df[choice2].corr()
        fig2 = plt.figure()
        sb.heatmap(data=df_corr , annot=True , fmt='.2f' , cmap='coolwarm' , vmin= -1 , vmax=1 , linewidths=0.5 )
        st.pyplot(fig2)