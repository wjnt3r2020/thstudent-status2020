import streamlit as st
import pandas as pd
import pickle

st.write("""
# Thai Student Status!
""")
st.write("""
#### Undergraduate (Acadamic 2562-2563)
""")
st.write("""
#### For TCAS 1,3,5
""")

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data:')


def get_input():
    #widgets
    v_HomeRegion = st.sidebar.selectbox('HomeRegion',[ 'Bangkok' , 'Central' , 'East' , 'North' , 'North East' , 'South' , 'West' ])
    v_Sex = st.sidebar.radio('Sex',['Male','Female'])
    
    st.sidebar.selectbox('Faculty details',[ '10:School of Liberal Arts' 
    , '11:School of Science' 
    , '12:School of Management' 
    , '13:School of Information Technology' 
    , '14:School of Agro-industry' 
    , '16:School of Law' 
    , '17:School of Cosmetic Science'
    , '18:School of Health Science'
    , '19:School of Nursing'
    , '21:School of Medicine'
    , '22:School of Dentistry'
    , '23:School of Social Innovation'
    , '24:School of Sinology'
    , '25:School of Integrative Medicine' ])
    v_FacultyID = st.sidebar.select_slider('FacultyID', [10, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 25])
    
    st.sidebar.selectbox('Department details',[ '1006:English' 
    , '1102:Applied Chemistry' 
    , '1105:Biotechnology' 
    , '1112:Materials Engineering' 
    , '1201:Accounting' 
    , '1202:Economics' 
    , '1203:Business Administration'
    , '1205:Tourism Management'
    , '1207:Hospitality Industry Management'
    , '1209:Logistics and Supply Chain Management'
    , '1210:Aviation Business Management'
    , '1301:Information Technology'
    , '1302:Computer Science and Innovation'
    , '1305:Software Engineering'
    , '1401:Food Science and Technology'
    , '1407:Posthavest Technology and Logistics'
    , '1501:Computer Engineering'
    , '1601:Laws'
    , '1701:Cosmetic Science'
    , '1703:Beauty Technology'
    , '1804:Public Health'
    , '1806:Sports and Health Science'
    , '1807:Environmental Health'
    , '1808:Occupational Health and Safety'
    , '1901:Nursing Science'
    , '2101:Medicine'
    , '2201:Dentistry'
    , '2301:International Development'
    , '2401:Chinese Study'
    , '2402:Business Chinese'
    , '2403:Teaching Chinese Language (5 Year)'
    , '2404:Chinese Language and Culture'
    , '2501:Applied Thai Traditional Medicine'
    , '2502:Physical Therapy'
    , '2503:Traditional Chinese Medicine'])
    v_DepartmentCode = st.sidebar.select_slider('DepartmentCode', [1006, 1102, 1105, 1112, 1201, 1202, 1203, 1205, 1207, 1209, 1210,
       1301, 1302, 1305, 1306, 1401, 1407, 1501, 1601, 1701, 1703, 1804,
       1806, 1807, 1808, 1901, 2101, 2201, 2301, 2401, 2402, 2403, 2404,2501, 2502, 2503])
    
    st.sidebar.selectbox('EntryType details',['29:DIRECT ADMISSION BY SCHOOL' 
    , '24:INTERNATIONAL SCHOOL' 
    , '20:DIRECT ADMISSION' 
    , '52:SPECIAL FOR GOOD STUDENT' 
    , '11:QUOTA BY SCHOOL' 
    , '51:SPECIAL TALENT'
    , '67:RE-ID FIRST SEMESTER GPAX 2.00'
    , '68:EP-MEP PROGRAM'
    , '64:DISABLE STUDENT'
    , '58:DIRECT ADMISSION UNDER CONDITION GPAX 2.00 FIRST SEMESTER'
    , '15:QUOTA BY COMMUNITY HOSPITAL'
    , '69:QUOTA FOR SOUTHERN BORDER'])
    v_EntryTypeID = st.sidebar.select_slider('EntryTypeID', [29, 24, 20, 52, 11, 51, 67, 68, 64, 58, 15, 69])
    
    v_TCAS = st.sidebar.select_slider('TCAS',[1, 3, 5] )
    v_GPAX = st.sidebar.slider('GPAX',min_value=0.00, max_value=4.00)

    st.sidebar.write("""#### Expectation for studying in MFU Q1-Q6""")
    v_Q1 = st.sidebar.radio('Q1 beautiful scenary and atmosphere', [0 ,1])
    v_Q2 = st.sidebar.radio('Q2 quality of life', [0,1])
    v_Q3 = st.sidebar.radio('Q3 campus and facilities', [0,1])
    v_Q4 = st.sidebar.radio('Q4 modern and ready-to-use learning support and facilities', [0,1])
    v_Q5 = st.sidebar.radio('Q5 sources of student scholarship', [0,1])
    v_Q6 = st.sidebar.radio('Q6 demand by workforce market', [0,1])

    st.sidebar.write("""#### Source of information for this application Q7-Q22""")
    v_Q7 = st.sidebar.radio('Q7 email', [0,1])
    v_Q8 = st.sidebar.radio('Q8 Facebook Admission@MFU', [0,1])
    v_Q9 = st.sidebar.radio('Q9 Facebook MFU', [0,1])
    v_Q10 = st.sidebar.radio('Q10 Facebook school or major', [0,1])
    v_Q11 = st.sidebar.radio('Q11 Road show', [0,1])
    v_Q12 = st.sidebar.radio('Q12 Family/friend/relative', [0,1])
    v_Q13 = st.sidebar.radio('Q13 school teachers', [0,1])
    v_Q14 = st.sidebar.radio('Q14 education exhibitions', [0,1])
    v_Q15 = st.sidebar.radio('Q15 tutor schools', [0,1])
    v_Q16 = st.sidebar.radio('Q16 television/Youtube channel', [0,1])
    v_Q17 = st.sidebar.radio('Q17 advertisement in radio/newspaper/other publications', [0,1])
    v_Q18 = st.sidebar.radio('Q18 other sources', [0,1])
    v_Q19 = st.sidebar.radio('Q19 https://admission.mfu.ac.th', [0,1])
    v_Q20 = st.sidebar.radio('Q20 https://www.mfu.ac.th', [0,1])
    v_Q21 = st.sidebar.radio('Q21 other educational websites', [0,1])
    v_Q22 = st.sidebar.radio('Q22 telephone/personal contact', [0,1])

    st.sidebar.write("""#### Factor to apply for MFU Q23-Q33""")
    v_Q23 = st.sidebar.radio('Q23 easy/convenient transportation', [0,1])
    v_Q24 = st.sidebar.radio('Q24 suitable cost', [0,1])
    v_Q25 = st.sidebar.radio('Q25 graduates with higher language/academic competency than other universities', [0,1])
    v_Q26 = st.sidebar.radio('Q26 learning in English', [0,1])
    v_Q27 = st.sidebar.radio('Q27 quality/reputation of university', [0,1])
    v_Q28 = st.sidebar.radio('Q28 excellence in learning support and facilities', [0,1])
    v_Q29 = st.sidebar.radio('Q29 provision of preferred major', [0,1])
    v_Q30 = st.sidebar.radio('Q30 environment and setting motivate learning', [0,1])
    v_Q31 = st.sidebar.radio('Q31 experienced and high-quality instructors', [0,1])
    v_Q32 = st.sidebar.radio('Q32 suggestion by school teacher/friend/relative', [0,1])
    v_Q33 = st.sidebar.radio('Q33 suggestion by family', [0,1])

    st.sidebar.write("""#### If your application fails, will you try again? Q34-Q36""")
    v_Q34 = st.sidebar.radio('Q34 try the same major', [0,1])
    v_Q35 = st.sidebar.radio('Q35 try a different major', [0,1])
    v_Q36 = st.sidebar.radio('Q36 will not try again', [0,1])

    st.sidebar.write("""#### Reason for apply for the major Q37-Q42""")
    v_Q37 = st.sidebar.radio('Q37 suggestion by school teacher', [0,1])
    v_Q38 = st.sidebar.radio('Q38 suggestion by family', [0,1])
    v_Q39 = st.sidebar.radio('Q39 personal preference', [0,1])
    v_Q40 = st.sidebar.radio('Q40 chance of getting a job after graduation', [0,1])
    v_Q41 = st.sidebar.radio('Q41 less competitive than other universities', [0,1])
    v_Q42 = st.sidebar.radio('Q42 suggestion by friend/relative/others', [0,1])
 
    #dictionary
    data = {
            'HomeRegion': v_HomeRegion,
            'Sex': v_Sex,     
            'FacultyID': v_FacultyID,
            'DepartmentCode': v_DepartmentCode,
            'EntryTypeID': v_EntryTypeID,
            'TCAS': v_TCAS,
            'GPAX': v_GPAX,
            'Q1': v_Q1,
            'Q2': v_Q2,
            'Q3': v_Q3,
            'Q4': v_Q4,
            'Q5': v_Q5,
            'Q6': v_Q6,
            'Q7': v_Q7,
            'Q8': v_Q8,
            'Q9': v_Q9,
            'Q10': v_Q10,
            'Q11': v_Q11,
            'Q12': v_Q12,
            'Q13': v_Q13,
            'Q14': v_Q14,
            'Q15': v_Q15,
            'Q16': v_Q16,
            'Q17': v_Q17,
            'Q18': v_Q18,
            'Q19': v_Q19,
            'Q20': v_Q20,
            'Q21': v_Q21,
            'Q22': v_Q22,
            'Q23': v_Q23,
            'Q24': v_Q24,
            'Q25': v_Q25,
            'Q26': v_Q26,
            'Q27': v_Q27,
            'Q28': v_Q28,
            'Q29': v_Q29,
            'Q30': v_Q30,
            'Q31': v_Q31,
            'Q32': v_Q32,
            'Q33': v_Q33,
            'Q34': v_Q34,
            'Q35': v_Q35,
            'Q36': v_Q36,
            'Q37': v_Q37,
            'Q38': v_Q38,
            'Q39': v_Q39,
            'Q40': v_Q40,
            'Q41': v_Q41,
            'Q42': v_Q42
            }

    #create data frame
    data_df = pd.DataFrame(data, index=[0])
    return data_df

df = get_input()
st.write(df)

data_sample = pd.read_csv('ex_samples.csv')
data_sample = data_sample.drop(columns=['Status'])
df = pd.concat([df, data_sample],axis=0)

cat_data = pd.get_dummies(df[['HomeRegion','Sex']])
#Combine all transformed features together
X_new = pd.concat([cat_data, df], axis=1)

X_new = X_new.drop(columns=['HomeRegion','Sex'])# Select only the first row (the user input data)
#Drop un-used feature
X_new = X_new[:1]
# -- Reads the saved normalization model

load_nor = pickle.load(open('normalization.pkl', 'rb'))
# #Apply the normalization model to new data
X_new = load_nor.transform(X_new)
#st.write(X_new)

# # -- Reads the saved classification model
load_knn = pickle.load(open('best_knn.pkl', 'rb'))
# # Apply model for prediction
prediction = load_knn.predict(X_new)

st.write("""
## Prediction
""")
st.write(prediction)