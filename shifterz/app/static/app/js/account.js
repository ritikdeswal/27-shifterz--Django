$('#saved_button').click(function(){
    $.get("/getaddress", function(data, status){
        console.log(data);
        document.getElementById('address-all2').innerHTML='';
        for (let i=0;i<data.length;i++){
        document.getElementById('address-all2').innerHTML+="<div class='address-block' id='address_"+data[i].id+"'><h3 style='margin-bottom: 4px;'>Address "+(i+1)+"</h3><div style='display:inline-block'><div>"+ data[i]['name']+"</div><div>"+data[i]['locality']+" , " +data[i]['city']+" , " +data[i]['state']+" , " +data[i]['zipcode']+"</div></div><div style='color:#ff5454;cursor:pointer;float:right;' id='delete-address' onclick='deleteaddress(this)' val='" +data[i].id+"'>Delete</div> </div>";
        }
    });
});


function deleteaddress(n){
    let id=n.getAttribute('val');
    
    $.get("/deleteaddress/"+id, function(data, status){
        $('#address_'+id).remove();
    });
};

$( "form" ).on( "submit", function(e) {
    var dataString = $(this).serialize();
    console.log(dataString);
    // alert(dataString); return false;
    $.ajax({
        type: "POST",
        url: '/newaddress/',
        data: dataString,
        success: function (data) {
            console.log("okok");
            document.getElementById('address-all2').innerHTML='';
        for (let i=0;i<data.length;i++){
        document.getElementById('address-all2').innerHTML+="<div class='address-block' id='address_"+data[i].id+"'><h3 style='margin-bottom: 4px;'>Address "+(i+1)+"</h3><div style='display:inline-block'><div>"+ data[i]['name']+"</div><div>"+data[i]['locality']+" , " +data[i]['city']+" , " +data[i]['state']+" , " +data[i]['zipcode']+"</div></div><div style='color:#ff5454;cursor:pointer;float:right;' id='delete-address' onclick='deleteaddress(this)' val='" +data[i].id+"'>Delete</div> </div>";
        }
    
        }
    });

    e.preventDefault();
});

        
$('#wishlist_button').click(function(){
    $.get("/getwishlist", function(data, status){
        // console.log(data);
        document.getElementById('wishlist-all').innerHTML='';
        for (let i=0;i<data.length;i++){
        document.getElementById('wishlist-all').innerHTML+='<div style="display: flex;margin: 10px;"><img src="'+data[i]['image']+'" alt="" style="width: 15%;float: left;aspect-ratio: 1.0;"><div style="margin:10px; line-height: 1.3;flex-grow: 1;"><div>'+data[i]['title']+'</div><div>'+data[i]['price']+'</div></div><div style="color:#ff5454;cursor:pointer;" onclick="removewishlist(this)" val="' +data[i].id+'">Remove</div></div></div>';
        }
    });
});

function removewishlist(n){
    let id=n.getAttribute('val');
    $.get("/removewishlist/"+id, function(data, status){
        document.getElementById('wishlist-all').innerHTML='';
        for (let i=0;i<data.length;i++){
        document.getElementById('wishlist-all').innerHTML+='<div style="display: flex;margin: 10px;"><img src="'+data[i]['image']+'" alt="" style="width: 15%;float: left;aspect-ratio: 1.0;"><div style="margin:10px; line-height: 1.3;flex-grow: 1;"><div>'+data[i]['title']+'</div><div>'+data[i]['price']+'</div></div><div style="color:#ff5454;cursor:pointer;" onclick="removewishlist(this)" val="' +data[i].id+'">Remove</div></div></div>';

        }
    });
};

$('#orders_button').click(function(){
    $.get("/getorders", function(data, status){
        document.getElementById('order').innerHTML='';
        for (let i=0;i<data.length;i++){
        document.getElementById('order').innerHTML+='<div class="order-block"><h3 style="margin-bottom: 4px;">Order ID : '+data[i]['order_id']+'</h3><div style="display:inline-block"><div> Total amount : '+data[i]['amount']+'</div><div> Shipping to - '+ data[i]['locality']+' , ' +data[i]['city'] +'</div><div> Placed on '+ data[i]['date']+'</div><div style="margin: 7px 0;"> Status <span style="color: #6dca6d;font-style: italic;">'+ data[i]['status']+'</span></div></div></div>';
        }
    });
});

function del_user(){
    $.get('/del-user',function(){
        console.log("deleted");
        location.reload();
    });
};