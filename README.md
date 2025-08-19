# News Automation System

## Features
- Automates the collection of news articles from various sources.
- Provides an API for accessing the collected news.
- Supports filtering news by categories, keywords, etc.
- Allows scheduling of regular news updates.
  
## Installation Instructions
1. Clone the repository:
   ```
   git clone https://github.com/wilsonwen77/news-automation-system.git
   ```
2. Navigate to the project directory:
   ```
   cd news-automation-system
   ```
3. Install dependencies:
   ```
   npm install
   ```

## API Documentation
- **GET /api/news**: Fetch all news articles.
- **GET /api/news/:id**: Fetch a specific news article by ID.
- **POST /api/news**: Add a new news article.
  
## Usage Examples
- To fetch all news articles, you can use:
   ```bash
   curl http://localhost:3000/api/news
   ```
- To fetch a specific article:
   ```bash
   curl http://localhost:3000/api/news/1
   ```
- To add a new article:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"title": "New Article", "content": "Article content goes here."}' http://localhost:3000/api/news
   ```
