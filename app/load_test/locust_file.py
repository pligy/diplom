from locust import User, task, between
import requests
import json
import random
import time


class LoadTester(User):
    wait_time = between(5, 15)


    @task(1)
    def post_location(self):
        url = 'http://0.0.0.0:8000/users/'

        # Генерация случайных данных для каждого запроса
        lastnames = ["Doe", "Smith", "Johnson", "Williams", "Platov", "Molodcov", "Platova", "Legendov"]
        firstnames = ["John", "Jane", "James", "Jill", "Igor", "Vasya", "Ivan", "Petya"]
        usernames = [f"{first}_{last}" for first in firstnames for last in lastnames]
        passwords = ["password123", "securepass", "admin123", "testpass"]
        roles = ["driver", "passenger"]

        data = {
            "lastname": random.choice(lastnames),
            "firstname": random.choice(firstnames),
            "username": random.choice(usernames),
            "password": random.choice(passwords),
            "role": random.choice(roles)
        }
        headers = {'Content-Type': 'application/json'}

        start_time = time.time()
        response = requests.post(url, headers=headers, data=json.dumps(data))
        execution_time = time.time() - start_time
        self.environment.events.request_success.fire(request_type="POST", name="/users", response_time=execution_time,
                                                     response_length=0)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")


if __name__ == "__main__":
    import locust

    locust.main()