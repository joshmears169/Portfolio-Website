const visit_counter = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('https://3pnd9hoy3j.execute-api.eu-west-2.amazonaws.com/Prod/VisitorCounter', {
    mode: 'cors',
    headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET"
        }
    }
        )
        .then(res => res.json())
        .then(res => {
        visit_counter.innerHTML = res.visitors;
    });
}