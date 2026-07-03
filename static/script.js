const input=document.getElementById("user-input");

const btn=document.getElementById("send-btn");

const chat=document.getElementById("chat-box");

function addMessage(text,type){

const div=document.createElement("div");

div.className=`message ${type}`;

div.innerHTML=text.replace(/\n/g,"<br>");

chat.appendChild(div);

chat.scrollTop=chat.scrollHeight;

}

async function sendMessage(){

const text=input.value.trim();

if(text==="") return;

addMessage(text,"user");

input.value="";

addMessage("Thinking...","bot");

const loading=chat.lastChild;

try{

const response=await fetch("/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

messages:[

{

role:"user",

content:text

}

]

})

});

const data=await response.json();

loading.remove();

let reply=data.reply;

if(data.recommendations){

reply+="<br><br><b>Recommended Assessments</b><br><br>";

data.recommendations.forEach(a=>{

reply+=`<b>${a.name}</b><br>${a.description}<br><a href="${a.url}" target="_blank">Open Assessment</a><br><br>`;

});

}

addMessage(reply,"bot");

}

catch(e){

loading.remove();

addMessage("Server Error","bot");

}

}

btn.onclick=sendMessage;

input.addEventListener("keypress",e=>{

if(e.key==="Enter") sendMessage();

});