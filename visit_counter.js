const visit_counter = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('https://c6jga50pg2.execute-api.eu-west-2.amazonaws.com/Prod')
        .then(res => res.json())
        .then(res => {
        visit_counter.innerHTML = res.website;
    });
}