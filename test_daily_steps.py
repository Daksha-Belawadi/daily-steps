from daily_steps import check_step_goal

def test_goal_met():
    result = check_step_goal("Alex", 12000)
    assert "met your daily step goal" in result

def test_goal_not_met():
    result = check_step_goal("Alex", 5000)
    assert "more steps" in result
