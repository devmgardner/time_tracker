# time_tracker
This program is meant to help track time spent on freelance projects (or anything, really). The API is easy to set up; simply set up a cron job (if on Unix-based platforms) or a scheduled task to run the flask_app.py file on reboot on your desired server, ensure your ports are forwarded and any other backend work is done to be able to access the API, and that part is set.

Then, run the tk_app.py file to open the time tracker. Ensure you've entered the IP/hostname for your API in the top bar, fill out the information on the right, and start/stop as you please. Go to File->View to open the viewer screen to make a GET request to your API, and you will be able to view your time inputs as well as total time by project number.

I will (likely) be adding features to this in the future.
