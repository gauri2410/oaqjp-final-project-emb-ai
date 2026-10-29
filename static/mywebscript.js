let RunSentimentAnalysis = ()=>{
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            const response = xhttp.responseText ? JSON.parse(xhttp.responseText) : {};
            document.getElementById("system_response").innerHTML =
                this.status == 200 ? JSON.stringify(response) : response.error;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
