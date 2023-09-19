import random

# Alarm systems

print("\tAlarm Systems")


class AlarmSystem:
    def __init__(self, is_open, is_people_inside, is_vacation):
        self.is_open = is_open
        self.is_people_inside = is_people_inside
        self.is_vacation = is_vacation
        self.is_activated = False

    def activate_alarm(self):
        assert not self.is_open, "Alarm cannot be activated when the doors are open."
        if self.is_people_inside:
            assert not self.is_vacation, "Alarm cannot be activated during vacation."
            self.is_activated = True
        else:
            self.is_activated = False

    def deactivate_alarm(self):
        self.is_activated = False


# Example usage:
alarm = AlarmSystem(is_open=False, is_people_inside=False, is_vacation=False)

# Try to activate the alarm under different conditions
try:
    alarm.activate_alarm()
    print("Alarm activated:", alarm.is_activated)
except AssertionError as e:
    print("Error:", e)

alarm.is_open = True  # Simulate open doors
try:
    alarm.activate_alarm()
    print("Alarm activated:", alarm.is_activated)
except AssertionError as e:
    print("Error:", e)

alarm.is_open = False
alarm.is_people_inside = True  # Simulate people inside
try:
    alarm.activate_alarm()
    print("Alarm activated:", alarm.is_activated)
except AssertionError as e:
    print("Error:", e)

alarm.is_vacation = True  # Simulate vacation mode
try:
    alarm.activate_alarm()
    print("Alarm activated:", alarm.is_activated)
except AssertionError as e:
    print("Error:", e)


# Sort Array
print("\tSorted Array")


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return arr


# Test
try:
    arr = [1, 5, 3, 2, 4]
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")
except AssertionError as e:
    print("Error:", e)


# Bits Assert

print("\tBits Assert")


def count_set_bits(number):
    assert isinstance(
        number, int) and number >= 0, "Input must be a positive integer"

# Count the number of bits
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


# Test
try:
    num = 0b10101010101010101010101010101010
    bit_count = count_set_bits(num)
    print(f"Number of bits set in {num}: {bit_count}")
except AssertionError as e:
    print("Error:", e)
