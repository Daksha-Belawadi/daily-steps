def check_step_goal(name, steps, goal=10000):
    if steps >= goal:
        return f"{name}, congratulations! You have met your daily step goal."
    else:
        remaining = goal - steps
        return f"{name}, you need {remaining} more steps to reach your daily goal."


if __name__ == "__main__":
    name = input("Enter your name: ")
    steps = int(input("Enter today's step count: "))
    print(check_step_goal(name, steps))
