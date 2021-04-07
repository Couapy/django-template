var csrf_token = getCookie('csrftoken');

/**
 * Get the cookie value from his name
 * This is the Django function from the documentation
 * Source : https://docs.djangoproject.com/fr/3.0/ref/csrf/
 * @param {string} name 
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * This function call an url to deliver a form
 * @param {string} url The url for the request
 * @param {Form} form The form data to transmit
 * @param {callback} success_callback This callback is called on success
 * @param {callback} error_callback This callback is called on error
 */
export function request(url, method='POST', form=null, success_callback = function () { }, error_callback = function () { }) {
    let httpRequest = new XMLHttpRequest()

    // Open the URL
    httpRequest.open(method, url, true);

    // Enable POST data
    httpRequest.setRequestHeader("X-CSRFToken", csrf_token);

    // Add events listeners
    httpRequest.addEventListener('readystatechange', function () {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                success_callback(httpRequest.responseText)
            }
            else {
                error_callback(httpRequest.responseText)
            }
        }
    })

    // Send the httpRequest
    httpRequest.send(form);
}
