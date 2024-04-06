// document.cookie

fetch(`http://127.0.0.1:5000/api/data`).then(r=>r.json()).then(d=>{
    document.getElementById("main").innerHTML=`Welcome Patient: ${d[0].name}`
})