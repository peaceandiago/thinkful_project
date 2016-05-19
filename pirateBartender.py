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

print ("What will you be having?")

def askQuestions():
    customerDrink = {}
    #print ("What will you be having?")  #why doesn't this automatically pop up? #how do you check when it just processes it ?
    
   # for customerDrink in questions:  --doesn't work... but why? -- 
    bartenderQuestion1 = input(questions['strong'])
    if bartenderQuestion1[0] == 'y' or bartenderQuestion1[0] == 'Y':
        customerDrink['strong'] = True
    else:
    	customerDrink['strong'] = False
    	
    bartenderQuestion2 = str(input(questions['salty']))
    if bartenderQuestion2[0] == 'y' or bartenderQuestion2[0] == 'Y':
        customerDrink['salty'] = True
    else:
        customerDrink['salty'] = False
    	
    bartenderQuestion3 = str(input(questions['bitter']))
    if bartenderQuestion3[0] == 'y' or bartenderQuestion3[0] == 'Y':
        customerDrink['bitter'] = True
    else:
        customerDrink['bitter'] = False

    bartenderQuestion4 = str(input(questions['sweet']))
    if bartenderQuestion4[0] == 'y' or bartenderQuestion4[0] == 'Y':
        customerDrink['sweet'] = True
    else:
        customerDrink['sweet'] = False

    bartenderQuestion5 = str(input(questions['fruity']))
    if bartenderQuestion5[0] == 'y' or bartenderQuestion5[0] == 'Y':
        customerDrink['fruity'] = True
    else:
        customerDrink['fruity'] = False
    
    bartenderQuestion6 = str(input(questions['mixed']))
    if bartenderQuestion6[0] == 'y' or bartenderQuestion6[0] == 'Y':
        customerDrink['mixed'] = True
    else:
        customerDrink['mixed'] = False
        
    bartenderQuestion7 = str(input(questions['cloudy']))
    if bartenderQuestion7[0] == 'y' or bartenderQuestion7[0] == 'Y':
        customerDrink['cloudy'] = True
    else:
        customerDrink['cloudy'] = False
    
    bartenderQuestion8 = str(input(questions['sickly']))
    if bartenderQuestion8[0] == 'y' or bartenderQuestion8[0] == 'Y':
        customerDrink['sickly'] = True
    else:
        customerDrink['sickly'] = False 
    
    bartenderQuestion9 = str(input(questions['magic']))
    if bartenderQuestion9[0] == 'y' or bartenderQuestion9[0] == 'Y':
        customerDrink['magic'] = True
    else:
        customerDrink['magic'] = False 


        
def makeDrink(customerDrink): #Assign the ingredient to whatever is TRUE from askQuestions function 
    cocktails = {}
    
    #if customerDrink['strong'] == True:  
     #   print(random.choice(ingredients['strong']))  -- why can't this work??, can I not do this without using Cocktails {}, why do I need to create a new dictionary
     
    if customerDrink['strong'] == True:
        cocktails['strong'] = random.choice(ingredients['strong'])
        
    if customerDrink['salty'] == True:
        cocktails['salty'] = random.choice(ingredients['salty'])
     
    if customerDrink['bitter'] == True:
        cocktails['bitter'] = random.choice(ingredients['bitter'])
        
    if customerDrink['sweet'] == True:
        cocktails['sweet'] = random.choice(ingredients['sweet']) 
    
    if customerDrink['fruity'] == True:
        cocktails['fruity'] = random.choice(ingredients['fruity']) 
        
    if customerDrink['mixed'] == True:
        cocktails['mixed'] = random.choice(ingredients['mixed']) 
    
    if customerDrink['cloudy'] == True:
        cocktails['cloudy'] = random.choice(ingredients['cloudy']) 
        
    if customerDrink['sickly'] == True:
        cocktails['sickly'] = random.choice(ingredients['sickly']) 
        
    if customerDrink['magic'] == True:
        cocktails['magic'] = random.choice(ingredients['magic']) 
        

if __name__ == '__main__':
    
    # makeDrink(askQuestions()) -- literally passing the preferences into making drink
    customerChoice = askQuestions()
    bartenderMakes = makeDrink(customerChoice)
    for order in bartenderMakes:
        print (drink) 
    
    
    