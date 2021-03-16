import { request } from '../ajax.js'

export default class Comment extends HTMLDivElement {

    constructor() {
        super();

        this.comment = {};
        this.comment.id = this.id.split('-')[1];

        this.buttons = {};
        this.buttons.like = this.querySelector('a.like');
        this.buttons.reply = this.querySelector('a.reply');
        this.buttons.edit = this.querySelector('a.edit');
        this.buttons.delete = this.querySelector('a.delete');

        this.elements = {};
        this.elements.likes = this.querySelector('span.likes');
        this.elements.body = this.querySelector('div.body');
        this.elements.actions = this.querySelector('div.actions');

        this.onLike = this.onLike.bind(this);
        this.onReply = this.onReply.bind(this);
        this.onEdit = this.onEdit.bind(this);
        this.onDelete = this.onDelete.bind(this);
    }

    connectedCallback() {
        if (this.buttons.like != null) {
            this.buttons.like.addEventListener('click', this.onLike);
        }
        if (this.buttons.reply != null) {
            this.buttons.reply.addEventListener('click', this.onReply);
        }
        if (this.buttons.edit != null) {
            this.buttons.edit.addEventListener('click', this.onEdit);
        }
        if (this.buttons.delete != null) {
            this.buttons.delete.addEventListener('click', this.onDelete);
        }
    }

    disconnectedCallback() {
        if (this.buttons.like != null) {
            this.buttons.like.removeEventListener('click', this.onLike);
        }
        if (this.buttons.reply != null) {
            this.buttons.reply.removeEventListener('click', this.onLike);
        }
        if (this.buttons.edit != null) {
            this.buttons.edit.removeEventListener('click', this.onLike);
        }
        if (this.buttons.delete != null) {
            this.buttons.delete.removeEventListener('click', this.onLike);
        }
    }

    onLike(e) {
        e.preventDefault();
        request(
            '/comments/like/' + this.comment.id + '/',
            'GET',
            null,
            (response) => {
                let res = JSON.parse(response);
                this.elements.likes.innerHTML = res.likes + ' likes';
            }
        )
    }

    onReply(e) {
        e.preventDefault();

    }

    onEdit(e) {
        e.preventDefault();
        let body = this.elements.body;
        let editor = document.createElement('textarea', { is: 'textarea-autogrow' });
        editor.value = body.innerText
        let buttonsDiv = document.createElement('div');
        buttonsDiv.classList = 'text-right';
        let validationButton = document.createElement('button');
        validationButton.innerText = 'Validate';
        validationButton.classList = 'btn btn-sm btn-primary';
        let cancelButton = document.createElement('button');
        cancelButton.innerText = 'Cancel';
        cancelButton.classList = 'btn btn-sm btn-outline-secondary mr-2';
        buttonsDiv.appendChild(cancelButton);
        buttonsDiv.appendChild(validationButton);

        body.style.display = 'none';
        this.elements.actions.style.display = 'none';
        body.insertAdjacentElement('afterEnd', editor);
        editor.insertAdjacentElement('afterEnd', buttonsDiv);

        let validateCallback = function () {
            let form = new FormData();
            form.append('body', editor.value)
            request(
                '/comments/edit/' + this.comment.id + '/',
                'POST',
                form,
                (res) => {
                    body.innerHTML = editor.value;
                },
                (err) => {
                    console.error(err);
                    alert('Unable to edit the comment.');
                }
            )
            cancelCallback();
        }
        validateCallback = validateCallback.bind(this);
        
        let cancelCallback = function () {
            body.style.display = null;
            editor.remove();
            buttonsDiv.remove();
            this.elements.actions.style.display = null;
        }
        cancelCallback = cancelCallback.bind(this);
        
        validationButton.addEventListener('click', validateCallback);
        cancelButton.addEventListener('click', cancelCallback);

        editor.focus();
    }

    onDelete(e) {
        e.preventDefault();
        request(
            '/comments/delete/' + this.comment.id + '/',
            'GET',
            null,
            (response) => {
                this.remove();
            }
        )
    }

}