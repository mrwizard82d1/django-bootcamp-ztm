The admin interface calls `JobPosting.__str__()` when displaying a job posting
- The default behavior returns a string like `JobPosting object...`

To override this behavior, we implement the member:
- `JobPosting.__str__()`
- This function returns a string that hopefully better communicates the job posting with actual human users

