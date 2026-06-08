from django.shortcuts import render, get_object_or_404
from .models import Profile

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    return render(request, 
                  'core/profile_detail.html', 
                  {'profile': profile}
    )
    