---
title: "JS Bookmarklets"
date: 2021-09-29T00:00:00-04:00
draft: true
tags: [tech]
---

I have way too many browser bookmarks, but there is one folder of bookmarks I use regularly: bookmarklets.

Just as you can save an HTML webpage as a bookmark, you can also save Javascript script as a bookmarklet, basically turning your bookmarks bar into a control panel.

```js
javascript:(function(){alert('hello!')})()
```

caption: a very basic javascript snippet

**Caution: make sure you know exactly what the bookmarklet is going to do before you run it or add it to your bookmarks bar. JS can grab passwords, cookies, and other data from your browser. If you don't trust the developer or the code, don't use it!**

## My Favorites

**enable context menu**

```js
javascript:(function(w){var arr=['contextmenu','copy','cut','paste','mousedown','mouseup','beforeunload','beforeprint'];for(var i=0,x;x=arr[i];i++){if(w['on'+x])w['on'+x]=null;w.addEventListener(x,function(e){e.stopPropagation()},true);};for(var j=0,f;f=w.frames[j];j++){try{arguments.callee(f)}catch(e){}}})(window)
```

<summary>Show code</summary>

<details>


Taken from https://stackoverflow.com/a/12819640/2727510

```js
javascript:(function(w) {
    var arr = ['contextmenu','copy','cut','paste','mousedown','mouseup','beforeunload','beforeprint'];
    for(var i = 0, x; x = arr[i]; i++) {
        if(w['on' + x])
            w['on' + x] = null;
        w.addEventListener(x, function(e) {
            e.stopPropagation()
        }, true);
    };
    for(var j = 0, f; f = w.frames[j]; j++) {
        try {
            arguments.callee(f)
        } catch (e) {}
    }
})(window);
```

</details>

**remove paywall**

```js
javascript: (function() {document.querySelector('html').style.overflow = 'visible';document.querySelector('body').style.overflow = 'visible';el = document.querySelector('.fbs-auth__adblock'); /* forbes */if (el) el.remove(); /* forbes */el = document.querySelector('#fusion-app~div');%20/*%20wapo%20*/if%20(el)%20el.remove();%20/*%20wapo%20*/document.querySelector('body').removeAttribute('data-paywall-overlay-status');%20/*%20bloomberg%20*/el%20=%20document.querySelector('#graphics-paywall-overlay');%20/*%20bloomberg%20*/if%20(el)%20el.remove();%20/*%20bloomberg%20*/document.querySelector('body').classList%20=%20[];%20/*%20businessinsider%20*/el%20=%20document.querySelector('.tp-backdrop');%20/*%20businessinsider%20*/if%20(el)%20el.remove();%20/*%20businessinsider%20*/el%20=%20document.querySelector('.tp-modal');%20/*%20businessinsider%20*/if%20(el)%20el.remove();%20/*%20businessinsider%20*/})()
```

Actually we can replace the above with [Outline](https://www.online-tech-tips.com/computer-tips/12-ways-to-get-past-a-paywall/)

**view/get/set cookie**

More for developers and hackers

**search custom website**

google.com/?q=TEST
duckduckgo.com/?q=TEST
amazon.com/s?k=amazon

POST

Jira/Confluence
Facebook
