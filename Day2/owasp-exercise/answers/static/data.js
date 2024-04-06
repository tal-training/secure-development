if (!localStorage.getItem("id")){
    fetch("http://127.0.0.1:5000/token").then(r=>r.headers).then(h=>{
        localStorage.setItem("id", JSON.parse(atob(h.get("Token"))).id)
    })    
}

fetch(`http://127.0.0.1:5000/api/data/${localStorage.getItem('id')}`).then(r=>r.json()).then(d=>{
    document.getElementById("main").innerHTML=`Welcome Patient: ${d[0].name}`
})