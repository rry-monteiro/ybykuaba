# ybykûaba

Um menu para busca de apps, arquivos, execução de comandos e cálculos e pesquisas na web.

## O que ele faz

- **Apps**: busca e abre aplicativos instalados
- **Arquivos**: pesquisa arquivos no sistema
- **Cálculos**: resolve operações matemáticas direto na barra de busca
- **Comandos**: executa comandos do terminal
- **Busca na web**: busca no seu navegador

## Stack

- Python
- [pywebview](https://pywebview.flowrl.com/) para a janela desktop
- Interface em HTML/CSS/JS (`ui/index.html`)
- [uv](https://docs.astral.sh/uv/) para gerenciar o projeto e as dependências

## Requisitos

- Linux
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

O Python e as dependências são gerenciados pelo uv, então não precisa instalar nada globalmente.

## Instalação

```bash
git clone https://github.com/rry-monteiro/ybykuaba.git
cd ybykuaba
uv sync
uv tool install .
```

## Uso

```bash
yby
```
- Associe esse comando a um atalho para abrir o ybykuaba de qualquer canto

