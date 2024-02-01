import numpy as np
student_scores=np.array([
    [90,88,91,92],
    [76,88,80,90],
    [77,88,90,78],
    [78,88,87,89]])
avg=np.mean(student_scores,axis=0)
high=np.argmax(avg)
highest= ['Math', 'Science', 'English', 'History'][high]
print(avg)
print(highest)
