var width = window.innerWidth;
var height = window.innerHeight;

window.onresize = () => {
	width = window.innerWidth;
	height = window.innerHeight;
	let svg = document.querySelector('svg');
	svg.setAttribute("width", width);
	svg.setAttribute("height", height);
}

// Declaração dos nós da árvore conexa
var nodes = [
	{ id: "A" }, { id: "B" }, { id: "C" }, { id: "D" },
	{ id: "E" }
];

// Declaração das arestas valoradas
var links = [
	{ source: "A", value: 2, target: "B" },
	{ source: "A", value: 4, target: "C" },
	{ source: "B", value: 1, target: "C" },
	{ source: "C", value: 5, target: "D" },
	{ source: "D", value: 3, target: "E" }
];

// D3 usa a referência desses dois objetos para salvar informações essenciais dos nós como posição e etc.

function renderizar(nodes, links) {
	document.querySelector("#grafo-exibicao").innerHTML = '';
	const grafoContainer = document.getElementById("grafo-exibicao");

	const svg = d3.select("#grafo-exibicao").append("svg")
		.attr("width", width)
		.attr("height", height)
		.call(d3.zoom().on("zoom", (event) => {
			container.attr("transform", event.transform);
			const zoomLevel = event.transform.k;
			grafoContainer.style.backgroundSize = `${35 * zoomLevel}px ${35 * zoomLevel}px`;
		}));

	const container = svg.append("g");

	// Simulação com força
	const simulation = d3.forceSimulation(nodes)
	.force("link", d3.forceLink(links)
		.id(d => d.id)
		.distance(180)) // ou qualquer fórmula baseada nos dados

	.force("charge", d3.forceManyBody().strength(-900)) // ← aqui controla a repulsão
	.force("center", d3.forceCenter(width / 2, height / 2))
	.force("collision", d3.forceCollide().radius(35)); // ← evita sobreposição direta



	// Arestas (sem direção)
	const link = container.selectAll(".link")
		.data(links)
		.enter().append("line")
		.attr("class", "link")
		.style("stroke", "#9dbaea")
		.style("stroke-width", 2);

	const node = container.selectAll(".node")
		.data(nodes)
		.enter().append("g")
		.attr("class", "node");

	node.append("circle").attr("r", 30);

	node.append("text").text(d => d.id).attr("dy", 5);

	// Adiciona o valor (peso) das arestas no ponto médio
	const linkLabel = container.selectAll(".link-label")
		.data(links)
		.enter().append("text")
		.attr("class", "link-label")
		.attr("fill", "#333")
		.attr("font-size", "20px")
		.attr("text-anchor", "middle")
		.text(d => d.value);

	simulation.on("tick", () => {
		link
			.attr("x1", d => d.source.x)
			.attr("y1", d => d.source.y)
			.attr("x2", d => d.target.x)
			.attr("y2", d => d.target.y);

		linkLabel
		.attr("x", d => (d.source.x + d.target.x) / 2)
		.attr("y", d => (d.source.y + d.target.y) / 2);


		node.attr("transform", d => `translate(${d.x},${d.y})`);
	});

	const drag = d3.drag()
		.on("start", (event, d) => {
			if (!event.active) simulation.alphaTarget(0.3).restart();
			d.fx = d.x;
			d.fy = d.y;
		})
		.on("drag", (event, d) => {
			d.fx = event.x;
			d.fy = event.y;
		})
		.on("end", (event, d) => {
			if (!event.active) simulation.alphaTarget(0);
			d.fx = null;
			d.fy = null;
		});

	node.call(drag);
}


// isso faz questão de manter salvo o exemplo selecionado para que o usuário
// veja o mesmo exemplo toda vez que recarregue a página.
async function trocarExemplo(evento) {

	const url = new URL(window.location.href);

	//
	let exemploSelecionado = document.querySelector('select#preset').value;
	let parametroExemploSalvo = url.searchParams.get('exemplo');

	let casoParametroExemploPresente = parametroExemploSalvo !== null;
	let casoUsuarioRecarregouPagina = evento === undefined;
	// evento será um objeto defindo caso essa função tenha sido chamada pelo onchange do elemento select.
	// nesse caso, o usuário selecionou um novo exemplo e queremos mudar para o novo exemplo.
	// evento é undefined quando essa função é chamada uma única vez no primeiro load da página.
	// nesse caso, queromos selecionar o exemplo salvo na url.
	if (casoUsuarioRecarregouPagina && casoParametroExemploPresente) {
		exemploSelecionado = parametroExemploSalvo;
		// alterar select para que também reflita a escolha.
		document.querySelector('select#preset').value = parametroExemploSalvo;
	}

	let resposta = await fetch(`/node/${exemploSelecionado}`, { method: 'GET' });
	if (!resposta.ok) {
		throw resposta.ok;
	}
	let { nodes: nodes_, links: links_ } = await resposta.json();
	console.log(links_);
	nodes = nodes_;
	links = links_;

	// atualiza a url para que toda vez que o usuário recarregar a página, o mesmo exemplo será exibido.
	const parametrosNovos = new URLSearchParams({ exemplo: exemploSelecionado }).toString();

	window.history.replaceState(null, "", `${url.pathname}?${parametrosNovos}`)

	await atualizar();

}

let tipoGrafoCompleto = document.querySelector('#tipo-grafo-completo');
let tipoLacos = document.querySelector('#tipo-lacos');
let tipoSimples = document.querySelector('#tipo-simples');

let arvoreNodeRaiz = document.querySelector('#arvore-raiz')
let tipoArvore = document.querySelector('#tipo-arvore');
let tipoBinaria = document.querySelector('#tipo-binaria');
let tipoCompleta = document.querySelector('#tipo-completa');
let checkboxSubgrafo = document.querySelector('#considerar-subgrafo');
let tipoCheia = document.querySelector('#tipo-cheia');

let exemplo = document.querySelector('select#preset');

async function atualizar() {
	renderizar(nodes, links);
}

function creditos() {
	let creditos = document.querySelector('#creditos');
	let butao = document.querySelector('#creditos-toggle');
	creditos.classList.toggle('hidden')
	if (creditos.classList.contains('hidden')) {
		butao.textContent = 'Exibir';
	} else {
		butao.textContent = 'Esconder';
	}
}


trocarExemplo();