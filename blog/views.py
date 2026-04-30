from django.shortcuts import render
from datetime import date
# Hardcoded list of blog posts
def post_list(request):
    # This is your hardcoded list of blog posts
    blog_posts = [
        {
            'id': 1,
            'title': 'Getting Started with Django',
            'author': 'John Doe',
            'published_date': date(2024, 1, 15),
            'summary': 'Learn how to set up your first Django project and create basic views.',
            'likes': 42,
            'is_new': True  # Custom field to indicate if the post is new
        },
        {
            'id': 2,
            'title': 'Understanding Django Templates',
            'author': 'Jane Smith',
            'published_date': date(2024, 1, 20),
            'summary': 'Master the Django template language with variables, tags, and filters.',
            'likes': 38,
            'is_new': False
        },
        {
            'id': 3,
            'title': 'Working with Static Files',
            'author': 'Mike Johnson',
            'published_date': date(2024, 1, 25),
            'summary': 'Learn how to manage CSS, JavaScript, and images in Django.',
            'likes': 55,
            'is_new': False
        },
        {
            'id': 4,
            'title': 'Django Models and Databases',
            'author': 'Sarah Williams',
            'published_date': date(2024, 1, 30),
            'summary': 'Create database models and perform CRUD operations in Django.',
            'likes': 61,
            'is_new': False
        },
        {
            'id': 5,
            'title': 'Building REST APIs with DRF',
            'author': 'Alex Chen',
            'published_date': date(2024, 2, 5),
            'summary': 'Learn how to build powerful REST APIs using Django REST Framework.',
            'likes': 47,
            'is_new': False
        }
    ]
    
    # Create context dictionary with data to pass to template
    context = {
        'posts': blog_posts,
        'blog_title': 'Awesome Django Blog',
        'total_posts': len(blog_posts),
        'show_sidebar': True,
    }
    
    # Render the template with context
    return render(request, 'blog/post_list.html', context)


# Alternative view: Show single post
def post_detail(request, post_id):
    # Hardcoded posts (same as above)
    blog_posts = [...]  # Same list as above
    
    # Find the specific post
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    
    context = {
        'post': post,
        'post_id': post_id
    }
    
    return render(request, 'blog/post_detail.html', context)