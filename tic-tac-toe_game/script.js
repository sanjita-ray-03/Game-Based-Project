let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#btn");
let newBtn= document.querySelector("#new-btn");
let msgContainer = document.querySelector(".msg-container");
let msg= document.querySelector("#msg");

let turn0 = true;

let winnPatterns = [
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,4,6],
    [3,4,5],
    [6,7,8],    
];


boxes.forEach((box) => {
    box.addEventListener("click",()=>{
        console.log("Box was clicked");
        if(turn0){
            box.innerText = "O";
            turn0 = false;
        }
        else{
            box.innerText = "X";
            turn0 = true;
        }
        box.disabled = true;

        checkWinner();
    });

});

const disablebtn = () =>{
    for(let box of boxes){
        box.disabled = true;
    }
};

const enablebtn = () =>{
    // turn0=true;
    for(let box of boxes){
       
        box.disabled = false;
        box.innerText = "";
    }
};

const  ShowWinner = (winner) =>{
    msg.innerHTML=`Congratulations, Winner is ${winner}`;
    msgContainer.classList.remove("hide");
    disablebtn();

};

const checkWinner = () => {
    for (let pattern of winnPatterns)
    {
        let pos1val= boxes[pattern[0]].innerText;
        let pos2val= boxes[pattern[1]].innerText;
        let pos3val= boxes[pattern[2]].innerText;

        if(pos1val!= "" && pos2val!="" && pos3val !="")
        {
            if(pos1val== pos2val && pos2val == pos3val)
            {
                console.log("Winner",pos2val);
                ShowWinner(pos2val);
            }
        }
    }
};

resetBtn.addEventListener("Click",() =>{
    enablebtn();
    console.log("hi");
    // boxes.innerText = "";
});
