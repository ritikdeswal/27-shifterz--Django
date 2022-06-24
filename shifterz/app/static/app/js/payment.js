var options = {
    "key": "rzp_test_mYGcz7UrWYirHW", // Enter the Key ID generated from the Dashboard
    // "amount": "{% widthratio final_price 1 100 %}", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    "amount": "{{total2}}", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    "currency": "AUD",
    "name": "27Shifterz",
    "description": "Test Transaction",
    "order_id": "{{order_id}}", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
    "callback_url": "{{callback_url}}",
    "prefill": {
      "name": "{{request.user.name}}",
      "email": "{{request.user.email}}",
      "contact": "+91" + "{{request.user.phone}}"
    },
  };
  var rzp1 = new Razorpay(options);
  document.getElementById('paynow').onclick = function (e) {
    $.get('/success/'+id,function(){    
    });    
    
    rzp1.open();
    e.preventDefault();
    
  };