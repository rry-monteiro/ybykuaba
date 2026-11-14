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

Basta instalar e associar o comando `yby` a um atalho do seu sistema, é recomendado o uso de `Super + espaço`, o propjeto inteiro só tem o comando `yby`, se quiser garantir que está funcionando antes de adiiconar um atalho, teste no terminal.

| Prefixo | Função | Exemplo | Observações |
| :-----: | ------ | ------- | ----------- |
| *(nenhum)* | Busca arquivos e pastas | `relatorio` | Procura em `Documentos`, `Desktop`, `Downloads`, `Projetos`, `Músicas` e `Imagens`, independente do idioma do sistema |
| `.` | Busca aplicativos | `.firefox` | O app precisa ter um arquivo `.desktop` para ser encontrado |
| `:` | Executa comandos no terminal | `:ls -la` | Não funciona com `sudo` nem com comandos que abrem outros apps |
| `=` | Calculadora | `=2**10` | Suporta `+`, `-`, `*`, `/`, `**` (potência) e `%` (resto). Também simplifica expressões: `=a**b+a**b` retorna `2*a**b` |
| `?` | Busca na web | `?rust lifetimes` | Abre o navegador com a pesquisa no DuckDuckGo |

## Sobre
Como cada coisa funciona.
### Busca de aplicativos, arquivos e pastas
Existe um arquivo `.db` que é gerado em `~/.local/share/ybykuaba/`, ele contem as tabelas `files` e `applications`, guardando informações de apps, documentos e pastas, a pesquisa é feita com sqlite e o banco é sincronizado a cada abertura.

### Execução de comandos
Os comandos que você executa são chamados por `subprocess.Popen()` e encapsulados com `/bin/sh -c <seu_comando>`, com um timeout de execução, por isso não é recomendado o uso pra abertura de programas e processos demorados, serve mais pra informações, matar processos, criar e deletar pastas, etc.

### Cálculos
É usada a biblioteca [`sympy`](https://www.sympy.org/pt/index.html) para o calculo e o `ast` do python pra identificar cada operação, é feito um parse na string passada à janela e uma função circular processa essa expressão até retornar um objeto `sympy.Expr`, que é transformado em string e devolvido a janela.

### Busca na web
Simplismente a biblioteca `webbbrowser` abrindo seu navegador com `webbbrowser.open` e a `urllib` ajustando sua string pra uma url.


## Próximos passos
[ ] - Arquivo de configuração em `.toml` permitindo editar onde é feita a busca de arquivos
[ ] - Inserir praticamente todo o cálculo I, II e III no parse, permitindo contas mais complexas
[ ] - Uma execução de comandos mais aberta, permitindo sudo com abertura de um terminal pra validação do comando
[ ] - Mostrar o resultado do cálculo com Latex.

## ybykûaba, do Tupi antigo.
A palavra *"ybybkûaba"* veio de *yby* (terra) + *kûaba* (conhecimento), e significa literalmente "produtividade" se traduzido do Tupi. 

A ideia de construir uma janela que me permitisse fazer praticamente tudo que eu preciso em um computador surgiu no mesmo dia que conheci essa palavra, assim eu o construí. 