Let's get trips list set up

Create logout template first
- Create `logged_out.html` in `templates/registration`
- Add `h1` tag: "You've been logged out."
- Add link to return to log in

Edit `trip_list.html` to include a link to the login page
- Block rendered **conditionally**; 
	- If logged in
		- Display a status message "Logged in as {{ user.username }}"
		- Display a link to the logout page
	- Otherwise (not logged in)
		- Display a link to login

The preceding approach **does not work**
- Instead, it generates an HTML 405 error with the following logged text:

```
[13/Nov/2024 20:21:11] "GET /accounts/logout/ HTTP/1.1" 405 0
Method Not Allowed (GET): /accounts/logout/
Method Not Allowed: /accounts/logout/
```

- I believe this error occurs because of a change in Django logout processing in Django ~5.
