# ARTEC - Sistema de Gerenciamento de Festival de Artes no Campus

O **ARTEC** é um sistema de gerenciamento de festival de artes desenvolvido em Python para a disciplina de **Programação Orientada a Objetos (POO)**.

O projeto simula uma amostra competitiva de artes realizada no campus, permitindo o cadastro de participantes, inscrição de trabalhos artísticos, avaliação por jurados e gerenciamento dos trabalhos por um organizador.

---

## Objetivo do Projeto

O objetivo do sistema é aplicar, de forma prática, os principais conceitos de **Programação Orientada a Objetos**, utilizando um contexto acadêmico voltado para a organização de um festival de artes.

O sistema permite controlar o fluxo básico de uma competição artística, desde a inscrição dos trabalhos até sua avaliação e alteração de status.

---

## Funcionalidades

### Participante

O participante pode:

- Acessar o sistema por matrícula;
- Cadastrar-se informando nome e matrícula;
- Inscrever trabalhos artísticos;
- Escolher a categoria do trabalho;
- Listar seus próprios trabalhos inscritos;
- Acompanhar o status de seus trabalhos.

### Jurado

O jurado pode:

- Acessar o sistema por matrícula;
- Cadastrar-se informando nome e matrícula;
- Visualizar trabalhos disponíveis para avaliação;
- Avaliar trabalhos com nota de 0 a 10;
- Adicionar comentários à avaliação;
- Avaliar trabalhos de forma anônima, sem visualizar o nome do participante;
- Avaliar apenas trabalhos com status `Inscrito`;
- Registrar uma única avaliação por trabalho.

### Organizador

O organizador pode:

- Visualizar todos os trabalhos cadastrados no sistema;
- Consultar informações gerais dos trabalhos;
- Alterar o status de um trabalho;
- Definir status como, por exemplo, `Desclassificado`, `Premiado` ou outro status necessário.

---

## Categorias de Trabalhos

O sistema permite a inscrição de trabalhos nas seguintes categorias:

- Pintura;
- Fotografia;
- Música.

Cada participante pode inscrever até **2 trabalhos por categoria**.

---

## Regras de Negócio

O sistema implementa algumas regras importantes:

- A matrícula/identificação do usuário não pode ser vazia;
- O nome do usuário não pode ser vazio;
- O título do trabalho não pode ser vazio;
- Apenas categorias válidas podem ser utilizadas;
- Cada participante possui limite de inscrições por categoria;
- A nota da avaliação deve estar entre 0 e 10;
- Cada trabalho recebe apenas uma avaliação;
- Após ser avaliado, o trabalho tem seu status alterado de `Inscrito` para `Avaliado`;
- Trabalhos avaliados deixam de aparecer na lista de trabalhos disponíveis para avaliação;
- Um jurado não pode avaliar novamente um trabalho já registrado;
- A avaliação dos trabalhos pelo jurado ocorre de forma anônima, ocultando o nome do participante.

---

## Conceitos de POO Aplicados

Este projeto foi desenvolvido com foco nos principais conceitos de Programação Orientada a Objetos.

### Classes e Objetos

O sistema possui classes para representar pessoas, participantes, jurados e trabalhos artísticos.

Principais classes:

- `PessoaARTEC`;
- `Participante`;
- `Jurado`;
- `Trabalho`;
- `TrabalhoPintura`;
- `TrabalhoFotografia`;
- `TrabalhoMusica`;
- `Avaliavel`.

### Herança

A classe `PessoaARTEC` funciona como classe base para os tipos de usuários do sistema.

As classes `Participante` e `Jurado` herdam seus atributos e comportamentos básicos.

```python
class Participante(PessoaARTEC):
    pass

class Jurado(PessoaARTEC):
    pass
```

Da mesma forma, a classe `Trabalho` é utilizada como classe base para os tipos específicos de trabalhos artísticos.

```python
class TrabalhoPintura(Trabalho):
    pass

class TrabalhoFotografia(Trabalho):
    pass

class TrabalhoMusica(Trabalho):
    pass
```

### Abstração

A classe `Trabalho` representa um modelo abstrato de trabalho artístico.

Ela define métodos que devem ser implementados pelas subclasses, como:

- `avaliar`;
- `calcular_nivel_avaliacao`.

### Polimorfismo

Cada tipo de trabalho implementa o método `avaliar` de acordo com sua própria categoria.

Apesar de todos os trabalhos possuírem o mesmo método, cada subclasse pode ter sua própria forma de execução.

### Encapsulamento

Os dados dos objetos são organizados dentro das classes, evitando manipulação direta fora da estrutura do sistema.

Cada classe possui responsabilidades bem definidas.

### Interface

O sistema utiliza a interface `Avaliavel`, criada com `ABC`, para definir o contrato de objetos que podem ser avaliados.

```python
class Avaliavel(ABC):
    @abstractmethod
    def avaliar(self, nota: float, comentario: str) -> None:
        pass
```

### Factory Method

No cadastro de trabalhos, o sistema utiliza uma lógica baseada no padrão Factory.

A partir da categoria informada pelo participante, o sistema cria automaticamente o tipo correto de trabalho.

```python
categorias = {
    "pintura": TrabalhoPintura,
    "fotografia": TrabalhoFotografia,
    "musica": TrabalhoMusica
}
```

---

## Estrutura do Projeto

```text
ARTEC-sistema-de-gerenciamento-de-festival-de-artes/
│
├── interfaces.py
├── trabalhos.py
├── usuarios.py
├── main.py
└── README.md
```

### Descrição dos Arquivos

| Arquivo | Descrição |
|---|---|
| `interfaces.py` | Contém a interface `Avaliavel`, responsável por definir o contrato de avaliação. |
| `trabalhos.py` | Contém a classe abstrata `Trabalho` e suas subclasses: pintura, fotografia e música. |
| `usuarios.py` | Contém as classes relacionadas aos usuários do sistema: `PessoaARTEC`, `Participante` e `Jurado`. |
| `main.py` | Arquivo principal do sistema, contendo o menu interativo via terminal. |
| `README.md` | Documentação do projeto. |

---

## Como Executar o Projeto

### Pré-requisitos

Para executar o sistema, é necessário ter o **Python 3** instalado na máquina.

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/seu-usuario/ARTEC-sistema-de-gerenciamento-de-festival-de-artes.git
```

### Passo 2: Acessar a pasta do projeto

```bash
cd ARTEC-sistema-de-gerenciamento-de-festival-de-artes
```

### Passo 3: Executar o arquivo principal

No Windows, utilize:

```bash
python main.py
```

Ou, dependendo da configuração do ambiente:

```bash
python3 main.py
```

---

## Menu Principal do Sistema

Ao executar o projeto, o sistema exibe o seguinte menu:

```text
=======================================================
=== SISTEMA ARTEC - AMOSTRA COMPETITIVA DE ARTES ===
=======================================================
1. Acessar como Participante
2. Acessar como Jurado
3. Acessar como Organizador (Admin)
0. Sair do Sistema
=======================================================
```

---

## Fluxo de Uso

### 1. Participante

O participante acessa o sistema com uma matrícula. Caso ainda não exista cadastro, o sistema solicita o nome e cria o usuário automaticamente.

Depois disso, ele pode inscrever trabalhos nas categorias disponíveis.

### 2. Jurado

O jurado também acessa o sistema com matrícula. Caso ainda não esteja cadastrado, o sistema solicita seu nome.

Após acessar, ele pode listar trabalhos pendentes e realizar avaliações.

### 3. Organizador

O organizador possui acesso direto no simulador e pode visualizar todos os trabalhos inscritos, além de alterar seus status.

---

## Exemplo de Funcionamento

Exemplo de inscrição de trabalho:

```text
Categorias válidas: pintura, fotografia, musica
Digite a categoria do trabalho: pintura
Digite o título da obra: Cores do Campus
>>> SUCESSO! Trabalho 'Cores do Campus' inscrito na categoria 'pintura'.
```

Exemplo de avaliação:

```text
Digite a nota atribuída (0 a 10): 9.5
Deixe um comentário sobre a obra: Excelente composição artística.
Trabalho de pintura 'Cores do Campus' avaliado.
>>> AVALIAÇÃO REGISTRADA COM SUCESSO!
```

---

## Tecnologias Utilizadas

- Python 3;
- Programação Orientada a Objetos;
- Terminal/Console;
- Estruturas de dados em memória.

---

## Persistência de Dados

Atualmente, o sistema utiliza persistência apenas em memória.

Isso significa que os dados cadastrados durante a execução são perdidos quando o programa é encerrado.

Essa escolha foi feita para simplificar o projeto e focar nos conceitos de Programação Orientada a Objetos.

---

## Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente:

- Cadastro fixo de organizador;
- Login com senha;
- Salvamento dos dados em arquivo;
- Integração com banco de dados;
- Interface gráfica;
- Relatórios de avaliação;
- Ranking dos trabalhos mais bem avaliados;
- Separação de permissões por tipo de usuário;
- Exportação dos resultados do festival.

---

## Finalidade Acadêmica

Este projeto foi desenvolvido exclusivamente para fins acadêmicos, como atividade prática da disciplina de **Programação Orientada a Objetos**.

O sistema demonstra a aplicação de conceitos como:

- Classes;
- Objetos;
- Herança;
- Abstração;
- Polimorfismo;
- Encapsulamento;
- Interfaces;
- Validações;
- Tratamento de exceções;
- Organização modular do código.

---

## Autoria

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)**.

**Sistema:** ARTEC - Sistema de Gerenciamento de Festival de Artes no Campus  
**Linguagem:** Python  
**Disciplina:** Programação Orientada a Objetos  
**Finalidade:** Projeto acadêmico
````