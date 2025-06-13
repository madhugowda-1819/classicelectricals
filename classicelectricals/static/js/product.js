let productdata={id:'A120',
                imageurl:'./images/shoe.png',
                pname:"Red Tape's shoes for men",
                price:1299,
                qty:1};
                
let htmlcode=`<tr>
                <td>${productdata.id}</td>
                <td><img src="${productdata.imageurl}" alt="" width="50px" height="50px" text-align="center"></td>
                <td>${productdata.pname}</td>
                <td>&#8377; ${productdata.price}.00</td>
                <td>
                <i class="bi bi-dash-circle-fill" onclick="decQty()"></i>
                <span id="display-qty"></span>
                <i class="bi bi-plus-circle-fill" onclick="incQty()"></i>
                </td>
                <td >&#8377;<span id="total-p"></span>.00</td>
              </tr>`;


let product=document.getElementById('display-data');
product.innerHTML=htmlcode;
let displaytotal=document.getElementById('total-p');
let displayqty=document.getElementById('display-qty');

    displaytotal.innerHTML=productdata.price;
    
    displayqty.textContent=productdata.qty;

    function incQty()
    {
        productdata.qty++;
        displayqty.textContent=productdata.qty;
        totalprice();
    }
    
    function decQty()
    {
        if(productdata.qty>1)
        {
            productdata.qty--;
            displayqty.textContent=productdata.qty;
            totalprice();
        }
        else
        { 
            displayqty.textContent=1;
            totalprice();
        }
    }    
    function totalprice(){
        displaytotal.textContent=(productdata.price*productdata.qty);
    }


   
