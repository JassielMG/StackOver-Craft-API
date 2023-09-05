## StackOver Craft APP

### Description
This project is a data processing API that interacts with the Stack Overflow API to retrieve and process data about questions and answers related to specific topics. The processed data is then exposed through a FastAPI-based API to provide insights and summaries.

Key Technologies Used:

- FastAPI: A modern, fast (high-performance) web framework for building APIs.
- Pandas: A powerful data manipulation and analysis library.
- Requests: A Python library for making HTTP requests to external APIs.
- Docker: Containerization technology for easier deployment and management.

The main features of this project include:
- Fetching data from the Stack Overflow API.
- Preprocessing and cleaning the retrieved data.
- Calculating insights such as answer statistics, less viewed questions, and more.
- Providing these insights through API endpoints for easy access.

### Installation
To run this project using Docker, follow these steps:

1.- Clone the repository
```
git clone https://github.com/JassielMG/StackOver-Craft-API.git
```

2.- Build the Docker image
```
docker build -t fast-app .
```

3.- Run the Docker container
```
docker run -d --name fast-app -p 8000:8000 fast-app
```

4.- Open the API in your browser
```
http://localhost:8000
```

If you want to interact with the code making modifications, you can run the project using docker volumes. This way, you can make changes to the code and see the results in real-time.

```
docker run -d --name fast-app -p 8000:8000 -v $(pwd):/app fast-app
```