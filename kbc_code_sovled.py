questions = [
    [
        "In which Italian city can you find the Colosseum?",
        "Venice",
        "Rome",
        "Naples",
        "Milan",
        2,
    ],
    [
        "In the TV show New Girl, which actress plays Jessica Day?",
        "Zooey Deschanel",
        "Kaley Cuoco",
        "Jennifer Aniston",
        "Alyson Hannigan",
        1,
    ],
    [
        "What is the largest canyon in the world?",
        "Verdon Gorge, France",
        "King`s Canyon, Australia",
        "Grand Canyon, USA",
        "Fjaðrárgljúfur Canyon, Iceland",
        3,
    ],
    [
        "How long is the border between the United States and Canada?",
        "3,525 miles",
        "4,525 miles",
        "5,525 miles",
        "6,525 miles",
        3,
    ],
    [
        "What is the largest active volcano in the world?",
        "Mount Etna",
        "Mount Vesuvius",
        "Mouna Loa",
        "Mount Batur",
        3,
    ],
    [
        "In which Italian city can you find the Colosseum?",
        "Venice",
        "Rome",
        "Naples",
        "Milan",
        2,
    ],
    [
        "In the TV show New Girl, which actress plays Jessica Day?",
        "Zooey Deschanel",
        "Kaley Cuoco",
        "Jennifer Aniston",
        "Alyson Hannigan",
        1,
    ],
    [
        "What is the largest canyon in the world?",
        "Verdon Gorge, France",
        "King`s Canyon, Australia",
        "Grand Canyon, USA",
        "Fjaðrárgljúfur Canyon, Iceland",
        3,
    ],
    [
        "How long is the border between the United States and Canada?",
        "3,525 miles",
        "4,525 miles",
        "5,525 miles",
        "6,525 miles",
        3,
    ],
    [
        "What is the largest active volcano in the world?",
        "Mount Etna",
        "Mount Vesuvius",
        "Mouna Loa",
        "Mount Batur",
        3,
    ],
    [
        "In which Italian city can you find the Colosseum?",
        "Venice",
        "Rome",
        "Naples",
        "Milan",
        2,
    ],
    [
        "In the TV show New Girl, which actress plays Jessica Day?",
        "Zooey Deschanel",
        "Kaley Cuoco",
        "Jennifer Aniston",
        "Alyson Hannigan",
        1,
    ],
    [
        "What is the largest canyon in the world?",
        "Verdon Gorge, France",
        "King`s Canyon, Australia",
        "Grand Canyon, USA",
        "Fjaðrárgljúfur Canyon, Iceland",
        3,
    ],
    [
        "How long is the border between the United States and Canada?",
        "3,525 miles",
        "4,525 miles",
        "5,525 miles",
        "6,525 miles",
        3,
    ],
    [
        "What is the largest active volcano in the world?",
        "Mount Etna",
        "Mount Vesuvius",
        "Mouna Loa",
        "Mount Batur",
        3,
    ],
]
money = [
    0,
    1000,
    5000,
    7000,
    9000,
    15000,
    20000,
    30000,
    40000,
    70000,
    100000,
    150000,
    250000,
    3500000,
    5000000,
    10000000,
]
print("Welcome To KBC \n")
q_number = 1
for question in questions:
    print(f"{q_number}. {question[0]} (for {money[q_number]} Rs.)")
    print()
    print(f"A. {question[1]}   B. {question[2]}")
    print(f"C. {question[3]}   D. {question[4]}")
    print()
    print("For Quite type - 'q'")
    ans = input("Enter Your Answar A-D:  ")
    while True:
        if ans not in ["A", "B", "C", "D", "a", "b", "c", "d","q"]:
            ans = input("please Enter Your Answar  between 'A-D' or 'q' - for quite the gaeme:  ")
        else:
            break

    print()
    if ans == "A" or ans == "a":
        ans = 1
    elif ans == "B" or ans == "b":
        ans = 2
    elif ans == "C" or ans == "c":
        ans = 3
    elif ans == "D" or ans == "d":
        ans = 4
    elif ans=='q':
        money=money[(q_number-1)]
        print("Your Win Money is: ",money," Rs.")
        break

    if ans == question[5]:
        print("You are right")
        print()
        q_number += 1

    else:
        print("wrong Answar")
        print("Your Win money is : - ", money[(q_number-1)]," Rs.")
        break

if q_number==16:
    print(f"Congratulation you have successfully complete the game your win money is: - {money[(q_number-1)]} Rs.")