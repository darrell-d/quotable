from django.test import TestCase
from quote.models import Quote

class QuoteTestCase(TestCase):
    def setUp(self):
        Quote.objects.create(
            quote="To be or not to be, that is the question",
            body="",
            source="William Shakespeare",
        )
        Quote.objects.create(
            quote="Be thine own palace, or the world's thy jail.",
            body="",
            source="John Donne",
        )
        
        Quote.objects.create(
            quote="Wise men speak because they have something to say; Fools because they have to say something.",
            body="",
            source="",
        )

    def test_quote_content(self):
        """Quote returns correct content"""
        shakespeare = Quote.objects.get(source="William Shakespeare")
        donne = Quote.objects.get(source="John Donne")

        self.assertEqual(shakespeare.quote, "To be or not to be, that is the question")
        self.assertEqual(donne.quote, "Be thine own palace, or the world's thy jail.")

    def test_quote_str(self):
        anonymous_quote = Quote.objects.get(quote="Wise men speak because they have something to say; Fools because they have to say something.")
        donne = Quote.objects.get(source="John Donne")
        
        self.assertTrue("Someone said:" in anonymous_quote.__str__())
        self.assertTrue("John Donne said:" in donne.__str__())