import datetime
from haystack import indexes
from threads.models import Thread


class ThreadIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    subtitle = indexes.CharField(model_attr='subtitle')
    author = indexes.CharField(model_attr='author')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Thread

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(modified__lte=datetime.datetime.now())