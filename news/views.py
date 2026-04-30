from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime, timedelta

def headline_ticker(request):
    # Hardcoded news headlines
    news_headlines = [
        {
            'id': 1,
            'title': 'breaking news: python releases new version with awesome features',
            'published_date': datetime.now(),
            'content': 'The Python Software Foundation has announced the release of Python 3.13 with significant performance improvements and new features that developers have been waiting for.',
            'category': 'TECHNOLOGY',
            'views': 15423
        },
        {
            'id': 2,
            'title': 'django 5.0 introduces simplified templates and async support',
            'published_date': datetime.now() - timedelta(hours=5),
            'content': 'Django 5.0 brings major improvements to template rendering and adds full async support for views and middleware, making it faster than ever.',
            'category': 'PROGRAMMING',
            'views': 8921
        },
        {
            'id': 3,
            'title': 'artificial intelligence breakthrough: new model understands context',
            'published_date': datetime.now() - timedelta(days=1),
            'content': 'Researchers have developed an AI model that can understand context better than previous systems, potentially revolutionizing natural language processing applications.',
            'category': 'AI NEWS',
            'views': 34287
        },
        {
            'id': 4,
            'title': 'tech giant announces revolutionary smartphone with holographic display',
            'published_date': datetime.now() - timedelta(days=2),
            'content': 'A major tech company has unveiled a new smartphone featuring a holographic display that projects 3D images without special glasses, pushing the boundaries of mobile technology.',
            'category': 'CONSUMER TECH',
            'views': 56123
        },
        {
            'id': 5,
            'title': 'cybersecurity alert: update your systems immediately',
            'published_date': datetime.now() - timedelta(hours=12),
            'content': 'A critical security vulnerability has been discovered affecting millions of systems worldwide. Users are urged to update their software immediately to patch this exploit.',
            'category': 'SECURITY',
            'views': 78934
        },
    ]
    
    # Breaking news ticker (extra headlines for ticker)
    ticker_headlines = [
        "BREAKING: Major tech acquisition announced today!",
        "WEATHER ALERT: Storm warning issued for coastal regions",
        "SPORTS: Underdog team advances to championship finals",
        "MARKETS: Stock indices reach all-time highs",
        "SCIENCE: New exoplanet discovered in habitable zone",
    ]
    
    context = {
        'headlines': news_headlines,
        'ticker_headlines': ticker_headlines,
        'page_title': 'DAILY NEWS HEADLINES',
        'current_time': datetime.now(),
        'total_articles': len(news_headlines),
    }
    
    return render(request, 'news/headline_ticker.html', context)