def combinations(characters, n ,main_combination=""):
    
    if len(main_combination) == n:
        print(main_combination)
        return
    
    for character in characters:
        combinations(characters, n , main_combination + character)


#example:
characters = ["a", "b", "c"]
n = 2  
combinations(characters, n)