# Passo a passo de Execução

## Instalação do Ollama 
```
1 Baixar o Ollama (ollama.com)
2 Instalar e abrir o terminal do windows
3 usar "ollama pull gpt-oss"
4 testar se funcionou com "ollama run gpt-oss"
```
## Código Completo

Todo o código-fonte esta no arquivo `app.py`.

## Como Rodar

```bash
# Instalar dependências
pip install pandas json requests streamlit 

# Garantir que Ollama está rodando
ollama serve

# Rodar a aplicação
streamlit run ./src/app.py
```
