from django.shortcuts import render, get_object_or_404
from .models import Profile


# Create home view for home page
def home(request):
    profiles = Profile.objects.all().order_by('name')
    return render(request, 'core/home.html', {'profiles': profiles})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    return render(request, 
                  'core/profile_detail.html', 
                  {'profile': profile}
    )
    