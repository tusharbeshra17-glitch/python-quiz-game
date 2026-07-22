import random

question =[ ["who is the precident of India","narendra modi","dropodi murmu","amit saha","nitish kumar",2],
["what is the capital of India","new delhi","odisha","kerala","manipur",1],
["what is the length of chickens neck of india","10 km","20 km","30 km","40 km",2],
["what is responible for Indias internal security","RAW","NIA","IB","MI",3],
["who is the CM of odisha","mohan majhi","biju patnaik","nabin patnaik","nitish kumar",1],
["who is the PM of India","narendra modi","dropodi murmu","amit saha","nitish kumar",1] ,
["who is the finance minister of India","narendra modi","dropodi murmu","amit saha","nirmala sitraman",4],
["who is srk","PM","plumber","actor","WWE wrestler",3],
["Who is known as the Father of the Nation of India?", "Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Bhagat Singh", 1],
["What is the national animal of India?", "Lion", "Tiger", "Elephant", "Leopard", 2],
["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
["How many states are there in India?", "28", "29", "30", "27", 1],
["Which is the largest ocean in the world?", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean", 3],
["Who invented the Python programming language?", "Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup", 3],
["Which language is primarily used for Android app development?", "Python", "Java", "C", "PHP", 2],
["Which data type stores True or False values in Python?", "int", "str", "bool", "float", 3],
["What does CPU stand for?", "Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Computer Program Unit", 1],
["What does RAM stand for?", "Random Access Memory", "Read Access Memory", "Random Active Memory", "Read Active Memory", 1],
["Which is the largest continent?", "Europe", "Africa", "Asia", "North America", 3],
["Who wrote the Indian National Anthem?", "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Subhas Chandra Bose", 1],
["What is the national flower of India?", "Rose", "Sunflower", "Lotus", "Jasmine", 3],
["Which is the longest river in India?", "Godavari", "Yamuna", "Ganga", "Brahmaputra", 3],
["What is the capital of Odisha?", "Cuttack", "Bhubaneswar", "Puri", "Sambalpur", 2],
["Which company developed Windows?", "Google", "Microsoft", "Apple", "IBM", 2],
["What is the full form of HTML?", "Hyper Text Markup Language", "High Text Markup Language", "Hyper Transfer Markup Language", "Home Tool Markup Language", 1],
["What is the full form of HTTP?", "Hyper Text Transfer Protocol", "High Text Transfer Protocol", "Hyper Transfer Text Protocol", "Hyper Tool Transfer Protocol", 1],
["Which symbol is used to start a comment in Python?", "//", "#", "/*", "--", 2],
["Which operator is used for exponentiation in Python?", "^", "**", "%", "//", 2],]

random.shuffle(question)

prize_money = [1000,2000,3000,4000,5000,6000,7000,8000,
               9000,10000,11000,12000,13000,14000,
               15000,16000,17000,18000,19000,20000,
               21000,22000,23000,24000,25000,26000,
               27000,28000]

i=0
sum=0
for questions in question :
    print("="*40)
    print(questions[0])
    print("="*40)
    print("OPTIONS")
    print("="*40)
    print(f"1.{questions[1]}")
    print(f"2.{questions[2]}")
    print(f"3.{questions[3]}")
    print(f"4.{questions[4]}")
    print("="*40)
    answer=int(input("enter answer :"))
    if answer == questions[5] :
        print(f"{answer} is correct")

    else:
        print("wrong answer")
        print("Better luck next time...")
        break

    sum+=prize_money[i]
    print(f"you won  {prize_money[i]}")
    print(f"you won total {sum}")
    i+=1
