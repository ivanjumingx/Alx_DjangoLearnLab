# Django Blog Project

## Overview

This project is a Django-based blog application that allows users to manage blog posts. Users can perform Create, Read, Update, and Delete (CRUD) operations on blog posts. This README file provides a comprehensive guide to the project's setup, features, and usage.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Blog Post Management**:
  - **List**: View a list of all blog posts.
  - **Detail**: View details of individual blog posts.
  - **Create**: Create new blog posts.
  - **Update**: Edit existing blog posts.
  - **Delete**: Delete blog posts.

## Project Structure

- `blog/` - Contains the core application code for the blog.
  - `migrations/` - Database migrations.
  - `templates/` - HTML templates for the blog.
    - `blog/` - Templates for blog posts.
  - `static/` - Static files (CSS, JavaScript).
  - `models.py` - Django models for the blog.
  - `views.py` - Views for handling blog post operations.
  - `forms.py` - Forms for creating and editing blog posts.
  - `urls.py` - URL routing for the blog.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/django_blog.git
   cd django_blog
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.

## URL Routing

- `/register/` - User registration page.
- `/login/` - User login page.
- `/logout/` - User logout page.
- `/profile/` - User profile page.
- `/posts/` - List all blog posts.
- `/posts/<int:pk>/` - View details of a specific blog post.
- `/posts/new/` - Create a new blog post.
- `/posts/<int:pk>/edit/` - Edit an existing blog post.
- `/posts/<int:pk>/delete/` - Delete a blog post.

## Templates

- **List View**: `blog/templates/blog/post_list.html`
- **Detail View**: `blog/templates/blog/post_detail.html`
- **Form View**: `blog/templates/blog/post_form.html`
- **Delete Confirmation**: `blog/templates/blog/post_confirm_delete.html`

## Forms

- `PostForm`: Used for creating and editing blog posts.

## Testing

- Views: Test CRUD functionality and user permissions.
- Forms: Ensure data validation and error handling.
- Navigation: Verify that all links and navigation paths are correct.

## Documentation

- The features are documented in the code comments and inline documentation.

## Contributing

Feel free to open issues and submit pull requests. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Bevolution License - see the [LICENSE](LICENSE) file for details.
