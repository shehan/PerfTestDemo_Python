import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3) # endpoint wait time -- how long the user agent will wait between endpoints (1 to 3 seconds)

    @task
    def home_page(self):
         self.client.get(url="/")

    @task
    def about_page(self):
        self.client.get(url="/about")
        
# locust -f load.py --host http://localhost:8000 --users 50 --spawn-rate 5