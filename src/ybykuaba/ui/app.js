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
    // se não temos query, operador = "" e resultado limpo
    if (!query) { op = ""; clean_result(); return; }
    if (query.length === 1) {
        op = get_operation();
    } else {
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

            case "command":
            case "web":
                clean_result();
                break;
        };
    };
});

// detecta teclas no input
input.addEventListener("keydown", (e) => {
    switch (op) {
        case "command":
            //execute_command
            break;

        case "web":
            // serach_web
            break;
    };
});

async function find_archives() {
    let archives = await pywebview.api.find_archive(query);
    const ul = document.createElement('ul');
    ul.className = 'result-list';
    // preenche com os dados da API
    ul.innerHTML = archives.map(item => `
        <li>
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
    ul.innerHTML = applications.map(app => `
        <li>
            <span>\u{f40e}</span>
            <div class="result-info">
                <strong>${app.name}</strong>
                <small>${app.exec}</small>
            </div>
        </li>
    `).join('');
    result_div.replaceChildren(ul);
}

async function calculate() {
    let resultado = await pywebview.api.calculate(query.replace('=',''))
    result_div.innerHTML = `
    <div class="calc-result">
        <strong>${resultado}</strong>
    </div>
    `
}

function exec_command() { }
function search_web() { }
