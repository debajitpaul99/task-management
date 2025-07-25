from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In progress"),
        ("COMPLETED", "Completed")
    )
    assigned_to = models.ManyToManyField(Employee)
    project = models.ForeignKey("Project",on_delete=models.CASCADE,default = 1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskDetails(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low")
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=200)
    priority = models.CharField(max_length=1,choices=PRIORITY_OPTIONS,default=LOW)
    notes = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Details for {self.task.title}"

class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name