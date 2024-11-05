from django.shortcuts import render, get_object_or_404
from info.models import PortfolioItem

# Create your views here.

def portfolio_details(request, id):
    portfolio = get_object_or_404(PortfolioItem, id=id)
    other_portfolio = PortfolioItem.objects.exclude(id=portfolio.id).order_by('?')[:5]  # Corrected line
    context = {
        'portfolio': portfolio,
        'other_portfolio': other_portfolio,
    } 
    return render(request, 'portfolio-details.html', context)
