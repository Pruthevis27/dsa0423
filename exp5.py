import numpy as np

# 4x4 matrix (4 students, 4 subjects)
# Order: Math, Science, English, History

student_scores = np.array([
    [85, 78, 90, 88],
    [75, 80, 85, 82],
    [92, 88, 91, 86],
    [70, 75, 80, 79]
])

# Calculate average for each subject (column-wise)
subject_average = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

# Find subject with highest average
highest_index = np.argmax(subject_average)
highest_subject = subjects[highest_index]

print("Average score for each subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_average[i])

print("\nSubject with highest average score:", highest_subject)