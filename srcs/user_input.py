def user_input():
    print("Subjects Legend: ARITHMANCY = 1, ASTRONOMY = 2, HERBOLOGY = 3, DEFENSE_AGAINST_THE_DARK_ARTS = 4\n"
          ", DIVINATION = 5, MUGGLE_STUDIES = 6, ANCIENT_RUNES = 7, HISTORY_OF_MAGIC = 8, TRANSFIGURATION = 9\n"
          ", POTIONS = 10, CARE_OF_MAGICAL_CREATURES = 11, CHARMS = 12, FLYING = 13")
    while True:
        try:
            val = input("Pick the subject that you want to have an histogram for: ")
            while int(val) < 1 or int(val) > 13:
                val = input("Please pick a valid index ranging from 1 - 13: ")
            break
        except ValueError:
            print("Please input integer only.")
            continue

    return int(val)
