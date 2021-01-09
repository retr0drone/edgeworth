// fetches api data from the db
function getClaimsListView() {
    fetch('api/claims/')
    .then(res => res.json())
    .then(data => {
        renderClaims(data);
    })
    .catch(err => {
        console.error(err);
    })
}

function renderClaims(data) {
    return data.map(claim => {
        renderClaim(claim);
    })
}

function createNode(element) {
    return document.createElement(element);
}

// takes in parent and element we want to append to the parent
function append(parent, el) {
    return parent.appendChild(el);
}

// renders fetched datsa from Claims List (through getClaimsListView) to the DOM
function renderClaim(claim) {
    const root = document.getElementById('root');
    const div = createNode('div');
    const title = createNode('h2');
    const p = createNode('p');
    p.innerText = claim.title;
    title.innerText = claim.title;
    append(div, title);
    append(div, p);
    append(root, div);
}