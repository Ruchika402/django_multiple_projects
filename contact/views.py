from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages

def contact_form(request):
    """
    Handle contact form submissions
    GET: Display empty form
    POST: Process form data and show success message
    """
    
    # Initialize context dictionary
    context = {
        'success_message': None,
        'submitted_data': None,
        'form_data': {}
    }
    
    # Check if this is a POST request (form submission)
    if request.method == 'POST':
        # Read form data using request.POST.get()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '')
        rating = request.POST.get('rating', '')
        message = request.POST.get('message', '').strip()
        
        # Store submitted data to display back
        context['form_data'] = {
            'name': name,
            'email': email,
            'subject': subject,
            'rating': rating,
            'message': message,
        }
        
        # Simple validation
        errors = []
        if not name:
            errors.append("Name is required")
        if not email:
            errors.append("Email is required")
        if not message:
            errors.append("Message is required")
        if not rating:
            errors.append("Please select a rating")
            
        if errors:
            # If validation fails, show error messages
            context['success_message'] = f"❌ Please fix the following errors: {', '.join(errors)}"
        else:
            # Process the data (save to database, send email, etc.)
            # For now, we'll just display it back
            
            # In a real application, you might:
            # - Send an email notification
            # - Save to database
            # - Send to external API
            
            print(f"New contact form submission:")
            print(f"  Name: {name}")
            print(f"  Email: {email}")
            print(f"  Subject: {subject}")
            print(f"  Rating: {rating}")
            print(f"  Message: {message}")
            
            # Set success message
            context['success_message'] = f"Thank you {name}! Your feedback has been received. We'll get back to you within 24 hours."
            
            # Store submitted data to display
            context['submitted_data'] = {
                'name': name,
                'email': email,
                'subject': dict(contact_form.SUBJECT_CHOICES).get(subject, subject),
                'rating': rating,
                'message': message,
            }
            
            # Optional: Clear form data after successful submission
            # context['form_data'] = {}  # Uncomment to clear form
    
    # For GET request, just show empty form
    # For POST request (with errors), show form with previously entered data
    
    return render(request, 'contact/contact.html', context)

# Subject choices mapping (for display)
contact_form.SUBJECT_CHOICES = [
    ('general', 'General Inquiry'),
    ('feedback', 'Feedback'),
    ('support', 'Technical Support'),
    ('business', 'Business Partnership'),
]