from django.shortcuts import render
from datetime import datetime, timedelta

def headline_ticker(request):
    # Hardcoded news headlines
    headlines = [
        {
            'id': 1,
            'title': 'breaking news: python releases new version with major performance improvements',
            'category': 'technology',
            'published_date': datetime.now(),
            'content': 'The Python Software Foundation has announced the release of Python 3.13 today. This version includes significant performance improvements, better error messages, and new features that developers have been requesting for years. The community is excited about these changes.',
            'views': 82345
        },
        {
            'id': 2,
            'title': 'django 5.0 introduces simplified templates and full async support',
            'category': 'programming',
            'published_date': datetime.now() - timedelta(hours=5),
            'content': 'Django 5.0 brings revolutionary changes to the web framework. With simplified template syntax and complete async support for views and middleware, developers can build faster applications with less code.',
            'views': 45231
        },
        {
            'id': 3,
            'title': 'artificial intelligence breakthrough: new model understands human emotions',
            'category': 'ai news',
            'published_date': datetime.now() - timedelta(days=1),
            'content': 'Researchers have developed an AI model that can understand and respond to human emotions with unprecedented accuracy. This breakthrough could revolutionize mental health support and customer service applications.',
            'views': 124567
        },
        {
            'id': 4,
            'title': 'tech giant unveils revolutionary smartphone with holographic display',
            'category': 'consumer tech',
            'published_date': datetime.now() - timedelta(days=2),
            'content': 'A major technology company has unveiled a smartphone featuring a holographic display that projects 3D images without special glasses. The device is expected to launch next quarter.',
            'views': 67342
        },
        {
            'id': 5,
            'title': 'cybersecurity alert: critical vulnerability discovered affecting millions',
            'category': 'security',
            'published_date': datetime.now() - timedelta(hours=12),
            'content': 'Security researchers have discovered a critical vulnerability affecting millions of systems worldwide. Users are strongly advised to update their software immediately to protect against potential attacks.',
            'views': 98765
        },
        {
            'id': 6,
            'title': 'space exploration: nasa announces new mission to europa',
            'category': 'science',
            'published_date': datetime.now() - timedelta(days=3),
            'content': 'NASA has announced an ambitious new mission to explore Europa, one of Jupiter\'s moons. The mission aims to search for signs of life beneath the moon\'s icy surface.',
            'views': 34567
        }
    ]
    
    # Breaking news ticker items
    ticker_headlines = [
        "BREAKING: Major tech acquisition announced today worth $50 billion",
        "WEATHER ALERT: Hurricane warning issued for coastal regions",
        "SPORTS: Underdog team advances to championship finals in stunning upset",
        "MARKETS: Stock indices reach all-time highs after positive economic data",
        "SCIENCE: New exoplanet discovered in habitable zone of distant star",
        "HEALTH: Breakthrough vaccine shows 95% effectiveness against new strain"
    ]
    
    context = {
        'headlines': headlines,
        'ticker_headlines': ticker_headlines,
        'current_time': datetime.now(),
        'total_articles': len(headlines),
    }
    
    return render(request, 'news/headline_ticker.html', context)