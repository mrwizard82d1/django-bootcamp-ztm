Time to actually get data from our form

Steps
- Add a `method=POST` attribute to our `form` in `create.html`
	- A `POST` request can carry data
- Change `views.add_link()` to get the data from the **request**
	- To investigate this change, we'll simply print the post request
		- `print(request.POST)`
		- Remember that this output will appear in the output window of the server

Handling our "CSRF verification failed. Request aborted." message
- CSRF: Client Site Request Forgery
- To correct, we must submit a random token whenever we submit the form so that the Django server can verify that the request came from a valid source
- Modify `create.html` by adding this token to the `form` block

```html
{% csrf_token %}
```

- This action causes our application to generate and submit a CSRF token as part of the request

Two changes
- The URL, after pressing the `Create` button, no longer contains the appended question mark ('?')
- The console output now reports that it contains a CSRF token when printing `request.POST`

Generally working now but we **do not see** our link data
- Add the `name="link"` attribute to our first `input` tag
- Now, after adding some text and pressing the 'Create' button
	- We see the text from our first `input` field in the result `QueryDict`

This code now works as expected; however, we will next investigate using **Django forms** to create our link form
- This feature makes creating and consuming forms "super, super" easy
