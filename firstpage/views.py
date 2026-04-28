from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("""
        <h1>Welcome to My Personal Profile</h1>
        <p>Hi! I'm Ruchika. Welcome to my personal website.</p>
        <nav>
            <a href="/home/">Home</a> | 
            <a href="/about/">About</a> | 
            <a href="/contact/">Contact</a>
        </nav>
    """)

def about(request):
    return HttpResponse("""
        <h1>About Me</h1>
        <p>Name: Ruchika</p>
        <p>Skills: Python, Django, Web Development</p>
        <p>Experience: 2+ years in programming</p>
        <nav>
            <a href="/home/">Home</a> | 
            <a href="/about/">About</a> | 
            <a href="/contact/">Contact</a>
        </nav>
    """)

def contact(request):
    return HttpResponse("""
        <h1>Contact Me</h1>
        <p>Email: ruchika@example.com</p>
        <nav>
            <a href="/home/">Home</a> | 
            <a href="/about/">About</a> | 
            <a href="/contact/">Contact</a>
        </nav>
    """)

# dynamic segments
def user_profile(request, username):
    return HttpResponse(f"""
        <h1>Profile Page</h1>
        <p>Welcome, {username}!</p>
        <p>This is your personal profile page.</p>
        <nav>
            <a href="/home/">Home</a> | 
            <a href="/about/">About</a> | 
            <a href="/contact/">Contact</a>
        </nav>
    """)