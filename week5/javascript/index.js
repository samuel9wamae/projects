console.log("button clicked")
document.getElementById("confirm").onclick=function check()
{
    var  age=document.getElementById("age").value;
    if (age<18)
    {var x="you cant get in";
console.log("ok")}
    else
    {var x="you can get in";}
    document.getElementById("msg").innerHTML=x;}
    var a=0
    document.getElementById("inc").onclick=function inc()
    { a+=1
       
     document.getElementById("no").innerHTML=a
     console.log("help")
    }
    document.getElementById("dec").onclick=function dec()
    { a-=1
     document.getElementById("no").innerHTML=a
    }
    document.getElementById("res").onclick=function res()
    { 
    
     document.getElementById("no").innerHTML=0
    }