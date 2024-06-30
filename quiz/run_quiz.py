from questions import quiz


def run_quiz(quiz):	
	"""
	Run the quiz based on the questions provided in the 'quiz' parameter.
	Calculate the score based on user answers and print feedback.
	Print the final score out of the total number of questions in the quiz.
	"""
	score = 0
	for q in quiz:
		print(q["question"])
		for i, choice in enumerate(q["choices"], 1):
			print(f"{i}. {choice}")
		answer = input("Type your answer: ").lower()
		if answer == q["answer"].lower():
			score += 1
			print("Thats correct!")
		else:
			print("Incorrect!")
	print(f"Your score is {score} out of {len(quiz)}")
	if score == len(quiz):
		print("Congratulations!")
	elif score < len(quiz) and score > 0:
		print("Better luck next time!")
	else:
		print("Hmm try again later!")

if __name__ == "__main__":
	run_quiz(quiz)
