# Is Number Positive?
def is_positive(number):
    return number > 0
def test_positive_number():
    assert is_positive(5) == True
def test_positive_number():
    assert is_positive(12) == True
def test_positive_number():
    assert is_positive(154.23) == True
def test_negative_number():
    assert is_positive(-1) == False
def test_negative_number():
    assert is_positive(-3) == False
def test_negative_number():
    assert is_positive(-100.5) == False
def test_zero():
    assert is_positive(0) == False

# Check Age Group
def get_age_group(age):
    if age < 18:
        return "Child"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
def test_child_age():
    assert get_age_group(10) == "Child"
def test_child_age():
    assert get_age_group(5) == "Child"
def test_adult_age():
    assert get_age_group(30) == "Adult"
def test_adult_age():
    assert get_age_group(45) == "Adult"
def test_senior_age():
    assert get_age_group(70) == "Senior"
def test_senior_age():
    assert get_age_group(80) == "Senior"

# Grade Pass/Fail
def is_passing(score):
    return score >= 60
def test_passing_score():
    assert is_passing(85) == True
def test_passing_score():
    assert is_passing(60) == True
def test_failing_score():
    assert is_passing(45) == False
def test_failing_score():
    assert is_passing(59) == False

# Traffic Light
def traffic_action(color):
    if color == "red":
        return "Stop"
    elif color == "yellow":
        return "Slow Down"
    elif color == "green":
        return "Go"
    else:
        return "Invalid"
def test_red_light():
    assert traffic_action("red") == "Stop"
def test_yellow_light():
    assert traffic_action("yellow") == "Slow Down"
def test_green_light():
    assert traffic_action("green") == "Go"

# Even or Odd
def is_even(number):
    return number % 2 == 0
def test_even_number():
    assert is_even(4) == True
def test_even_number():
    assert is_even(0) == True
def test_odd_number():
    assert is_even(9) == False
def test_odd_number():
    assert is_even(7) == False

# Temperature Check
def temperature_status(temp):
    if temp < 0:
        return "Freezing"
    elif temp < 20:
        return "Cold"
    elif temp < 30:
        return "Warm"
    else:
        return "Hot"
def test_freezing_temp():
    assert temperature_status(-5) == "Freezing"
def test_freezing_temp():
    assert temperature_status(-10) == "Freezing"
def test_cold_temp():
    assert temperature_status(10) == "Cold"
def test_cold_temp():
    assert temperature_status(15) == "Cold"
def test_warm_temp():
    assert temperature_status(25) == "Warm"
def test_warm_temp():
    assert temperature_status(29) == "Warm"
def test_hot_temp():
    assert temperature_status(30) == "Hot"
def test_hot_temp():
    assert temperature_status(40) == "Hot"

# Simple Calculator Addition
def add_numbers(a, b):
    return a + b
def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5
def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5
def test_add_mixed_numbers():
    assert add_numbers(-2, 3) == 1

# String Length Check
def is_long_string(text):
    return len(text) > 5
def test_long_string():
    assert is_long_string("Hello World") == True
def test_long_string():
    assert is_long_string("Python Project") == True
def test_short_string():
    assert is_long_string("Hi") == False
def test_short_string():
    assert is_long_string("Test") == False

# Number Comparison
def compare_numbers(a, b):
    if a > b:
        return "Greater"
    elif a < b:
        return "Less"
    else:
        return "Equal"
def test_greater_number():
    assert compare_numbers(10, 5) == "Greater"
def test_greater_numbers():
    assert compare_numbers(20, 15) == "Greater"
def test_less_number():
    assert compare_numbers(3, 7) == "Less"
def test_less_number():
    assert compare_numbers(0, 1) == "Less"
def test_equal_number():
    assert compare_numbers(7, 7) == "Equal"
def test_equal_number():
    assert compare_numbers(0, 0) == "Equal"

# Simple Discount
def apply_discount(price, has_coupon):
    if has_coupon:
        return price * 0.9
    else:
        return price
def test_with_coupon():
    assert apply_discount(100, True) == 90
def test_with_coupon():
    assert apply_discount(200, True) == 180
def test_without_coupon():
    assert apply_discount(100, False) == 100
def test_without_coupon():
    assert apply_discount(200, False) == 200
