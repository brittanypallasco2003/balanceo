from locust import  HttpUser, task, between

class MyUser(HttpUser):
    wait_time=between(1,2)
    @task
    def indx(self):
        responese=self.client.get("http://servidor1:5000/")
        