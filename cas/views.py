from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from umd_python_cas import UMDCASClient


#hostname and post authentication flask route must be passed in to generate CAS login url
client = UMDCASClient(host_name="http://127.0.0.1:8000/", post_auth_route="/secure")

#default route to load html
def index(request):
    return render(request, "templates/index.html", {"user_id": request.session.get('username')})

def login(request):
    return redirect(client.get_login_cas_url())

def secure(request):
    request.session['username'] = client.validate_ticket(request)
    return redirect(reverse('index'))

def logout(request):
	request.session.clear()
	return redirect(client.get_logout_cas_url())
