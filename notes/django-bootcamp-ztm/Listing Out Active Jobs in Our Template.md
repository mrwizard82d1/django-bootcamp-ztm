Change `index` to:
- Get all active job postings (`active_jobs`)

Create a `context` variable to capture these active job postings

Create an `.html` file to render our view
- `job_board/templates/job_board/index.html`
	- But only need `job_board/index.html` in call to `render()`

The `index.html` file
- Renders all active jobs in an unordered list
- Uses `{% for posting... %} ... {% endfor %}` to loop over all postings in `context.job_postings`
- Renders details of each active job posting inside `<li> ... </li>` tags
	- `{{ posting.title }} | {{ posting.description }} | ${{ posting.salary }}`

Spoilers
- Current output is very functional
- Text is **not** capitalized
- Salary is not well formatted (no thousands separator)

