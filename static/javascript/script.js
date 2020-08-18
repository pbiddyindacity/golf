function updateScorecard() {
    fetch('/scorecard', {
    method:"POST",
    body: JSON.stringify({
        'course': document.getElementById('course').value
        }),
    headers: {
    'Content-Type': 'application/json'
}
    })
    .then(function (response) {
        document.getElementById('courseform').submit();
    }).then(function (text) {
        console.log('POST response: ');
        console.log(text)



    });

}