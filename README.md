# Blog Platform API

Welcome to the **Blog Platform API**, a Django-based RESTful API for managing blog posts, categories, likes, dislikes, and comments. This API allows authenticated users to create posts, interact with them (like, dislike, and comment), and organize posts by categories.

---

## Features

### Post Management
- List all posts
- Create new posts (authenticated users only)
- Like and dislike posts (authenticated users only)
- Add comments to posts (authenticated users only)

### Category Management
- List all categories
- Retrieve posts by category with pagination

### Signals
- Automatically handle conflicts between likes and dislikes for a post using Django signals.

### Documentation
- Interactive API documentation with Swagger and ReDoc.

---

## Installation and Setup

### Prerequisites
- Python 3.10 or higher
- Django 4.x
- Django REST Framework (DRF)
- drf-yasg for API documentation

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedElgindy/BlogAPI/
   cd apiProject
   ```

2. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   - ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## API Endpoints

### Public Endpoints
- `GET /blog/posts` - List all posts
- `GET /blog/categories` - List all categories
- `GET /blog/category/<int:category_id>/posts` - List posts in a specific category with pagination

### Authenticated Endpoints
- `POST /blog/create-post` - Create a new post
- `POST /blog/like/<int:pk>` - Like a post
- `POST /blog/dislike/<int:pk>` - Dislike a post
- `POST /blog/comment/<int:pk>` - Add a comment to a post

---

## How It Works

### Likes and Dislikes
- A user can only like or dislike a post, but not both. If a user tries to like a post they have already disliked (or vice versa), the conflict is resolved automatically by Django signals.

### Comments
- Users can add comments to posts. Each comment must include content.

### Pagination
- Post listings by category are paginated, with a default page size of 10 posts.

---

## Future Plans

1. **User Profiles**
   - Allow users to create and update their profiles.
   - Display user activity, such as posts created, likes, and comments.

2. **Search Functionality**
   - Implement search for posts by title, content, and category.

3. **Post Drafts**
   - Enable saving posts as drafts before publishing them.

4. **Notifications**
   - Notify users when their posts receive likes, dislikes, or comments.

5. **Advanced Filtering**
   - Add filters for posts based on date created, number of likes, and other criteria.

6. **Enhanced Security**
   - Add rate limiting to prevent abuse of API endpoints.
   - Implement JWT-based authentication.

7. **Frontend Integration**
   - Develop a React or Vue.js frontend to consume the API.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests for new features, bug fixes, or improvements.

---

## Contact
For questions or support, please contact:
- **Ahmed Alaa Mohamed**
- Email: ahmedalaa1316@gmail.com
- LinkedIn: [www.linkedin.com/in/ahmed-elgindy-a855161b3](www.linkedin.com/in/ahmed-elgindy-a855161b3)

