import{
    countryList
} from '/codes.js';

const dropdowns=document.querySelectorAll("form .fromtoopt .indrop select");

let btn=document.querySelector("form .form button");

for(let select of dropdowns){

    for(let code in countryList){
        let newOption=document.createElement("option");
        newOption.innerText=code;
        newOption.value=code;
         
        if(select.name=='curfrom' && code=="USD"){
            newOption.selected="selected";
        }  
        else if(select.name=='curto' && code=="INR"){
            newOption.selected="selected";
        }
        select.append(newOption);
    }
    select.addEventListener("change", (evt) => {
        updateFlag(evt.target);
      });

}


let updateFlag=(element)=>{
  let currency=element.value;  
  let conCur=countryList[currency];
  let image=element.parentElement.querySelector("form .fromtoopt .flag img");
  let source=`https://flagsapi.com/${conCur}/flat/64.png`;
  image.src=source;

  
}
btn.addEventListener("click",(evt)=>{
  evt.preventDefault();
  let amount=document.querySelector("form .amt input");
  let amtVal=amount.value;
  if(amtVal<1 || amtVal==""){
    amount.value=1;
    amtVal=1;
  }
  else{
    amount.value=amtVal;
  }
  let toCur=document.querySelector("form .fromtoopt .to select");
  let fromCur=document.querySelector("form .fromtoopt .from select");
  var myHeaders = new Headers();
  myHeaders.append("apikey", "NwyvF92H6e3RzwGyzapT3NHAn6eYKRKL");

  var requestOptions = {
    method: 'GET',
    redirect: 'follow',
    headers: myHeaders
  };
fetch(`https://api.apilayer.com/exchangerates_data/convert?to=${toCur.value.toUpperCase()}&from=${fromCur.value.toUpperCase()}&amount=${amtVal}`, requestOptions)
  .then(response => response.json())
  .then(result => {
    console.log(result["result"])
    let finalRes=result["result"]
    let msg=document.querySelector("form .range p")  
    msg.innerText=`${amtVal} ${fromCur.value.toUpperCase()} = ${finalRes} ${toCur.value.toUpperCase()}`;
  }
  )
  
  .catch(error => console.log('error', error));

});

