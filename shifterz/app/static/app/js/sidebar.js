sidebar=document.getElementById('sidebar');

function viewSignup() {
//    sidebar.style.display='block';
   sidebar.style.cssText='right:0;';
   
}
function hideSidebar() {
    console.log("okok");
//    sidebar.style.display='none';
sidebar.style.cssText='right:-25%;';
if (x.matches) { // If media query matches
    sidebar.style.cssText='right:-60%;';
    }
   sidebar.classList.remove('sidebar-extend');
   document.getElementById('accountitem').style.width='100%';
   document.getElementById('accountitem').style.display='block';
   document.getElementById('main-content').style.display='none';
}

function extend() {
    sidebar.classList.add('sidebar-extend');
    document.getElementById('accountitem').style.width='30%';
    if (x.matches) { // If media query matches
        document.getElementById('accountitem').style.display='flex';
        console.log("flex again");
    }
    document.getElementById('main-content').style.display='unset';

}
var x = window.matchMedia("(max-width: 700px)")
// x.addEventListener();
function savedAddressView(el){
    document.getElementById('address-all').style.display='unset';
    document.getElementById('wishlist-all').style.display='none';
    document.getElementById('order').style.display='none';
    document.getElementById('orders_button').classList.remove('underlined');
    document.getElementById('wishlist_button').classList.remove('underlined');
    el.classList.add('underlined');
    
}
function wishlistView(el){
    document.getElementById('address-all').style.display='none';
    document.getElementById('wishlist-all').style.display='unset';
    document.getElementById('order').style.display='none';
    document.getElementById('saved_button').classList.remove('underlined');
    document.getElementById('orders_button').classList.remove('underlined');
    el.classList.add('underlined');

    
}
function ordersView(el){
    document.getElementById('address-all').style.display='none';
    document.getElementById('wishlist-all').style.display='none';
    document.getElementById('order').style.display='unset';
    el.classList.add('underlined');
    document.getElementById('saved_button').classList.remove('underlined');
    document.getElementById('wishlist_button').classList.remove('underlined');
    
}