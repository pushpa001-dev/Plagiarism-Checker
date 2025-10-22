from django.db import models

class PlagiarismResult(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    similarity = models.FloatField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plagiarism Result ({self.similarity}%) on {self.checked_at.strftime('%Y-%m-%d %H:%M')}"
