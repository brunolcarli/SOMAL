import graphene
from guesser.util import load_model


CLASSIFIER = load_model('somal/training/bk_model')
BLACK_CLF = load_model('somal/training/black_model')

class Query:
    guess = graphene.String(
        text=graphene.String(
            required=True,
            description='Input text to classify.'
        ),
        description='Classifies a text author between Kamal and Beelzebruno.'
    )
    def resolve_guess(self, info, **kwargs):
        text = kwargs.get('text')
        return CLASSIFIER.predict([text])[0]

    guess_black = graphene.String(
        text=graphene.String(
            required=True,
            description='Input text to classify.'
        ),
        description='Guess if a text is from the username $Black'
    )

    def resolve_guess_black(self, info, **kwargs):
        """
        $Black is a very boring user we dont want in our server,
        so this classifier predicts the user text with $Black pattern.
        """
        text = kwargs.get('text')
        return BLACK_CLF.predict([text])[0]
