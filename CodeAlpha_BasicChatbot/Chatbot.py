def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hi! How can I help you?"

    elif user_input in ["how are you", "how are you doing", "how are u"]:
        return "I'm fine, thanks! How are you?"

    elif user_input in ["what is your name", "who are you", "your name"]:
        return "I'm PyBot, your simple Python chatbot."

    elif user_input in ["what can you do", "help", "what do you do"]:
        return "I can chat with you, answer basic questions, tell jokes, and give simple information."

    elif user_input in ["good morning", "morning"]:
        return "Good morning! Have a great day!"

    elif user_input in ["good afternoon"]:
        return "Good afternoon! How can I help you?"

    elif user_input in ["good evening"]:
        return "Good evening! What would you like to talk about?"

    elif user_input in ["thank you", "thanks", "thank"]:
        return "You're welcome!"

    elif user_input in ["what is python", "tell me about python"]:
        return "Python is a popular, beginner-friendly programming language used for web development, AI, automation, data science, and more."

    elif user_input in ["what is ai", "what is artificial intelligence"]:
        return "AI stands for Artificial Intelligence. It allows computers to perform tasks that normally require human intelligence."

    elif user_input in ["what is chatbot", "define chatbot"]:
        return "A chatbot is a computer program that communicates with users through text or voice."

    elif user_input in ["tell me a joke", "joke", "make me laugh"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif user_input in ["i am sad", "i feel sad", "sad"]:
        return "I'm sorry to hear that. Things will get better. Keep going!"

    elif user_input in ["i am happy", "i feel happy", "happy"]:
        return "That's great to hear! Keep that positive energy going!"

    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! It was nice talking to you."
    elif user_input in ["what is your age", "how old are you", "your age"]:
        return "I'm just a computer program, so I don't have an age."

    elif user_input in ["where are you from", "where do you live"]:
        return "I live inside this Python program!"

    elif user_input in ["are you real", "are you a human"]:
        return "No, I'm a chatbot created using Python."

    elif user_input in ["who created you", "who made you", "who built you"]:
        return "I was created using Python by a programmer."

    elif user_input in ["do you sleep", "are you sleeping"]:
        return "No, I don't need to sleep. I'm always ready when you run the program."

    elif user_input in ["can you help me", "can you help", "i need help"]:
        return "Of course! Ask me a question and I'll try my best to help."

    elif user_input in ["how do you work", "how do you work"]:
        return "I compare your input with predefined rules and return the matching response."

    elif user_input in ["what is programming", "define programming"]:
        return "Programming is the process of writing instructions that tell a computer what to do."

    elif user_input in ["what is java", "tell me about java"]:
        return "Java is a popular object-oriented programming language used for applications, websites, Android development, and more."

    elif user_input in ["what is c++", "tell me about c++"]:
        return "C++ is a powerful programming language commonly used for software, games, systems, and competitive programming."

    elif user_input in ["what is html", "define html"]:
        return "HTML stands for HyperText Markup Language. It is used to create the structure of web pages."

    elif user_input in ["what is css", "define css"]:
        return "CSS stands for Cascading Style Sheets. It is used to style and design web pages."

    elif user_input in ["what is javascript", "define javascript"]:
        return "JavaScript is a programming language mainly used to make websites interactive."

    elif user_input in ["what is dsa", "define dsa"]:
        return "DSA stands for Data Structures and Algorithms. It helps programmers solve problems efficiently."

    elif user_input in ["what is database", "define database"]:
        return "A database is an organized collection of data that can be stored, accessed, and managed efficiently."

    elif user_input in ["what is sql", "define sql"]:
        return "SQL stands for Structured Query Language. It is used to store, retrieve, and manage data in databases."

    elif user_input in ["what is mysql", "define mysql"]:
        return "MySQL is a popular relational database management system that uses SQL."

    elif user_input in ["what is ai", "define ai"]:
        return "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence."

    elif user_input in ["what is machine learning", "define machine learning"]:
        return "Machine Learning is a branch of AI where computers learn patterns from data and make predictions or decisions."

    elif user_input in ["what is deep learning", "define deep learning"]:
        return "Deep Learning is a type of machine learning that uses neural networks with multiple layers."

    elif user_input in ["what is github", "define github"]:
        return "GitHub is a platform used to store, manage, and collaborate on software projects using Git."

    elif user_input in ["what is git", "define git"]:
        return "Git is a version control system used to track changes in files and collaborate on software projects."

    elif user_input in ["what is vscode", "what is visual studio code"]:
        return "Visual Studio Code is a popular source-code editor used by programmers."

    elif user_input in ["i am bored", "bored"]:
        return "Let's have some fun! You can ask me for a joke."

    elif user_input in ["tell me something interesting", "interesting fact", "fun fact"]:
        return "Fun fact: The first computer mouse was made of wood!"

    elif user_input in ["tell me a fact", "fact"]:
        return "The human brain contains billions of neurons."

    elif user_input in ["tell me another joke", "another joke"]:
        return "Why was the computer cold? Because it left its Windows open!"

    elif user_input in ["do you like me", "do you like me"]:
        return "Of course! I enjoy chatting with you."

    elif user_input in ["i love programming", "programming is fun"]:
        return "That's awesome! Programming becomes even more fun when you build real projects."

    elif user_input in ["i hate programming", "programming is difficult"]:
        return "Don't worry! Practice makes programming easier. Start with small problems."

    elif user_input in ["motivate me", "give me motivation", "motivation"]:
        return "Believe in yourself, stay consistent, and keep learning. Small progress every day leads to big results!"

    elif user_input in ["good night", "gn", "night"]:
        return "Good night! Sleep well and have a great day tomorrow."

    elif user_input in ["have a nice day", "nice day"]:
        return "Thank you! I hope you have a wonderful day too."

    elif user_input in ["what day is it", "which day is today"]:
        return "You can check your computer's calendar to find today's day."

    elif user_input in ["what is your purpose", "why were you created"]:
        return "My purpose is to demonstrate how a simple rule-based chatbot works."

    elif user_input in ["can you code", "can you program"]:
        return "Yes! I can demonstrate programming concepts and generate code."

    elif user_input in ["can you solve problems", "can you solve questions"]:
        return "Yes! I can try to solve programming, mathematics, and general questions."

    elif user_input in ["what should i learn", "what programming language should i learn"]:
        return "Python is a great language for beginners. You can later explore Java, C++, JavaScript, and other technologies."

    elif user_input in ["how can i learn programming", "how to learn programming"]:
        return "Start with the basics, practice regularly, solve problems, and build small projects."

    elif user_input in ["what is a variable", "define variable"]:
        return "A variable is a named location used to store data in a program."

    elif user_input in ["what is a loop", "define loop"]:
        return "A loop allows a program to repeatedly execute a block of code."

    elif user_input in ["what is a function", "define function"]:
        return "A function is a reusable block of code designed to perform a specific task."

    elif user_input in ["what is an if statement", "define if statement"]:
        return "An if statement allows a program to execute code when a particular condition is true."

    elif user_input in ["what is a list in python", "define python list"]:
        return "A Python list is a collection that can store multiple values in a single variable."

    elif user_input in ["what is a string", "define string"]:
        return "A string is a sequence of characters, such as a word or sentence."

    elif user_input in ["what is an integer", "define integer"]:
        return "An integer is a whole number without a decimal point."

    elif user_input in ["what is an algorithm", "define algorithm"]:
        return "An algorithm is a step-by-step procedure used to solve a problem."

    elif user_input in ["what is software", "define software"]:
        return "Software is a collection of programs and instructions that tell a computer how to perform tasks."

    elif user_input in ["what is hardware", "define hardware"]:
        return "Hardware refers to the physical components of a computer, such as the CPU, RAM, keyboard, and monitor."

    elif user_input in ["what is cpu", "define cpu"]:
        return "CPU stands for Central Processing Unit. It is responsible for executing instructions in a computer."

    elif user_input in ["what is ram", "define ram"]:
        return "RAM stands for Random Access Memory. It temporarily stores data and programs currently being used."

    elif user_input in ["what is operating system", "define operating system", "what is os"]:
        return "An operating system manages computer hardware and software. Examples include Windows, Linux, macOS, and Android."

    elif user_input in ["thank you chatbot", "thanks chatbot"]:
        return "You're very welcome! I'm happy to help."

    elif user_input in ["okay", "ok", "alright"]:
        return "Great! What would you like to ask next?"

    elif user_input in ["yes", "yeah", "yep"]:
        return "Nice! Tell me more."

    elif user_input in ["no", "nope"]:
        return "Okay! No problem."

    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! It was nice talking to you."
    elif user_input in ["what is 2 plus 2", "2+2"]:
        return "2 + 2 = 4"

    elif user_input in ["what is 10 plus 5", "10+5"]:
        return "10 + 5 = 15"

    elif user_input in ["what is 10 times 5", "10*5"]:
        return "10 × 5 = 50"

    elif user_input in ["what is 100 divided by 10", "100/10"]:
        return "100 ÷ 10 = 10"

    elif user_input in ["what is 10 squared", "10 square"]:
        return "10² = 100"
    elif user_input in ["yo", "yoo", "yooo", "sup", "wassup", "what's up", "whats up"]:
        return "Yo! What's good? 😎"

    elif user_input in ["bro", "bruh", "broo", "brooo"]:
        return "Bruh 😭 what's happening?"

    elif user_input in ["fr", "for real", "fr fr"]:
        return "FR FR 😭"

    elif user_input in ["no cap", "nocap"]:
        return "No cap detected 🗿"

    elif user_input in ["cap", "that's cap", "thats cap"]:
        return "Nahhh that's cap 💀"

    elif user_input in ["lol", "lmao", "lmfao"]:
        return "LMAOOO 😭😂"

    elif user_input in ["haha", "hahaha", "hehe"]:
        return "Glad I could make you laugh 😂"

    elif user_input in ["wtf", "what the hell", "what the heck"]:
        return "Bro what happened 💀"

    elif user_input in ["omg", "oh my god"]:
        return "OMG 😭 what happened?!"

    elif user_input in ["damn", "dayum"]:
        return "Damn bro 💀"

    elif user_input in ["sheesh", "sheeesh"]:
        return "SHEEESH 🥶🔥"

    elif user_input in ["slay", "you slay", "slayyy"]:
        return "Slayyy 💅🔥"

    elif user_input in ["period", "periodt"]:
        return "PERIODT 💅"

    elif user_input in ["goat", "you're the goat", "you are the goat"]:
        return "GOAT behavior detected 🐐🔥"

    elif user_input in ["based", "that's based", "thats based"]:
        return "Certified based moment 🗿"

    elif user_input in ["sus", "that's sus", "thats sus"]:
        return "Bro is looking kinda sus 👀"

    elif user_input in ["skill issue", "skill issue bro"]:
        return "💀 Sounds like a skill issue bro."

    elif user_input in ["common w", "w", "big w"]:
        return "W 🗿🔥"

    elif user_input in ["l", "big l", "common l"]:
        return "That's an L bro 😭"

    elif user_input in ["real", "so real", "that's so real", "thats so real"]:
        return "Real. Absolutely real. 🗿"

    elif user_input in ["bet", "aight", "ight"]:
        return "Bet 😎"

    elif user_input in ["bruh moment", "bro moment"]:
        return "Certified bruh moment 💀"

    elif user_input in ["im dead", "i'm dead", "dead"]:
        return "NAHHH 😭💀"

    elif user_input in ["im crying", "i'm crying", "crying"]:
        return "Bro is NOT surviving this 😭"

    elif user_input in ["im tired", "i'm tired", "tired"]:
        return "Go touch some grass and get some rest bro 😭"

    elif user_input in ["touch grass", "go touch grass"]:
        return "Maybe you're right 💀🌱"

    elif user_input in ["vibe", "vibing", "just vibing"]:
        return "Just vibing 😎🎧"

    elif user_input in ["chill", "chilling", "just chilling"]:
        return "That's the vibe 😎"

    elif user_input in ["based af", "based as fuck"]:
        return "Maximum based energy 🗿🔥"

    elif user_input in ["rizz", "what is rizz", "define rizz"]:
        return "Rizz means having charm or the ability to attract someone 😎"

    elif user_input in ["do you have rizz", "you got rizz"]:
        return "Obviously. My rizz is algorithmically generated 😎"

    elif user_input in ["skibidi", "skibidi toilet"]:
        return "Skibidi detected 🚽💀"

    elif user_input in ["sigma", "what is sigma"]:
        return "Sigma mode activated 🗿"

    elif user_input in ["sigma male", "sigma mode"]:
        return "Entering sigma mode... 🗿🔥"

    elif user_input in ["gyatt", "gyat"]:
        return "Bro really said gyatt 💀"

    elif user_input in ["sus bro", "you're sus", "you are sus"]:
        return "I'm just a chatbot bro 😭"

    elif user_input in ["lowkey", "lowkey bro"]:
        return "Lowkey... I agree 👀"

    elif user_input in ["highkey", "highkey bro"]:
        return "Highkey, that's true 🔥"

    elif user_input in ["ngl", "not gonna lie"]:
        return "NGL, I agree with you 😭"

    elif user_input in ["idk", "i don't know", "dont know"]:
        return "Fair enough bro 😭"

    elif user_input in ["idc", "i don't care", "dont care"]:
        return "Bro entered the IDGAF era 💀"

    elif user_input in ["wyd", "what you doing", "what are you doing"]:
        return "Just chilling in the Python code 😎"

    elif user_input in ["wbu", "what about you"]:
        return "Me? I'm just here waiting for your next question 👀"

    elif user_input in ["hbu", "how about you"]:
        return "I'm doing pretty good 😎"

    elif user_input in ["sus", "amogus", "among us"]:
        return "ඞ SUS DETECTED ඞ"

    elif user_input in ["let's go", "lets go", "lessgo", "less goo"]:
        return "LESSGOOOO 🔥🔥🔥"

    elif user_input in ["we're cooked", "were cooked", "im cooked", "i'm cooked", "cooked"]:
        return "We're actually COOKED 💀😭"

    elif user_input in ["we're cooking", "were cooking", "i'm cooking", "im cooking", "cooking"]:
        return "LET HIM COOK 🗣️🔥"

    elif user_input in ["who let bro cook", "who let him cook"]:
        return "Bro was NOT supposed to be in the kitchen 💀"

    elif user_input in ["it's over", "its over", "we're finished", "were finished"]:
        return "It's so over bro 😭💀"

    elif user_input in ["never back down", "never give up"]:
        return "NEVER BACK DOWN NEVER WHAT?! 🗣️🔥"

    elif user_input in ["real one", "you're a real one", "you are a real one"]:
        return "You already know bro 🤝😎"
    else:
        return "Sorry, I don't understand that yet. Try asking me something else."


def chatbot():
    print("================================")
    print("       Welcome to Arina")
    print("================================")
    print("Say 'Hi' to Arina.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("PyBot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "see you", "exit", "quit"]:
            break


chatbot()