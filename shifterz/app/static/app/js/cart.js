function remove_from_cart(n){
    $.get("/remove-from-cart/"+n,function(data){
        console.log(data);
            alert("Successfully removed from cart .");
            $('#total_sum').html('$ '+data[0]['total']);
            $('#shipping_charges').html('$ '+data[0]['shipping']);
            $('#total_2').html('$ '+data[0]['total2']);
            $('#block_'+n).remove();

        });
};

function minus_cart(n){
    $.get("/minus-cart/"+n,function(data){
        // console.log(data);
            $('#total_sum').html('$ '+data[0]['total']);
            $('#shipping_charges').html('$ '+data[0]['shipping']);
            $('#total_2').html('$ '+data[0]['total2']);
            $('#quantity_value_'+n).html(data[0]['that_quantity']);
        });
};

function plus_cart(n){
    $.get("/plus-cart/"+n,function(data){
        // console.log(data);
            $('#total_sum').html('$ '+data[0]['total']);
            $('#shipping_charges').html('$ '+data[0]['shipping']);
            $('#total_2').html('$ '+data[0]['total2']);
            $('#quantity_value_'+n).html(data[0]['that_quantity']);
        });
};