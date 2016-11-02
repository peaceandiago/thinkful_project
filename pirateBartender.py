import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    "mixed": "Ya'll want some-some into one?",
    "cloudy": "Want to be weirded out by the drink?",
    "sickly": "Do ya want to get rid of that cold?",
    "magic": "Want something special?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    "mixed": ["slice of orange", "dash of cassis", "cherry on top","shake of bitters", "splash of tonic", "twist of lemon peel"],
    "cloudy": ["dash of baking powder", "sea salt", "fire rum"],
    "sickly": ["lemon drops", "ginger", "hot water", "cloves of garlic"],
    "magic": ["fairy dust", "widow's tears", "sun-dropped petal"]
}

#print ("What will you be having?")

def askQuestions():
    customerPreference = {}
    print ("What will you be having?")  #why doesn't this automatically pop up? #how do you check when it just processes it ?
    
    for customerDrink in questions: 
        # print (customerDrink)
        # print(questions[customerDrink])
        answer = input(questions[customerDrink]) 
        if answer in ["y", "Y", "yes", "Yes"]:
            customerPreference[customerDrink] = True 
        else:
            customerPreference[customerDrink] = False 
    print (customerPreference)
    return customerPreference #returns dictionary and assigns dict to another variable

def makeDrink(preference):
    
    for drink in ingredients:
        if preference[drink] == True:
            cocktail = random.choice(ingredients[drink])
            print (cocktail)
            

newPreference = askQuestions()
makeDrink(newPreference)
    

    
    
    