from locust import HttpUser, task, between

class GameSalesUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def index_page(self):
        self.client.get("/")
    
    @task(3)
    def survey_page(self):
        self.client.get("/survey/")