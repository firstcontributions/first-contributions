const count_heading=document.getElementById("total-count")
const increass_button=document.getElementById("increass-button")
const decreass_button=document.getElementById("decreass-button")
const warning=document.getElementById("warning")
increass_button.addEventListener("click",(e)=>{
    e.preventDefault()
    warning.innerHTML=null
    let currentcount=count_heading.innerHTML
    currentcount++
    count_heading.innerHTML=currentcount
})

decreass_button.addEventListener("click",(e)=>{
    e.preventDefault()
    let currentcount=parseInt(count_heading.innerHTML)
    if(currentcount>0){
        console.log(typeof currentcount)
        currentcount--;
        count_heading.innerHTML=currentcount
    }else{
        warning.innerHTML="Count can't be less than 0"
    }
})