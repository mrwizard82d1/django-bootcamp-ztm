An introduction to terminology

Web browser
- Device to "surf" the internet

Web Server
- No keyboard, screen, etc
- Connected to the internet
- Have IP address
	- Which may be tied to a URL
		- Easier to remember

How does client interact with server
- Client sends a request 
	- For example, an HTTP "GET" request
		- See Mozilla MDN docs for definition
		- Only retrieves (specified) data
			- For example, a form page
- Server returns a response
- An HTTP "POST" request
	- Often causes a change in state
	- Or a side-effect
	- For example, creating an account via a signup

Supports **multiple and concurrent** clients submitting requests
