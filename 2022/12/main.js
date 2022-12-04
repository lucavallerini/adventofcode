
let fs = require('fs');
let file = fs.readFileSync('sample', 'utf-8');

function init_graph() {
    const input = file.split(/(\n)/).filter(m => m.length > 2);
    const rows = input.length;
    const columns = input[0].length;

    let start = undefined;
    let end = undefined;

    const graph = [];
    for (let i = 0; i < rows; i++) {
        const row = [];
        graph.push(row);
        for (let j = 0; j < columns; j++) {
            const elevation = input[i][j].charCodeAt(0) - 97; // a - z -> [97, 122] -> [0, 25]
            let node = undefined;
            if (elevation == -14 /* S */ ) {
                node = {
                    original: input[i][j],
                    value: 0,
                    f: 0,
                    j: undefined,
                    edges: [],
                    pos: {i: i, j: j}
                };
                start = node;
            } else if (elevation == -28 /* E */ ) {
                node = {
                    original: input[i][j],
                    value: 25,
                    f: Number.MAX_SAFE_INTEGER,
                    j: undefined,
                    edges: [],
                    pos: {i: i, j: j}
                };
                end = node;
            } else {
                node = {
                    original: input[i][j],
                    value: elevation,
                    f: Number.MAX_SAFE_INTEGER,
                    j: undefined,
                    edges: [],
                    pos: {i: i, j: j}
                };
            }
            row.push(node);
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            const node = graph[i][j];

            if (i - 1 >= 0) {
                const to_node = graph[i-1][j];
                if (is_edge(node, to_node)) {
                    node.edges.push({i: i-1, j: j});
                }
            } 
            
            if (i + 1 < rows) {
                const to_node = graph[i+1][j];
                if (is_edge(node, to_node)) {
                    node.edges.push({i: i+1, j: j});
                }
            } 
            
            if (j - 1 >= 0) {
                const to_node = graph[i][j-1];
                if (is_edge(node, to_node)) {
                    node.edges.push({i: i, j: j-1});
                }
            } 
            
            if (j + 1 < columns) {
                const to_node = graph[i][j+1];
                if (is_edge(node, to_node)) {
                    node.edges.push({i: i, j: j+1});
                }
            }
        }
    }

    return {
        graph: graph,
        start: start,
        end: end,
    }
}

function is_edge(from, to) {
    return to.value - from.value <= 1;
}

function is_same_node(node1, node2) {
    return node1.pos.i == node2.pos.i && node1.pos.j == node2.pos.j;
}

function find_minimum_path(graph, start, end) {
    const S = [start];
    const Q = graph.flat();

    let current_node = start;
    while ( Q.length > 0 ) {
        const F = [];
        current_node.edges.forEach(e => {
            const node = graph[e.i][e.j];
            if (node.f != undefined && !S.find(n => is_same_node(n, node))) {
                F.push(node);
            }
        });
        if (F.length == 0) {
            break;
        }

        F.sort((n1, n2) => n1.f - n2.f);
        if (F.find(n => is_same_node(n, end))) {
            current_node = F.find(n => is_same_node(n, end));
        } else {
            current_node = F[0];
        }
        if (is_same_node(current_node, end)) {
            break;
        }
        Q.splice(Q.indexOf(Q.find(n => is_same_node(n, current_node))), 1);
        S.push(current_node);
        
        current_node.edges.forEach(e => {
            const node = graph[e.i][e.j];
            const alt = current_node.f + 1;
            const found = Q.find(n => is_same_node(n, node));
            if (found && alt < node.f) {
                node.f = alt;
                node.j = current_node;
            }
        });
    }
    return S;
}

const {graph, start, end} = init_graph();

const S = find_minimum_path(graph, start, end);
console.log("Minimum steps to reach E:", S.length);

let drawing = "";
for (let i = 0; i < graph.length; i++) {
    drawing += "\n";
    for (let j = 0; j < graph[0].length; j++) {
        if (S.find(n => is_same_node(n, graph[i][j]))) {
            const n = S.indexOf(S.find(n => is_same_node(n, graph[i][j])));
            drawing += n == 0 ? ' S ' : n < 10 ? "0" + n + " " : n + " ";
        } else {
            drawing += ' ' + graph[i][j].original + ' ';
        }
    }
}
console.log(drawing);
