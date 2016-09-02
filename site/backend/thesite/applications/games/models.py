class Game(models.model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=750)
