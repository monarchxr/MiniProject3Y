document.getElementById("resume_form").addEventListener("submit", async function(e){
    e.preventDefault();
    //this is to stop default form submission


    const resume = document.getElementById("resume").files[0];
    const jobRole = document.getElementById("job_role").value;

    if(!resume.files.length){
        alert("Please upload a resume before submitting.");
        return
    }
})

const btn = document.getElementById("submit_button");

btn.addEventListener('click', ()=>{
    alert('Successfully submitted!');
});