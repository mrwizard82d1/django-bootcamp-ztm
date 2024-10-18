
We will use Render to launch our live "project"
- They have a nice free tier

Steps
- Create an account on `render.com`
- Create a new web service
- Connect to GitHub account

Launch project on `render.com`
- Select GitHub repository
- Select branch if necessary
	- I selected `2024-10`
- Change "Root Directory" if necessary
	- I selected `code/video`
	- I think this is the correct choice
		- It does contain my `requirements.txt` but may be in the wrong place
- Accept defaults for
	- Build Command
- Change Start Command
	- To `gunicorn config.wsgi`
- Choose "Free" instance type
- Do not need to select "Environment Variables" at this time
- Nor need we select any "Advanced" options
- Press "Deploy Web Service"

Review logs
- Build was successful
- Deploy may take time since it is the free tier

Review deployed application
- When ready, a URL will appear in the upper-left-hand corner of the page
- Click on URL to view deployed applications
- Some known limitations
	- Will **not** see image on "About" page
	- Text is not styled
		- I'm uncertain if this limitation still exists