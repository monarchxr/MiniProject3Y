const btn = document.getElementById("submit_button");

btn.addEventListener('click', ()=>{
    alert('Successfully submitted!');
});

document.getElementById("resume_form").addEventListener("submit", async function(e){
    e.preventDefault();
    //this is to stop default form submission
})

