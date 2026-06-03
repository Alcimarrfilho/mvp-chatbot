# Chatbot de Atendimento Contextual - Seguro Saúde S/A (Modelo B)

Este repositório contém o protótipo do **Modelo B (Solução / Contextual)**, desenvolvido como um Produto Mínimo Viável (MVP) para um experimento acadêmico focado em Processamento de Linguagem Natural (PLN) e gestão de contexto em diálogos encadeados.

O objetivo principal desta aplicação é validar a eficácia da retenção de histórico de mensagens em comparação com abordagens tradicionais baseadas em regras e palavras-chave.

---

## Cenário do Experimento (Escopo do MVP)

O chatbot simula um atendente virtual para a seguradora fictícia **Seguro Saúde S/A**, especializado em fornecer informações sobre três modalidades de planos de saúde: **Bronze, Prata e Ouro**.

### Diferencial Técnico (Modelo B vs. Modelo A)
*   **Modelo A (Baseline / Tradicional):** Desenvolvido com estruturas condicionais estáticas (`if/else`) e Regex. Não possui armazenamento de histórico, dependendo de palavras-chave explícitas em cada turno.
*   **Modelo B (Este Repositório):** Desenvolvido utilizando a biblioteca **LangChain** para orquestração de LLM, equipado com um módulo de memória ativa que concatena o histórico de interações recentes ao prompt, permitindo resolver correferências e pronomes oblíquos (ex: *"dele"*, *"nele"*, *"disso"*).

---

## Resultados e Análise Crítica

O experimento foi desenhado de forma controlada através de um Dataset laboratorial de **50 interações**, divididas em sessões de 5 perguntas encadeadas. Os dados consolidados nos logs do sistema apontam:

*   **Acurácia do Modelo B:** **86%** (43 acertos de 50 interações).
*   **Tempo Médio de Resposta:** ~1.4 segundos (devido à latência de chamadas de API externas em nuvem).
*   **Ganho de Desempenho:** Superou o Modelo A (que obteve 44% de acurácia) em **42%**, ultrapassando a meta inicial estipulada de +30%.

### Limitações Identificadas (Alucinação Contextual)
Durante os testes, mapeou-se que o Modelo B apresenta falhas quando ocorre uma **mudança abrupta de assunto** por parte do usuário (ex: transicionar de dúvidas sobre o Plano Ouro para uma emergência veterinária com um cachorro). Por forçar a associação com o histórico contido na memória, a IA tende a gerar alucinações contextuais, misturando os tópicos.

---

## Tecnologias Utilizadas

*   **Python 3.11+**
*   **Streamlit:** Interface web responsiva para interação com o usuário.
*   **LangChain:** Framework para gerenciamento de prompts e histórico de conversas (`MessagesPlaceholder`).
*   **Groq API:** Infraestrutura de processamento de ultra-baixa latência.
*   **Llama 3.1 8B Instant:** Modelo de linguagem de código aberto utilizado como motor de inferência.

---

## Como ver o Projeto

### Acesso Rápido (Nuvem)
O projeto já está configurado e rodando online. Basta clicar no link abaixo para testar o chatbot imediatamente pelo computador ou celular:
👉 **[Clique aqui para abrir o Chatbot no Streamlit Cloud](https://chat-saude-alcimar.streamlit.app)**
