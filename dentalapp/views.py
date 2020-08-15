from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			message_name, #subject
			message_email, #from
			message, #message
			['gmarous@hotmail.com'], #to email
			fail_silently=False,
		)

		context = {'message_name': message_name, 'message_email': message_email, 'message': message}
		return render(request, 'contact.html', context)
	else:
		return render(request, 'contact.html', {})

def blog_details(request):
	return render(request, 'blog-details.html', {})