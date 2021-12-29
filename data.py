# constants
roshan_Sandwich = "Roshan's chicken sandwich"
tuna_Sandwich = "Tuna sandwich"
cali_sandwich = "Cali fresh Steak sandwich"
veggie_sandwich = "Veggie Heaven sandwich"

NAMEOFSANDWICH = 'Name of the sandwich'
INGREDIENTS = 'Usual ingredients'
BREAD = 'Bread'
SPREAD = 'Spread'
OPTIONS = 'Option'
EXCEPTIONS = 'Exception or Removed'

greetings = ["Hello!", "Hi!", "Nice to meet you!", "Greetings human!"]
menu = [roshan_Sandwich, tuna_Sandwich, cali_sandwich, veggie_sandwich]
header = [INGREDIENTS, BREAD, SPREAD]
fullMenu = {
    roshan_Sandwich: [["Chicken", "Tomatoes", "Onions", "Pickles", "Cucumber", "Avocado"], None, "Mayo"],
    tuna_Sandwich: [["Tuna", "Tomatoes", "Pickles", "Cucumber"], "Rye", "Mustard"],
    cali_sandwich: [["Steak", "Bacon", "Avocado", "Onions", "Lettuce"], "Multigrain", "Mozzarella"],
    veggie_sandwich: [["Onions", "Tomatoes", "Pickles", "Cucumber", "Avocado", "Lettuce"], None, None]}

breadOptions = ["Multigrain", "Rye", "Wheat", "Sourdough"]
spreadOptions = ["Butter", "Mayo", "Mozzarella", "Mustard"]
ingredients = ["Tomatoes", "Onions", "Pickles", "Cucumber", "Avocado", "Lettuce", "Spinach", "Carrots"]
exceptionOptions = ingredients
options = ['Toasted', 'Extra Cheese']

optionsDict = {BREAD: breadOptions, SPREAD: spreadOptions, INGREDIENTS: ingredients, EXCEPTIONS: exceptionOptions,
               OPTIONS: options}

synonyms = {BREAD: {'Multigrain': ["multigrain bread", "Multi-grain", "multi-grain bread", "multigrain", "multi-grain"],
                    'Rye': ["Rye bread", "Rye"],
                    'Wheat': ['Whole wheat', 'wheat', 'Wheat'],
                    'Sourdough': ['Sourdough bread', 'Sourdough']},
            # sandwich
            NAMEOFSANDWICH: {
                roshan_Sandwich: [roshan_Sandwich, 'roshan sandwich', 'roshan', 'roshan chicken sandwich'],
                tuna_Sandwich: [tuna_Sandwich],
                cali_sandwich: [cali_sandwich, 'cali sandwich', 'cali fresh sandwich', 'cali fresh steak',
                                'cali steak'],
                veggie_sandwich: [veggie_sandwich, 'veggie sandwich', 'veg sandwich', 'veg heaven','veggie heaven','heaven sandwich']},
            # spread options
            SPREAD: {
                'Butter': ['butter', 'buter'],
                'Mayo': ['Mayonaisse', 'Mayo', 'mayonaise', 'mayoniece' ],
                'Mozzarella': ['Mozzarella', 'mozarella', 'mozarela', 'mozzarellaa','mozarrela','mozzarella'],
                'Mustard': ['Mustard']},
            # options
            OPTIONS: {
                'Cheese': ['Cheese', 'cheese', 'extra cheese', 'chese'],
                'Coke': ['Coke', 'coca cola', 'coca-cola'],
                'Toasted': ['Toasted', 'tosted'],
                'Fries': ['fries', 'french fries', 'Fries']
            },
            # exceptions
            EXCEPTIONS: {
                'Tomatoes': ['tomato', 'tomatoes'],
                'Onions': ['Onions', 'onion'],
                'Pickles': ['Pickles', 'pickle'],
                'Cucumber': ['Cucumbers', 'Cucumber'],
                'Avocado': ['Avocado', 'avocados', 'avocadoes', 'Avacado', 'avacadoes', 'avacados'],
                'Lettuce': ['Lettuce', 'leetuce', 'Lettuces'],
                'Spinach': ['Spinach', 'spinaches', 'spinachs'],
                'Carrots': ['Carrots', 'carrot', 'carot', 'carots']}
            }
exceptionPossibilities = ['hold the', 'no', 'without the', 'do not want', 'dont want', "don't put", "do not put",
                          'without', 'exclude','exclude the', 'excluding', 'remove', 'remove the','hold on the','minus','minus the']
exceptionDict = {}
for key in synonyms[EXCEPTIONS].keys():
    exceptionList = []
    for exception in exceptionPossibilities:
        for word in synonyms[EXCEPTIONS][key]:
            exceptionList.append(exception.strip() + " " + word.strip())
    exceptionDict[key] = exceptionList
synonyms[EXCEPTIONS] = exceptionDict

menuMap = {NAMEOFSANDWICH: menu, INGREDIENTS: "", BREAD: breadOptions, SPREAD: spreadOptions, OPTIONS: options,
           EXCEPTIONS: exceptionOptions}

menuPrompt = ["menu", 'choices', 'choose', 'options', 'items', 'what can i order?', 'order', 'provide', 'have you got',
              'do you have']

ignoreWords = ['Please', 'can', 'i', 'have', 'thanks', 'want', 'like', 'could', 'to']
required = {NAMEOFSANDWICH: True, INGREDIENTS: True, BREAD: True, SPREAD: True, OPTIONS: False,
            EXCEPTIONS: False}
YES = 'Yes'
NO = 'No'
yesOrNo = {YES: [YES, 'yes', 'y', 'yeah', 'yep', 'sure','ok'],
           NO: [NO, 'no', 'n', 'nope', 'nah']}
