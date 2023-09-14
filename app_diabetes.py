import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_diabete3.pkl', 'rb') 
maquina_preditiva_diabete3 = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER DIABETES</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA PREVER DIABETES - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    Sexo = st.selectbox('Sexo', ("Feminino", "Masculino"))
    Idade = st.number_input("Idade") 
    hipertensao = st.selectbox('hipertensao', ("Não", "Sim"))
    doenca_cardiaca = st.selectbox('doenca_cardiaca', ("Não", "Sim"))
    historico_tabagismo = st.selectbox('historico_tabagismo', ("Nunca", "Não sei", "Não Tenho atualmente", "Antigamente tinha", "Sempre tive", "Tenho atualmente"))
    bmi = st.number_input("bmi") 
    HbA1c_level = st.number_input("HbA1c_level")
    glicose = st.number_input("glicose")  
      
    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result, probabilidade = prediction(Sexo, Idade, hipertensao, doenca_cardiaca, historico_tabagismo, bmi, HbA1c_level, glicose) 
        st.success(f'Resultado: {result}')
        st.write(f'Probabilidade: {probabilidade}')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(Sexo, Idade, hipertensao, doenca_cardiaca, historico_tabagismo, bmi, HbA1c_level, glicose):   
    # Pre-processando a entrada do Usuário    
    if Sexo == "Feminino":
        Sexo = 0
    else:
        Sexo = 1
 
    if hipertensao == "Não":
        hipertensao = 0
    else:
        hipertensao = 1  
    
    if doenca_cardiaca == "Não":
        doenca_cardiaca = 0
    else:
        doenca_cardiaca = 1

    historico_tabagismo_dict = {
        "Nunca": 0,
        "Não sei": 1,
        "Não Tenho atualmente": 2,
        "Antigamente tinha": 3,
        "Sempre tive": 4,
        "Tenho atualmente": 5
    }
    historico_tabagismo = historico_tabagismo_dict[historico_tabagismo]

    # Fazendo a Predição
    parametro = np.array([[Sexo, Idade, hipertensao, doenca_cardiaca, historico_tabagismo, bmi, HbA1c_level, glicose]])
    fazendo_previsao = maquina_preditiva_diabete3.predict(parametro)
    probabilidade = maquina_preditiva_diabete3.predict_proba(parametro)

    if (fazendo_previsao == 0).any():
        pred = 'NÃO TEM DIABETE'
    else:
        pred = 'TEM DIABETE'

    return pred, probabilidade

if __name__ == '__main__':
    main()

