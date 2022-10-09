from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=500)
    body = models.TextField(blank=True,null=True, default="")
    source = models.CharField(max_length=128, default="anonymous")
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.source in 'anonymous':
            _str = 'Someone said: "{}"'.format(self.quote)
        else:
            _str = '{} said: "{}"'.format(self.source, self.quote)

        return _str

    def get_rand(daily=False):
        import time, random
        from django.db.models import Min, Max
        from django.core.exceptions import ObjectDoesNotExist
        t = time.time()

        if daily:
            seed = int(t / 100000) * 100000
            random.seed(seed)
        else:
            random.seed(t)

        quotes = Quote.objects.all()
        if quotes.exists():
            
            max_id = quotes.aggregate(max_id=Max("id"))['max_id']
            min_id = quotes.aggregate(max_id=Min("id"))['max_id']
            pk = random.randint(min_id, max_id)
            try:
                quote = Quote.objects.get(pk=pk)
            except ObjectDoesNotExist as e:
                # Another way to do random
                quote = Quote.objects.order_by("?").first()
        else:
            quote = {
                'quote': 'The beauty of quotes is that they allow us to glimpse into another minds and understand how they think and look at the world',
                'body': 'This is the default quote. Go to the admin panel to start adding your own',
                'source': 'Joseph Geran III',
            }

        return quote