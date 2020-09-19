//function getCat() {
//    fetch("https://api.thecatapi.com/v1/images/search?api_key=a7ed07bb-660b-4184-8084-4163dfd5bc14")
//    .then(res => res.json())
//    .then(res=> {
//        const div = document.getElementById("cat-div");
//        div.innerHTML = '';
//        const cat = new Image();
//        cat.src = res[0].url;
//        div.appendChild(cat);
//    });
//}

function getAQI() {
    var zip = document.location.href.split('?')[1];
    fetch("https://api.weatherbit.io/v2.0/current/airquality?&postal_code="+zip+"&country=US&key=9b56e1214a514320bd53f194caeec05f")
    .then(res => res.json()).then(function(res) {
        $post("/results", {aqi:res});
    });
    //.then(res => res.json())
    //.then(res => {
        //const div = document.getElementById("AQI-div");
        //div.innerHTML = '';
    //    const lat = res["lat"];
    //    const lon = res["lon"];
    //    const aqi = res[data][0]["aqi"];
    //    let data = [lat, long, aqi]
        //div.appendChild(aqi);
    //    $.post("/results", {

        //})
    }



//window.onload = function() { 
//    const catButton = document.getElementById("cat-button");
//    catButton.onclick = getCat;
//}