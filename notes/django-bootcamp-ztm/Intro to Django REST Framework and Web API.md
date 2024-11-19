We are gong to look at Django REST Framework

We have talked about having
- A server serving pages to
- A client

How to access our project from different clients
- Currently, we get back an HTML page
- Perhaps not ideal for other devices
- Possible because of **the data**
- The client then has full responsibility for displaying the data

General structure
- Server serves `JSON`
- Client have full responsibility for dispay

Contrast
- An HTML document describes in some detail how to display the data
- `JSON` data similar to a Python dictionary
	- Just **structured data**

Django REST Framework
- A library that allows one to create web/REST APIs
	- Serves the **data**