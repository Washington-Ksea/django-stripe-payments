import stripe

from django.shortcuts import render
from django.views.generic.base import TemplateView
from config.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['key'] = STRIPE_PUBLISHABLE_KEY

        #print(stripe.Balance.retrieve())

        #CHARGE
        print(stripe.Charge.retrieve('ch_1F58AbGA5wUJhNFUulUxAY28')['id'])
        for charge in stripe.Charge.list(limit= 3):
            print(charge['id'])
        
        #Customer

        #
        return context


def charge(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['stripeToken'])
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )        
        customer = stripe.Customer.create(
            description="Customer for jenny.rosen@example.com",
            source='tok_visa' # obtained with Stripe.js
        )
        print(charge) #charge object json
        print(customer) #customer object json
        return render(request, 'charge.html')
    