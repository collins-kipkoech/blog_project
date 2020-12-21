
function myFunction() {

    var x = document.getElementById("sup-container").style;
    var y = document.getElementById("dir-login").style;
    var z = document.getElementById("container").style;
    var w = document.getElementById("dir-signup").style;  
     

if(x.display === "none" && y.display === "none" && z.display === "block" && w.display === "block"){
    y.display = "block";
    x.display = "block"; 
    z.display = "none";
    w.display = "none";
     
}
else{
    x.display = "none";
    y.display = "none";
    z.display = "block";
    w.display = "block"; 
}

}



