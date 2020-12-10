from django.core.management.base import BaseCommand
from somal.training.train import train_models


class Command(BaseCommand):
    def __init__(self):
        self.help = 'Trains the model.'

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str)

    def handle(self, *args, **options):
        task = options['model']
        if task == 'train':
            print('Training service learning models...')
            train_models()
            print('Done!')

        else:
            print(f"Invalid value for this field: {task}", 'error')
            exit(1)
