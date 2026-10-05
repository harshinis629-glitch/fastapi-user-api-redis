# FastAPI User API with Redis Caching

A backend REST API built with **FastAPI, MySQL, SQLAlchemy, Alembic, and Redis** to demonstrate user management, database persistence, caching, cache invalidation, and performance comparison between MySQL and Redis.

This project was developed as a backend learning project to understand how a production-style API can use **Redis caching** to reduce repeated database queries and improve response performance.

---

## 🚀 Project Overview

This project provides a RESTful API for managing users.

The application stores user information permanently in a **MySQL database** and uses **Redis** as an in-memory caching layer.

When the client requests the list of users:

1. The application first checks Redis.
2. If the data exists in Redis, it returns the cached data.
3. If the data does not exist, the application queries MySQL.
4. The MySQL result is stored in Redis.
5. Future requests can retrieve the data directly from Redis.

This demonstrates the basic concept of **cache-aside caching**.

---
## Project Structure

```text
fastapi-user-api-redis/
├── .gitignore
├── README.md
├── cache.py
├── database.py
├── main.py
├── models.py
├── schemas.py


## ✨ Features

- Create users
- Retrieve all users
- Update users
- Delete users
- MySQL database persistence
- SQLAlchemy ORM
- Alembic database migrations
- Redis caching
- Cache hit and cache miss handling
- Cache expiration
- Cache invalidation
- Pydantic request/response validation
- Error handling
- Swagger/OpenAPI documentation
- MySQL vs Redis performance comparison
- Environment-based configuration
- Simple frontend interface

---

## 🛠️ Technologies Used

### Backend

- **Python**
- **FastAPI**
- **Uvicorn**

### Database

- **MySQL**
- **SQLAlchemy**


### Caching

- **Redis**
- **Memurai** for Redis-compatible caching on Windows

### Validation and Configuration

- **Pydantic**
- **python-dotenv**

##Application Architecture
                Client
                  |
                  v
             FastAPI API
                  |
                  v
             Redis Cache
              /      \
             /        \
       Cache Hit    Cache Miss
          |              |
          |              v
          |           MySQL
          |              |
          |              v
          |          Store in Redis
          |              |
          +------<-------+
                  |
                  v
               Response

📊 MySQL vs Redis
MySQL

MySQL provides:

Persistent storage
Relational database capabilities
Structured data
Transactions
SQL querying
Redis

Redis provides:

In-memory data storage
Very fast data access
Key-value storage
TTL-based expiration
Caching capabilities

In this project:

MySQL = Persistent Database
Redis  = Caching Layer

Redis does not replace MySQL. Instead, it works alongside MySQL to reduce repeated database queries.

🚀 Future Improvements

Possible future improvements include:

JWT authentication
Role-based access control
Redis-based rate limiting
Pagination
Search and filtering
Automated testing with Pytest
Docker support
CI/CD pipeline
Production deployment
Structured logging
Monitoring and metrics
Redis connection pooling

What I Learned
Built REST APIs using FastAPI
Performed CRUD operations
Connected FastAPI with MySQL
Used SQLAlchemy ORM
Implemented Redis caching
Understood cache hit and cache miss
Implemented cache expiration (TTL)
Implemented cache invalidation
Used Pydantic for validation
Handled API errors and responses
Tested APIs using Swagger/OpenAPI
Compared MySQL vs Redis performance
Used environment variables for configuration

👩‍💻 Author

Harshini S

B.Tech Information Technology


