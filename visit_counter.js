const countEl = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('https://db0u1sqe9d.execute-api.us-east-2.amazonaws.com/prod/cou')
        .then(res => res.json())
        .then(res => {
        countEl.innerHTML = res.visits;
    });
}