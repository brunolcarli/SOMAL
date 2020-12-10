import graphene
from guesser.util import load_model


CLASSIFIER = load_model('somal/training/bk_model')

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
