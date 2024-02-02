import numpy as np
study_hours = np.array([2, 3, 1, 4, 5, 2, 3, 4, 5, 1])
exam_scores = np.array([65, 70, 60, 75, 80, 65, 70, 75, 80, 60])
covariance_study_exam = np.cov(study_hours, exam_scores)[0, 1]
print("Covariance between Study Hours and Exam Scores:", covariance_study_exam)
