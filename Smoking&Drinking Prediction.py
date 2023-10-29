import pickle
import streamlit as st

model = pickle.load(open('smoking_driking_dataset_Ver01.sav','rb'))

st.title(smoking and drinking data)
sex	= st.number_input('input sex')
age	= st.number_input('input age')
height	= st.number_input('input height')
weight	= st.number_input('input weight')
waistline	= st.number_input('input waistline')
sight_left	= st.number_input('input sight_left')
sight_right	= st.number_input('input sight_right')
hear_left	= st.number_input('input hear_left')
hear_right = st.number_input('input hear_right')
SBP	= st.number_input('input SBP')
DBP	= st.number_input('input DBP')
HDL_chole	= st.number_input('input HDL_chole')
LDL_chole	= st.number_input('LDL_chole')
triglyceride	= st.number_input('input triglyceride')
hemoglobin	= st.number_input('input hemoglobin')
urine_protein=	= st.number_input('input urine_protein')
serum_creatinine 	= st.number_input('input serum_creatinine')
SGOT_AST	= st.number_input('input SGOT_AST')
SGOT_ALT	= st.number_input('input SGOT_ALT')
gamma_GTP	= st.number_input('input gamma_GTP')
SMK_stat_type_cd = st.number_input('input SMK_stat_type_cd')

predict = ''

if st.button('Cek Analisis sinyal tubuh Klasifikasi perokok'):
    predict = model.predict(
        [[residual_sugar, pH, alcohol, chlorides, sulphates, fixed_acidity, volatile_acidity, citric_acid, free_sulfur_dioxide, total_sulfur_dioxide, density]]
    )
    st.write('Estimasi smoking & driking:', predict)