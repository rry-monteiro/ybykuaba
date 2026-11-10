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
                // calcular
                break;

            case "app":
                // buscar app
                break;

            case "archive":
                // find_archive
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

