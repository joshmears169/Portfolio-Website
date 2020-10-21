const visit_counter = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('https://dhtbtrg610.execute-api.eu-west-2.amazonaws.com/Prod', {
        mode: 'cors'
    })
        .then(res => res.json())
        .then(res => {
        visit_counter.innerHTML = Math.trunc(res.body.visitors);
    });
}