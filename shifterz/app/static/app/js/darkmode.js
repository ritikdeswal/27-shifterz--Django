let lightMode = localStorage.getItem('lightMode'); 

        const lightModeToggle = document.querySelector('#dark-toggle');

        const enableLightMode = () => {
        document.body.classList.add('lightmode');
        document.getElementById('logo').src="{%static 'app/brand-img/black.png' %}";
        localStorage.setItem('lightMode', 'enabled');
        }

        const disableLightMode = () => {
        document.body.classList.remove('lightmode');
        document.getElementById('logo').src="{%static 'app/brand-img/white.png' %}";
        localStorage.setItem('lightMode', null);
        }
        

        if (lightMode === 'enabled') {
        enableLightMode();
        }

        lightModeToggle.addEventListener('click', () => {
        lightMode = localStorage.getItem('lightMode'); 
        
        if (lightMode !== 'enabled') {
            enableLightMode(); 
        } else {  
            disableLightMode(); 
        }
        });
