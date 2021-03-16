function debounce(callback, delay){
    var timer;
    return function(){
        var args = arguments;
        var context = this;
        clearTimeout(timer);
        timer = setTimeout(function(){
            callback.apply(context, args);
        }, delay)
    }
}

export default class TextareaAutogrow extends HTMLTextAreaElement {

    constructor() {
        super();
        this.onFocus = this.onFocus.bind(this);
        this.onResize = debounce(this.onResize.bind(this), 50);
        this.autogrow = this.autogrow.bind(this);

        this.style.resize = 'none';
    }

    connectedCallback() {
        this.addEventListener('focus', this.onFocus);
        this.addEventListener('input', this.autogrow);
    }
    
    disconnectedCallback() {
        this.removeEventListener('focus', this.onFocus);
        this.removeEventListener('input', this.autogrow);
        window.removeEventListener('resize', this.onResize);
    }

    onFocus() {
        this.style.overflow = 'hidden';
        this.autogrow();
        window.addEventListener('resize', this.onResize);
        this.removeEventListener('focus', this.onFocus);
    }

    onResize() {
        this.autogrow();
    }
    
    autogrow() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    }

}
