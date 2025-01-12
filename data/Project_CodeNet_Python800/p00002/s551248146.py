# coding: utf-8
remaining_questions = True
while remaining_questions:
    try:
        value_a, value_b = map(int, input().split(" "))
        print(len(str(value_a + value_b)))
    except:
        remaining_questions = False