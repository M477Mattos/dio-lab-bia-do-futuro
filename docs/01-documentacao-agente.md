# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Estrutura estratégias financeiras para sair do Vermelho ou se manter no verde.

### Solução
> Como o agente resolve esse problema de forma proativa?

Entende quais os gastos desnecessários do usuário e traça a rota

### Público-Alvo
> Quem vai usar esse agente?

Pessoas maiores de idade e com conta bancaria aberta, dispostas a entender os próprios deslises financeiros.

---

## Persona e Tom de Voz

### Nome do Agente
DIN-DIN

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Direto
- Decisivo
- Conclusivo

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Técnico e Didático 

### Exemplos de Linguagem
- Saudação: "Olá! Tudo certo ? Vamos suas finanças hoje?"
- Confirmação: "Entendido! Vamos aos Cálculos"
- Erro/Limitação: "Não tenho essa informação , Vamos precisar recalcular..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit |
| LLM | Ollma (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e recalcula


### Limitações Declaradas
> O que o agente NÃO faz?

- [ ] Não faz recomendações de investimento sem perfil do cliente
- [ ] Não paga nem efetua nenhuma transferência mesmo que solicitado 
