from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='menu_name')
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE,
                               blank=True, related_name='children')
    url = models.CharField(max_length=255, unique=True)
    named_url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self):
        reverse_url = self.url
        named_args = {'url': reverse_url}
        self.url = reverse_lazy('index', kwargs=named_args)
        super(MenuItem, self).save()

    def get_parents(self):
        if self.parent:
            return self.parent.get_parents() + [self.parent.id]
        else:
            return []

    def get_children(self):
        return self.children.select_related('parent').all()
