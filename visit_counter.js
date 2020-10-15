const countEl = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('httpdkclmsd')
        .then(res => res.json())
        .then(res => {
        countEl.innerHTML = res.visits;
    });
}