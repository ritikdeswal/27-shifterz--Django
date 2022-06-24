function changeit(id) {
    var flag=id.getAttribute("name");
    if (flag=="dark") {
      id.setAttribute("name","light");
      document.documentElement.style.setProperty('--bgclr', 'white');
      document.documentElement.style.setProperty('--txtclr', 'black');
      document.documentElement.style.setProperty('--footerclr', '#d9d9d9');
    
    }
    if (flag=="light") {
      id.setAttribute("name","dark");
      document.documentElement.style.setProperty('--bgclr', 'rgb(25,26,27)');
      document.documentElement.style.setProperty('--txtclr', 'white');
      document.documentElement.style.setProperty('--footerclr', '#262729');
    }
    }
    