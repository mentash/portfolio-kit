from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Profile

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 
                  'core/profile_detail.html', 
                  {'profile': profile}
    )
    