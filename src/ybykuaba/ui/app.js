// salva a div e o input:
const input = document.getElementById("busca");
const result_div = document.getElementById("resultados");

// recebe a query e a operação
let query = "";
let op = "";

// função que limpa a div de resultados
function clean_result() {
    result_div.innerHTML = "";
};

// detecta o tipo de operação
function get_operation() {
    if (query.startsWith("=")) return "calc";
    if (query.startsWith(":")) return "command";
    if (query.startsWith("?")) return "web";
    if (query.startsWith(".")) return "app";
    return "archive";
};

// fechamenbto da janela com esc
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' || event.key === 'Esc') {
        pywebview.api.close();
    }
});

// detecta o primeiro caractere:
input.addEventListener("input", (e) => {
    query = e.target.value;

    if (!query) {
        op = "";
        clean_result();
        return;
    }

    const new_op = get_operation();

    // limpa quando mudamos de operação
    if (new_op !== op) {
        op = new_op;
        clean_result();
    }

    switch (op) {
        case "calc":
            calculate();
            break;

        case "app":
            find_app();
            break;

        case "archive":
            find_archives();
            break;
    }
});

// detecta teclas no input
input.addEventListener("keydown", async (e) => {

    // executar ou abrir com enter
    if (e.key === "Enter") {
        // se for comando 
        if (op === "command") {
            const command = query.slice(1).trim();
            // mantem o modo a cada enter
            input.value = query = ":";
            // executa ne
            if (command) exec_command(command);
        // abrindo arquivo ou app
        } else if (op === "app" || op === "archive") {
            const selected = result_div.querySelector(".selected");

            if (selected) {
                const path = selected.dataset.open;
                // abre de acordo com a operação
                if (op === "app") {
                    await pywebview.api.open_app(path);
                } else {
                    await pywebview.api.open_path(path);
                }
                // Fecha o launcher depois de abrir o resultado
                pywebview.api.close();
            }
        } else if (op === "web") {
            // busca (o motor é resolvido no python)
            await pywebview.api.search_web(query.replace('?',''))
            pywebview.api.close();
        }
    }

    // setas navegam
    else if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        const items = [...result_div.querySelectorAll(".result-list li")];

        // só se existir resultado
        if (items.length) {
            e.preventDefault();
            // pega o resultado selecionado
            const selected = result_div.querySelector(".selected");
            const index = items.indexOf(selected);
            // define se sobe ou desce, se não sobe...só desce
            const step = e.key === "ArrowDown" ? 1 : -1;
            ''
            // remove a seleção anterior
            selected?.classList.remove("selected");
            // seleciona o próximo resultado, mantendo a navegação circular
            items[(index + step + items.length) % items.length].classList.add("selected");
        }
    }
});

async function find_archives() {
    let archives = await pywebview.api.find_archive(query);
    const ul = document.createElement('ul');
    ul.className = 'result-list';
    // preenche com os dados da API
    ul.innerHTML = archives.map((item, i) => `
    <li data-open='${item.path}' class="${i === 0 ? 'selected' : ''}">
        <span>${item.is_dir ? '\u{e5fe}' : '\u{f1517}'}</span>
        <div class="result-info">
            <strong>${item.name}</strong>
            <small>${item.path}</small>
        </div>
    </li>
`).join('');
    result_div.replaceChildren(ul);
}

async function find_app() {
    let applications = await pywebview.api.find_app(query.replace('.',''))
    const ul = document.createElement('ul');
    ul.className = 'result-list';
    // preenchendo com apps
    ul.innerHTML = applications.map((app, i) => `
        <li data-open='${app.bin}' class="${i === 0 ? 'selected' : ''}">
            <span>\u{f40e}</span>
            <div class="result-info">
                <strong>${app.name}</strong>
                <small>${app.bin}</small>
            </div>
        </li>
    `).join('');
    result_div.replaceChildren(ul);
}

async function calculate() {
    let q = query.replace('=', '')

    const resposta = await pywebview.api.calculate(q);

    const div = document.createElement('div');
    div.className = resposta.sucesso
        ? 'calc-result'
        : 'calc-result error';

    const strong = document.createElement('strong');

    // gambiarra pra não aparecer syntax error no primeiro caractere
    strong.textContent = (q ? resposta.resultado : "");

    div.appendChild(strong);

    result_div.replaceChildren(div);
}

async function exec_command(command) {
    const output = await pywebview.api.execute(command);
    const div = document.createElement('div');
    div.className = 'command-result';
    const pre = document.createElement('pre');
    const code = document.createElement('code');
    code.textContent = output;
    pre.replaceChildren(code);
    div.replaceChildren(pre);
    result_div.replaceChildren(div);
}
