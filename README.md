<div align="center">

<img src="logo.png" alt="Galvão Bueno CEP - Haja CEP!" width="420">

# 🎙️ Galvão Bueno CEP

### *Haja CEP!* Busque endereços pelo CEP e veja tudo no mapa.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

**[🚀 Acessar a aplicação online](https://projeto-05-busca-cep.streamlit.app)**

</div>

---

## 📖 Sobre o Projeto

O **Galvão Bueno CEP** é uma aplicação web feita com **Streamlit** que permite:

- 🔎 **Buscar CEP:** informe um CEP e receba o endereço completo, com a localização marcada em um mapa interativo.
- 🧭 **Descobrir CEP:** digite um endereço e receba um link de busca no Google para encontrar o CEP correspondente.

O projeto nasceu como atividade prática de desenvolvimento Python: consumir uma API REST, tratar dados com Pandas e entregar uma interface simples, intuitiva e responsiva.

## 🎯 Objetivos

- Buscar informações de endereço em tempo real
- Exibir os resultados de forma organizada
- Mostrar a localização no mapa
- Oferecer uma interface profissional e amigável

## ✨ Funcionalidades

### 🔎 Buscar CEP
- Validação do CEP (exatamente 8 dígitos numéricos)
- Consulta em API externa
- Exibição de CEP, endereço, bairro, cidade e estado
- Tratamento de erros: CEP inválido, CEP não encontrado e falhas na consulta

### 🗺️ Mapa interativo
- Localização do endereço exibida com `st.map`
- Coordenadas (latitude e longitude) convertidas automaticamente em um `DataFrame`

### 🧭 Descobrir CEP
- Busca a partir de um endereço (ex.: `Rua Olga, Barueri, SP`)
- Geração de link de busca no Google
- Validação de campo vazio

### 📱 Interface
- Barra lateral com logo e menu de navegação
- Layout adaptável a diferentes telas
- Mensagens claras de sucesso e erro

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| **Python 3.8+** | Linguagem de programação |
| **Streamlit** | Framework da aplicação web |
| **Pandas** | Manipulação de dados e montagem do mapa |
| **Requests** | Requisições HTTP à API de CEP |
| **AwesomeAPI** | API de consulta de CEPs brasileiros |

## 📁 Estrutura do Projeto

```
Projeto_05_Busca_Cep/
│
├── .devcontainer/      # Configuração do ambiente de desenvolvimento
├── app.py              # Aplicação principal (interface Streamlit)
├── BuscarCep.py        # Módulo com as funções buscar_cep e descobrir_cep
├── logo.png            # Logo exibido na barra lateral e neste README
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Git
- Conexão com a internet

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/GalvaoLabs/Projeto_05_Busca_Cep.git
   cd Projeto_05_Busca_Cep
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:** <http://localhost:8501>

### 📦 requirements.txt

```txt
streamlit
pandas
requests
```

## 🚀 Como Usar

1. Abra a aplicação e escolha uma opção na **barra lateral**.
2. Em **Buscar CEP**, digite um CEP válido (somente números, ex.: `01001000`) e clique em **Buscar**.
3. Veja o endereço completo e a **localização no mapa**.
4. Em **Descobrir CEP**, digite o endereço (ex.: `Rua Olga, Barueri, SP`), clique em **Descobrir** e abra o link de busca gerado.

## 🧪 CEPs para Testar

| CEP | Local |
|---|---|
| `01001000` | Praça da Sé, São Paulo/SP |
| `22030060` | Copacabana, Rio de Janeiro/RJ |
| `40130150` | Comércio, Salvador/BA |
| `70002900` | Asa Norte, Brasília/DF |

## 🧠 Habilidades Praticadas

- ✅ Desenvolvimento com Streamlit
- ✅ Consumo de APIs REST
- ✅ Manipulação de dados com Pandas
- ✅ Tratamento de erros em Python
- ✅ Criação de interfaces web
- ✅ Versionamento com Git
- ✅ Documentação de projetos

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

> O logo (`logo.png`) não está coberto por essa licença.

## 🙌 Créditos

Projeto baseado em [msousa07/Projeto_05_Busca_Cep](https://github.com/msousa07/Projeto_05_Busca_Cep), adaptado e mantido por [GalvaoLabs](https://github.com/GalvaoLabs).

<div align="center">

**Bem, amigos... achou o CEP!** 🎉

</div>
