# 🏆 Alura Album - Copa do Mundo Tech

[![Licença: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

O **Alura Album - Copa do Mundo Tech** é um álbum de figurinhas interativo e ultra-moderno desenvolvido como parte da **Imersão Dev/Tech da Alura**. O projeto homenageia os maiores nomes da tecnologia mundial e nacional, divididos em categorias como Inteligência Artificial, Python, Banco de Dados, Sistemas Operacionais e Celebridades Tech do Brasil.

Com uma interface responsiva, temática cyberpunk/neon e animações fluidas, este projeto simula a experiência física de folhear um álbum de figurinhas real diretamente no navegador, integrando-se dinamicamente com uma API para preenchimento dos slots.

---

## 🚀 Funcionalidades Principais

*   📖 **Efeito de Virada de Página Realista**: Implementado com a biblioteca `St.PageFlip`, proporcionando transições 3D suaves e física realista ao folhear as páginas.
*   🔊 **Som Dinâmico Sintetizado (Web Audio API)**: Em vez de carregar arquivos de áudio pesados, o som de papel sendo folheado é sintetizado em tempo real usando ruído branco manipulado com filtros dinâmicos e envelopes de volume.
*   🖱️ **Controles por Gestos e Teclado**: Suporte a arraste com o mouse/touchpad (drag-to-flip), botões de navegação lateral discretos e navegação por teclado usando as teclas `Seta Esquerda` (←) e `Seta Direita` (→).
*   🌐 **Integração com API Backend**: Busca automática de dados e imagens das figurinhas a partir de um servidor backend local (FastAPI).
*   ✨ **Design Premium e Interativo**:
    *   Efeito de *glitch text* na capa.
    *   Esfera tecnológica central 3D e cards flutuantes com animação de flutuação.
    *   Slots especiais maiores para destacar figurinhas chave.
    *   Código de barras realista na contracapa.
    *   Indicador visual de sucesso ("colado") com brilho suave e transição de escala ao carregar a imagem.

---

## 📂 Estrutura do Projeto Frontend

O frontend é composto por três arquivos principais:

*   **`index.html`**: Estrutura semântica do álbum, contendo a capa, páginas temáticas, slots para cada figurinha com informações do personagem, e a contracapa.
*   **`style.css`**: Estilização completa do projeto. Utiliza variáveis CSS para consistência de cores, gradientes radiais no plano de fundo, fontes modernas do Google Fonts (*Inter* e *Outfit*) e animações `@keyframes` personalizadas para micro-interações.
*   **`app.js`**: Lógica de controle do álbum. Inicializa o `PageFlip`, implementa os listeners para arraste customizado, sintetiza o som de virada de página e realiza a requisição `fetch` assíncrona ao backend FastAPI.

---

## 🛠️ Tecnologias Utilizadas

*   **HTML5** & **CSS3** (Variáveis, Flexbox, CSS Grid, Animações)
*   **Vanilla JavaScript** (ES6+)
*   **[PageFlip API](https://nodexpert.github.io/page-flip/docs/index.html)** - Biblioteca para animação de páginas.
*   **Web Audio API** - Para geração procedural e em tempo real do som de virada de folha.

---

## ⚙️ Como Executar o Projeto

### 1. Servindo o Frontend
Por questões de segurança do navegador (CORS e carregamento de scripts locais), é recomendado rodar o projeto por meio de um servidor local simples.

**Opção A: Extensão Live Server (VS Code)**
1. Instale a extensão **Live Server** no VS Code.
2. Abra a pasta do projeto.
3. Clique em **"Go Live"** na barra inferior do editor.

**Opção B: Servidor Python Embutido**
Caso possua o Python instalado, execute o comando abaixo no terminal da pasta do projeto:
```bash
python -m http.server 3000
```
Depois, acesse `http://localhost:3000` no seu navegador.

### 2. Conectando com o Backend (API de Figurinhas)
Este projeto está preparado para consumir figurinhas de uma API local.

Se você possui a API desenvolvida no **Dia 3 da Imersão**, inicie-a com o seguinte comando:
```bash
cd backend/dia-3
uvicorn main:app --reload
```
A API será iniciada em `http://localhost:8000`. O arquivo `app.js` fará a requisição automática para `http://localhost:8000/figurinhas` para baixar os dados e preencher os slots no álbum de forma dinâmica!

> [!NOTE]
> Se o backend não estiver rodando, o álbum ainda funcionará normalmente no modo de visualização dos slots (com os nomes e descrições dos desenvolvedores), registrando apenas um aviso amigável no console do desenvolvedor.

---

## 🗂️ Categorias & Figurinhas Disponíveis

O álbum conta com 30 figurinhas divididas em 6 páginas:

1.  **IA (#01 - #05)**: Alan Turing, John McCarthy, Sam Altman, Geoffrey Hinton, Yann LeCun.
2.  **Python (#06 - #10)**: Guido van Rossum, Tim Peters, Raymond Hettinger, Travis Oliphant, Wes McKinney.
3.  **Banco de Dados (#11 - #15)**: Edgar F. Codd, Larry Ellison, Michael Widenius, Salvatore Sanfilippo, Eliot Horowitz.
4.  **Sistemas Operacionais (#16 - #20)**: Linus Torvalds, Dennis Ritchie, Richard Stallman, Bill Gates, Steve Jobs.
5.  **Brasil Vol. 1 (#21 - #25)**: Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Andre David.
6.  **Brasil Vol. 2 (#26 - #30)**: Guilherme Lima, Gi Space Coding, Vinicius Neves, Rafaela Ballerini, **Você** (Espaço especial!).

---

Desenvolvido com 💙 durante a Imersão Alura.
