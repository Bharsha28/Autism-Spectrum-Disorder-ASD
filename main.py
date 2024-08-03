import pickle
import streamlit as st
import numpy as np
st.set_page_config(page_title="Autism Spectrum Disorder", layout='wide')


st.title("Autism Spectrum Disorder")
#st.subheader("Autism Spectrum Disorder (ASD) is a developmental condition affecting communication, social skills, and behavior. Individuals with ASD may struggle with social interactions and exhibit repetitive behaviors. Sensory sensitivities and focused interests are also common. Each person with ASD is unique, and early intervention can help improve outcomes. Understanding and support can enhance inclusivity and well-being for those with ASD.")

model=pickle.load(open('asd_final.pkl','rb'))
value=["YES","NO"]
A1= st.radio(
    "How often does the individual have difficulty starting or maintaining conversations with others?",
    ["NO","YES"]

)
A2= st.radio(
    "Does the individual show a strong preference for routines and become distressed when these routines are disrupted?",
    ["NO","YES"]

)
A3= st.radio(
    "In what areas does the individual show exceptional abilities or talents that stand out compared to their peers?",
    ["NO","YES"]

)
A4= st.radio(
    "Does the individual often react strongly to certain sensory inputs, such as loud noises, bright lights, or specific textures?",
    ["NO","YES"]

)
A5= st.radio(
    "How frequently does the individual engage in aggressive behaviors, such as hitting, kicking, or yelling?",
    ["NO","YES"]

)
A6=st.radio(
    "Does the individual often have trouble sitting still or staying focused on tasks due to excessive movement or restlessness?",
    ["NO","YES"]

)
A7=st.radio(
    "How often does the individual have difficulty paying attention to tasks or activities and get easily distracted?",
    ["NO","YES"]

)
A8=st.radio(
    "How often does the individual feel anxious or worried about everyday things? For example, do they frequently feel nervous about going to school or meeting new people?",
    ["NO","YES"]

)
A9=st.radio(
    "Does the individual frequently show signs of depression, such as persistent sadness, loss of interest in activities, or changes in sleep patterns?",
    ["NO","YES"]

)
A10=st.radio(
    "How often does the individual become easily irritated or frustrated, especially when faced with minor inconveniences or changes?",
    ["NO","YES"]

)
#age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

age = st.slider("*How old are you?*streamlit", 0, 130, 25)
st.write("I'm ", age, "years old")
g=["MALE","FEMALE"]
gender = st.selectbox(
    "What is the individual's gender?",
    g
)
Jundice=st.radio(
    "Has the individual ever experienced jaundice (yellowing of the skin or eyes) during infancy or childhood?",
    ["NO", "YES"]
)
Austim=st.radio(
    "Does an immediate family member of the patient have a diagnosis of Autism Spectrum Disorder (ASD)?",
    ["NO","YES"]
)
Used_app_before=st.radio(
    "Has the patient previously undergone a screening test for Autism Spectrum Disorder (ASD) using any app or tool?",
    ["NO","YES"]
)
input_values=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,age, gender,Jundice, Austim, Used_app_before]
mapping_dict = {"YES": 1, "NO": 0, "MALE": 0, "FEMALE": 1}

def map_values(data, mapping_dict):
    return [mapping_dict.get(item, item) for item in input_values]
input_values= map_values(input_values, mapping_dict)

input_values=np.array(input_values,dtype=float)
input_values=input_values.reshape(1,-1)
my_predict=model.predict(input_values)
my_predict=int(my_predict)
if my_predict==1:
    words="The evaluation suggests a [:red]strong probability of Autism Spectrum Disorder based on the provided response"
else:
    words1="The evaluation suggests a [:green]Low probability of Autism Spectrum Disorder based on the provided response"
def predict():
    pass

if st.button("PREDICT"):
    if my_predict == 1:
        st.markdown(":red[The evaluation suggests a :red[strong] probability of Autism Spectrum Disorder based on the provided response]")

    else:
        st.write(':green[The evaluation suggests a :green[LOW]  probability of Autism Spectrum Disorder based on the provided response]')
