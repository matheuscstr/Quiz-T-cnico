import streamlit as st

st.title("Quiz Técnico")
st.write("Este Quiz contém questões de programação, manutenção e suporte de computadores e redes de computadores")
perguntas = [ 

    {"pergunta": "Qual foi a primeira liguagem de programação criada?",
        "opcoes": ["Java", "Python", "FORTRAN", "PHP"],

        "resposta_correta": "FORTRAN"},

    {"pergunta": "Qual a linguagem de programação mais usada?",
        "opcoes": ["PHP", "Python", "Inglês", "JavaScript"],

        "resposta_correta": "JavaStript"},
        
    {"pergunta": "Qual dessas linguagens de programação é mais popular no desenvolvimento de jogos?",
    "opcoes": ["C-Sharp", "C", "C++", "JavaScript"],

        "resposta_correta": "C-Sharp"},

    {"pergunta": "A linguagem de programção JavaScript é mais indicada para?",
        "opcoes": ["Desenvolvimento back_end", "Desenvolvimento front_end", "Suporte computacional", "Inicialização de boot"],

        "resposta_correta": "Desenvolvimento front_end"},

    {"pergunta": "Qual dessas alternativas é uma função da placa de vídeo?",
        "opcoes": ["Resfriar", "Renderizar", "Alimentar", "Armazenar"],

        "resposta_correta": "Renderizar"},

    {"pergunta": "Qual a função de um disco rígido?",
        "opcoes": ["Armazenar", "Otimizar", "Resfriar", "Alimentar"],

        "resposta_correta": "Armazenar"},

    {"pergunta": "Onde o cabo SATA se conecta?",
        "opcoes": ["Placa de vídeo", "Fonte de alimentação", "Disco rígido", "Cooler"],

        "resposta_correta": "Disco rígido"},

    {"pergunta": "TCP e UDP fazem parte de qual camada?",
        "opcoes": ["Camada de Aplicação", "Camada de Apresentação", "Camada de Transporte", "Camada de Rede"],

        "resposta_correta": "Camada de Transporte"},

    {"pergunta": "O DNS faz parte de qual camada?",
        "opcoes": ["Camada de Apresentação", "Camada de Aplicação", "Camada de Enlace", "Camada de Transporte"],

        "resposta_correta": "Camada de Aplicação"},

    {"pergunta": "Qual dessas funções o DHCP NÃO faz?",
        "opcoes": ["Dar endereço IP", "Rastrear informações", "Dar mascára de sub-rede", "Atribuir Gateway padrão"],

        "resposta_correta": "Rastrear informações"},

            ]

pontuacao = 1

for i in range(len(perguntas)):
    pergunta = perguntas[i]
    st.header(f"Pergunta {i + 1}: {pergunta['pergunta']}")
    resposta_usuario = st.radio("Escolha a opção correta:", pergunta["opcoes"])

    if st.button(f"Ver Resposta {i + 1}"):
        st.write(f"Resposta Correta: {pergunta['resposta_correta']}")

    if resposta_usuario == pergunta["resposta_correta"]:
        pontuacao += 1

st.header("Resultado Final")
st.write(f"Sua pontuação total: {pontuacao} de {len(perguntas)}")

if pontuacao == len(perguntas):
    st.success("Parabéns! Você acertou todas as perguntas.")
elif pontuacao >= len(perguntas) / 2:
    st.info("Bom trabalho! Você acertou pelo menos metade das perguntas.")
else:
    st.warning("Você pode revisar seus conhecimentos. Tente novamente!")