import numpy as np
import pickle
import streamlit as st
import pandas as pd


# loading the saved model
#model = pickle.load(open('D:/Projects/Mini Project/Application/diabetes_prediction.pkl', 'rb'))
pickle_in = open("random_forest_model.pkl","rb")
model=pickle.load(pickle_in)

ssc_min = 75
ssc_max = 100
inter_min = 60
inter_max = 98.4
btech_min = 54.03
btech_max = 94.23
ip_min = 41
ip_max = 99
psp_min = 40
psp_max = 96
elcs_min = 46
elcs_max = 90
eng1_min = 40
eng1_max = 87
ds_min = 40
ds_max = 94
os_min = 40
os_max = 98
dbms_min = 44
dbms_max = 96
oopc_min = 40
oopc_max = 95
cn_min = 41
cn_max = 97
wt_min = 41
wt_max = 99
package_min = 350000
package_max = 2936000



st.title('Campus Placements Prediction')

list_of_columns=['SSC', 'Inter', 'B.Tech 3-1', 'IP', 'PSP', 'ELCS LAB',
                'ENGLISH 1', 'DS', 'OS', 'DBMS', 'OOPC', 'CN', 'WT', 'Package']

input_data=pd.DataFrame(columns=list_of_columns)
input_data.drop(['Package'], axis='columns',inplace=True)

input_data.at[0, 'SSC'] = st.slider('SSC Percentage : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'Inter'] = st.slider('Inter Percenatge : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'B.Tech 3-1'] = st.slider('B.tech Percenatge : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'IP'] = st.slider('IP Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'PSP'] = st.slider('PSP Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'ELCS LAB'] = st.slider('ELCS Lab Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'ENGLISH 1'] = st.slider('English 1 : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'DS'] = st.slider('DS Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'OS'] = st.slider('OS Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'DBMS'] = st.slider('DBMS Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'OOPC'] = st.slider('OOPC Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'CN'] = st.slider('CN Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'WT'] = st.slider('WT Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
# De-normalisation
input_data['SSC']=(input_data['SSC']-ssc_min)/(ssc_max-ssc_min)
input_data['Inter']=(input_data['Inter']-inter_min)/(inter_max-inter_min)
input_data['B.Tech 3-1']=(input_data['B.Tech 3-1']-btech_min)/(btech_max-btech_min)
input_data['IP']=(input_data['IP']-ip_min)/(ip_max-ip_min)
input_data['PSP']=(input_data['PSP']-psp_min)/(psp_max-psp_min)
input_data['ELCS LAB']=(input_data['ELCS LAB']-elcs_min)/(elcs_max-elcs_min)
input_data['ENGLISH 1']=(input_data['ENGLISH 1']-eng1_min)/(eng1_max-eng1_min)
input_data['DS']=(input_data['DS']-ds_min)/(ds_max-ds_min)
input_data['OS']=(input_data['OS']-os_min)/(os_max-os_min)
input_data['DBMS']=(input_data['DBMS']-dbms_min)/(dbms_max-dbms_min)
input_data['OOPC']=(input_data['OOPC']-oopc_min)/(oopc_max-oopc_min)
input_data['CN']=(input_data['CN']-cn_min)/(cn_max-cn_min)
input_data['WT']=(input_data['WT']-wt_min)/(wt_max-wt_min)


if st.button("Predict the Package"):
    result =  model.predict(input_data)
    Package=result*(package_max-package_min)+package_min
    st.text('Predicted  Package = ')
    st.text(Package)