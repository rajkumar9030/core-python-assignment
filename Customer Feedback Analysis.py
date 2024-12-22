def positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    return (positive_count / len(ratings)) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive_percentage = positive_feedback_percentage(ratings)

print(f"Positive Feedback: {positive_percentage}%")
