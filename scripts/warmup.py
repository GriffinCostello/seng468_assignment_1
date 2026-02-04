"""
Warms the System so we can run our tests on a hot cache.
Uses varying, realistic accesses to determine the number of requests
to each endpoint to simulate traffic.
"""

from locust import HttpUser, task, between
import random

class BookStoreUser(HttpUser):
    wait_time = between(0.5, 2.0)

    @task(4)
    def browse_books(self):
        self.client.get("/api/books?page=1")

    @task(3)
    def search_books(self):
        queries = ["python", "data", "science", "history", "novel"]
        q = random.choice(queries)
        self.client.get(f"/api/search?q={q}")

    @task(2)
    def view_book_detail(self):
        book_id = random.randint(1, 10000)
        self.client.get(f"/api/books/{book_id}")

    @task(1)
    def get_recommendations(self):
        self.client.get("/api/recommendations")

    @task(1)
    def view_cart(self):
        self.client.get("/api/cart")
