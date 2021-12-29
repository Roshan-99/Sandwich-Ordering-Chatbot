Step 1:
Sandwiches offered =
1)Roshan's chicken sandwich
 Ingredients : Chicken, Tomatoes, Onions, Pickles, Cucumber, Avocado
 Bread: None
 Spread: Mayo

2)Tuna sandwich
 Ingredients: Tuna, Tomatoes, Pickles, Cucumber
 Bread: Rye
 Spread: Mustard

3)Cali fresh Steak sandwich
 Ingredients: Steak, Bacon, Avocado, Onions, Lettuce,
 Bread: Multigrain
 Spread: Mozzarella

4)Veggie Heaven sandwich
 Ingredients: Onions, Tomatoes, Pickles, Cucumber, Avocado, Lettuce
 Bread: None
 Spread: None

Bread options= Multigrain, Rye, Wheat, Sourdough
Spread options= Butter, Mayo, Mozzarella, Mustard
Options (add ons)= Cheese, Coke, Toasted, Fries
Exceptions (removables)= Tomatoes, Onions, Pickles, Cucumber, Avocado, Lettuce, Spinach, Carrots

------------------------------------------------------------------------------------------------------------------------
Step 2:
Items treated equal or as synonyms

BREAD: {'Multigrain': ["multigrain bread", "Multi-grain", "multi-grain bread", "multigrain", "multi-grain"],
        'Rye': ["Rye bread", "Rye"],
        'Wheat': ['Whole wheat', 'wheat', 'Wheat'],
        'Sourdough': ['Sourdough bread', 'Sourdough']},

NAMEOFSANDWICH: {
        roshan_Sandwich: [roshan_Sandwich, 'roshan sandwich', 'roshan', 'roshan chicken sandwich'],
        tuna_Sandwich: [tuna_Sandwich],
        cali_sandwich: [cali_sandwich, 'cali sandwich', 'cali fresh sandwich', 'cali fresh steak',
                     'cali steak'],
        veggie_sandwich: [veggie_sandwich, 'veggie sandwich', 'veg sandwich', 'veg heaven','veggie heaven','heaven sandwich']},

SPREAD: {
        'Butter': ['butter', 'buter'],
        'Mayo': ['Mayonaisse', 'Mayo', 'mayonaise', 'mayoniece' ],
        'Mozzarella': ['Mozzarella', 'mozarella', 'mozarela', 'mozzarellaa','mozarrela','mozzarella'],
        'Mustard': ['Mustard']},

OPTIONS: {
        'Cheese': ['Cheese', 'cheese', 'extra cheese', 'chese'],
        'Coke': ['Coke', 'coca cola', 'coca-cola'],
        'Toasted': ['Toasted', 'tosted'],
        'Fries': ['fries', 'french fries', 'Fries']},

EXCEPTIONS: {
        'Tomatoes': ['tomato', 'tomatoes'],
        'Onions': ['Onions', 'onion'],
        'Pickles': ['Pickles', 'pickle'],
        'Cucumber': ['Cucumbers', 'Cucumber'],
        'Avocado': ['Avocado', 'avocados', 'avocadoes', 'Avacado', 'avacadoes', 'avacados'],
        'Lettuce': ['Lettuce', 'leetuce', 'Lettuces'],
        'Spinach': ['Spinach', 'spinaches', 'spinachs'],
        'Carrots': ['Carrots', 'carrot', 'carot', 'carots']}

YES: [YES, 'yes', 'y', 'yeah', 'yep', 'sure','ok'],
NO: [NO, 'no', 'n', 'nope', 'nah']


Words being ignored: Every other word other than the word present in one of the above list
so, ignored = {All words- words the above system}

We can say exception using =
[hold the X, no X, without the X, do not want X, dont want X, don't put X, do not put X, without X, exclude X, exclude the X,
 excluding X, remove X, remove the X, hold on the X, minus X, minus the X]
Where X can be one of the exceptions items

------------------------------------------------------------------------------------------------------------------------
Step 3:
Programming language used : Python

To run the program.
Command: python sandwich.py
This will activate the program, then the user can simply play around based on the prompts given by the sandwich bot

File used:
sandwich.py and data.py

sandwich.py: This file contains the main method. It has the logic structure behind deciding what the user provided as input
and generating the respective response based on the classification. It uses data.py for getting data.

data.py : this file contains data - it has menu, sandwiches, breads, spreads, options, exception and other helpful information
such as the words that are considered same and header information

------------------------------------------------------------------------------------------------------------------------
Step 4:

Example 1:

C:\Users\rosha\Desktop\Assignments\MS\AI\Code\Chatbot> python sandwich.py
Hi! What would you Like to have?
Hey! whats on the menu ?
Here is the menu:
1) Roshan's chicken sandwich which has Chicken ,Tomatoes ,Onions ,Pickles ,Cucumber ,Avocado. The spread included is Mayo.
2) Tuna sandwich which has Tuna ,Tomatoes ,Pickles ,Cucumber. The bread included is Rye. The spread included is Mustard.
3) Cali fresh Steak sandwich which has Steak ,Bacon ,Avocado ,Onions ,Lettuce. The bread included is Multigrain. The spread included is Mozzarella.
4) Veggie Heaven sandwich which has Onions ,Tomatoes ,Pickles ,Cucumber ,Avocado ,Lettuce.
Options =Cheese ,Coke ,Toasted ,Fries
Removables=Tomatoes ,Onions ,Pickles ,Cucumber ,Avocado ,Lettuce ,Spinach ,Carrots

What would you like to have?
I would like a Roshans sandwich with Coke and fries
Bread is missing for Roshan's chicken sandwich. Please Choose among one of the options:
Multigrain ,Rye ,Wheat ,Sourdough
Rye bread please
Roshan's chicken sandwich comes with Mayo as default. Respond yes to agree, no to choose something else
Yeah sure


Order:Name of the sandwich : Roshan's chicken sandwich
Usual ingredients : Chicken ,Tomatoes ,Onions ,Pickles ,Cucumber ,Avocado
Bread : Rye
Spread : Mayo
Option : Coke ,Fries
Exception or Removed : <Empty>

Is this what you ordered?
Yep
Order confirmed, have a great Day


Example 2:

 C:\Users\rosha\Desktop\Assignments\MS\AI\Code\Chatbot> python sandwich.py
Hi! What would you Like to have?
I would like a tuna sandwich without Pickles
Tuna sandwich comes with Rye as default. Respond yes to agree, no to choose something else
No
Please choose one of following:Multigrain ,Rye ,Wheat ,Sourdough
Give me the sourdough bread instead
Tuna sandwich comes with Mustard as default. Respond yes to agree, no to choose something else
Yes


Order:Name of the sandwich : Tuna sandwich
Usual ingredients : Tuna ,Tomatoes ,Pickles ,Cucumber
Bread : Sourdough
Spread : Mustard
Option : <Empty>
Exception or Removed : Pickles

Is this what you ordered?
Yeah thats right
Order confirmed, have a great Day

Example 3:

C:\Users\rosha\Desktop\Assignments\MS\AI\Code\Chatbot> python sandwich.py
Hello! What would you Like to have?
Whats on the menu
Here is the menu:
1) Roshan's chicken sandwich which has Chicken ,Tomatoes ,Onions ,Pickles ,Cucumber ,Avocado. The spread included is Mayo.
2) Tuna sandwich which has Tuna ,Tomatoes ,Pickles ,Cucumber. The bread included is Rye. The spread included is Mustard.
3) Cali fresh Steak sandwich which has Steak ,Bacon ,Avocado ,Onions ,Lettuce. The bread included is Multigrain. The spread included is Mozzarella.
4) Veggie Heaven sandwich which has Onions ,Tomatoes ,Pickles ,Cucumber ,Avocado ,Lettuce.
Bread options=Multigrain ,Rye ,Wheat ,Sourdough
Spread options=Butter ,Mayo ,Mozzarella ,Mustard
Options =Cheese ,Coke ,Toasted ,Fries
Removables=Tomatoes ,Onions ,Pickles ,Cucumber ,Avocado ,Lettuce ,Spinach ,Carrots

What would you like to have?
Cali fresh steak with Rye bread and no Onions
Cali fresh Steak sandwich comes with Mozzarella as default. Respond yes to agree, no to choose something else
yeah


Order:Name of the sandwich : Cali fresh Steak sandwich
Usual ingredients : Steak ,Bacon ,Avocado ,Onions ,Lettuce
Bread : Rye
Spread : Mozzarella
Option : <Empty>
Exception or Removed : Onions

Is this what you ordered?
Yes
Order confirmed, have a great Day

#failure case
Example 4:

C:\Users\rosha\Desktop\Assignments\MS\AI\Code\Chatbot> python sandwich.py
Greetings human! What would you Like to have?
roshans sandwich with rye and butter without tomatoes or pickles. Please remove the lettuce as well


Order:Name of the sandwich : Roshan's chicken sandwich
Usual ingredients : Chicken ,Tomatoes ,Onions ,Pickles ,Cucumber ,Avocado
Bread : Rye
Spread : Butter
Option : <Empty>
Exception or Removed : Tomatoes ,Lettuce

Is this what you ordered?
yes
Order confirmed, have a great Day

Exception row should have been tomatoes,pickles and lettuce. It instead is tomatoes and lettuce because my program checks
for occurrences of keywords such as 'Without X', 'remove the X' and cannot identify 'without X or Y', that is if
multiple elements are present after without or remove or other exception keyword.

------------------------------------------------------------------------------------------------------------------------
Step 5:
Easiest part of the assignment: Easy to map which word belongs to which row/column in the filled out menu.

Hardest Part of the assignment: It was really hard to code quickly while thinking about scalability.
This led me to think a lot about the data structure to use to store the data such that I can modify any changes quickly
without having to propagate everywhere.
A close contender was to identify ways in which the flow of the program can go (user's response) and code in response to that.

Something I learned:  data collection, processing and proper data structure is extremely useful for an efficient chatbot.

