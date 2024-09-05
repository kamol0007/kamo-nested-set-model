from django.db import models


# Create your models here.
class NestedModel(models.Model):
    nested_left = models.IntegerField(default=0)
    nested_right = models.IntegerField(default=0)
    nested_row = models.IntegerField(default=0)
    nested_parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE)

    class Meta:
        abstract = True,
        models.Index(fields=['nested_left', 'nested_right']),
        models.Index(fields=['nested_row']),

    def __str__(self):
        return str(self.nested_row)