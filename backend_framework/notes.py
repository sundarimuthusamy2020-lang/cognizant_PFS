# ==========================================
# TASK 1: UNDERSTANDING DJANGO'S REQUEST-RESPONSE CYCLE
# ==========================================

# Example Request:
# GET /api/courses/

# What happens when a user visits /api/courses/?

# 1. The browser sends an HTTP GET request to the Django application.

# 2. Django receives the request and passes it through the
#    configured middleware components.

# 3. Middleware performs tasks such as security checks,
#    session management, and authentication before the
#    request reaches the application logic.

# 4. The URL Router (urls.py) looks for a matching URL pattern.
#
#    Example:
#    path("api/courses/", views.course_list)

# 5. Once a match is found, Django calls the corresponding View.

# 6. The View contains the business logic needed to handle
#    the request. If data is required, it communicates with
#    the Model.

# 7. The Model interacts with the database and executes
#    the necessary query.
#
#    Example:
#    Course.objects.all()

# 8. The database returns the requested data to the Model.

# 9. The View processes the data and prepares an HTTP response.

# 10. Before leaving the application, the response passes
#     through the middleware stack once again.

# 11. Django sends the final response back to the browser,
#     where the user can view the result.


# Request Flow:
#
# Browser
#    ↓
# Middleware
#    ↓
# URL Router (urls.py)
#    ↓
# View (views.py)
#    ↓
# Model (models.py)
#    ↓
# Database
#    ↓
# View
#    ↓
# Middleware
#    ↓
# Browser Response


# ==========================================
# MIDDLEWARE IN DJANGO
# ==========================================

# Middleware acts as a layer between the incoming request
# and Django's core processing. It can inspect, modify,
# or block requests before they reach a View, and it can
# also modify responses before they are returned to the user.

# Examples of Built-in Middleware:

# 1. django.middleware.security.SecurityMiddleware
#    - Adds several security features to the application.
#    - Helps enforce HTTPS connections.
#    - Protects against common security risks.

# 2. django.contrib.sessions.middleware.SessionMiddleware
#    - Enables session support.
#    - Stores and retrieves session data for users.
#    - Keeps users logged in across multiple requests.


# ==========================================
# WSGI VS ASGI
# ==========================================

# WSGI (Web Server Gateway Interface)
#
# - The traditional interface used by Python web applications.
# - Handles requests synchronously, meaning each request
#   is processed in a blocking manner.
# - Works well for most standard websites and APIs.

# ASGI (Asynchronous Server Gateway Interface)
#
# - A modern interface designed for asynchronous applications.
# - Supports async code, WebSockets, and long-running connections.
# - Handles many concurrent connections more efficiently.

# Which one does Django use?

# Django projects are commonly deployed with WSGI for
# traditional web applications. However, Django also
# includes ASGI support through the asgi.py file.

# When should you choose ASGI?

# - Real-time chat applications
# - Live notifications
# - WebSocket communication
# - Streaming services
# - Applications that make extensive use of async views


# ==========================================
# MVC AND DJANGO'S MVT ARCHITECTURE
# ==========================================

# MVC stands for Model-View-Controller.

# Model
# - Manages data and database operations.

# View
# - Handles what the user sees and interacts with.

# Controller
# - Receives requests and controls the application's logic.

# Django uses a closely related pattern called MVT
# (Model-View-Template).

# MVC Model      → Django Model
# MVC View       → Django Template
# MVC Controller → Django View

# Breakdown:

# Django Model
# - Defines the application's data structure.
# - Handles communication with the database.

# Django View
# - Receives requests.
# - Executes business logic.
# - Retrieves data from Models and prepares responses.
# - Performs a role similar to the Controller in MVC.

# Django Template
# - Controls how information is displayed.
# - Generates the user interface presented in the browser.
# - Serves a role similar to the View in MVC.


# MVC → Django MVT Mapping

# Model      → Model
# View       → Template
# Controller → View