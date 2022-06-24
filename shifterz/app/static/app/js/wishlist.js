function addwishlist(n){
    $.get("/addwishlist/"+n, function(data, status){
        document.getElementById('wishlist_toggle').innerHTML='<div onclick="removewishlist_2({{product.id}})" val="{{product.id}}" style="cursor: pointer;display: flex;align-items: center;margin-top: 10px;font-size: 1.1em;"><img src="https://img.icons8.com/material-sharp/24/fa314a/like--v1.png"/>remove from wishlist</div>';

    });
};

function removewishlist_2(n){
    $.get("/removewishlist/"+n, function(data){
        document.getElementById('wishlist_toggle').innerHTML='<div onclick="addwishlist({{product.id}})" val="{{product.id}}" style="cursor: pointer;display: flex;align-items: center;margin-top: 10px;font-size: 1.1em;"><img src="https://img.icons8.com/material-outlined/24/000000/like--v1.png" />add to wishlist</div>';

        });
};

function add_to_cart(n){
    $.get("/add-to-cart/"+n,function(data){
        alert("Successfully added to cart .");
    });
};
