def check_step_goal(name, steps, goal=10000):
    """
    Checks whether the daily step goal is met.
    """
    if steps >= goal:
        return f"{name}, congratulations! You have met your daily step goal."
    else:
        remaining = goal - steps
        return f"{name}, you need {remaining} more steps to reach your daily goal."


def main():
    # Default values for CI/CD and Docker execution
    name = "User"
    steps = 7500
    print(check_step_goal(name, steps))


if __name__ == "__main__":
    main()
