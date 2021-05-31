from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    part_of = models.ForeignKey(
        'Place', on_delete=models.CASCADE,
        blank=True, null=True,
        related_name="superunit_of"
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.ForeignKey(
        'Place', on_delete=models.CASCADE,
        related_name="is_place_of_birth"
    )
    death_place = models.ForeignKey(
        'Place', on_delete=models.CASCADE,
        related_name="is_place_of_death"
    )

    def __str__(self):
        return self.name


class MyText(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    author = models.ManyToManyField(Author, blank=True)
    pub_place = models.ForeignKey(
        'Place', on_delete=models.CASCADE,
        related_name="is_publication_place",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
