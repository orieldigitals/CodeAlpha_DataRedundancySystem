document.addEventListener("DOMContentLoaded",function(){

console.log("Platform Loaded Successfully");

const cards=document.querySelectorAll(".card");

cards.forEach(function(card){

card.addEventListener("mouseenter",function(){

card.style.transform="translateY(-6px)";

});

card.addEventListener("mouseleave",function(){

card.style.transform="translateY(0px)";

});

});

});