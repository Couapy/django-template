import Comment from './elements/Comment.js';
import TextareaAutogrow from './elements/TextareaAutogrow.js';

customElements.define("div-comment", Comment, { extends: 'div' });
customElements.define("textarea-autogrow", TextareaAutogrow, { extends: 'textarea' });

document.addEventListener('DOMContentLoaded', () => {
    if (document.location.hash.match('#comment-')) {
        let element = document.querySelector(document.location.hash)
        if (element) {
            window.scroll({
                left: 0,
                top: element.offsetTop - 200,
                behavior: 'smooth',
            })
        }
    }
})

console.info("[INFO][COMMENTS] App loaded");
