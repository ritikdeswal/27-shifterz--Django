# 27-shifterz--Django
 
This webapp was created in **HTML, CSS, Javascript ,Jquery and
AJAX**.\
Backend : **python + Django**.\
used **Google OAuth API** for signup.\
used **Razorpay Payment API**.\
Deployed on **AWS**.

## Python modules 
```python
from django.conf.urls import url
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import (Customer,Product,Cart,OrderPlaced,Wishlist)
from shifterz import settings
from django.contrib.sites.shortcuts import get_current_site
from json import dump, dumps
import razorpay
from django.views.decorators.csrf import csrf_exempt
```


## Logo Designing
![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/logo_design.png)

## Layout Designing
![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/layout_design.png)

## Final preview
![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/homepage.png)

![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/2.png)

![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/3.png)

![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/4.png)

![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/5.png)

![](https://github.com/ritikdeswal/27-shifterz--Django/blob/main/screenshots/6.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
