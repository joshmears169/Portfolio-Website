const visit_counter = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('https://3pnd9hoy3j.execute-api.eu-west-2.amazonaws.com/Prod/VisitorCounter'
        )
        .then(res => res.json())
        .then(res => {
        visit_counter.innerHTML = res.visitors;
    });
}