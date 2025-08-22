from pyscript import Element
import time

# Your questions array here

questions = [
    ["1. A train 150 m long passes a man walking at 6 km/hr in 15 seconds. Find the speed of the train.", "42 km/hr", "48 km/hr", "54 km/hr", "60 km/hr", 1],

    
    ["2. A sum of ₹12,500 amounts to ₹15,625 in 3 years at simple interest. What is the rate.", "4%", "6%", "8%", "10%", 2],


    ["3. If cost price of 15 pens = selling price of 12 pens, find the profit %.", "20%", "25%", "30%", "40%", 2],


    ["1. A train 150 m long passes a man walking at 6 km/hr in 15 seconds. Find the speed of the train.", "42 km/hr", "48 km/hr", "54 km/hr", "60 km/hr", 1],

    ["2. A sum of ₹12,500 amounts to ₹15,625 in 3 years at simple interest. What is the rate.", "4%", "6%", "8%", "10%", 2],

    ["3. If cost price of 15 pens = selling price of 12 pens, find the profit %.", "20%", "25%", "30%", "40%", 2],

    ["4. A and B complete a work in 12 days together, while B alone takes 30 days. A alone can do it in:", "15 days", "18 days", "20 days", "25 days", 2],

    ["5. Population increases by 10% in first year and decreases by 10% in second year. Present population is 9900. What was the population 2 years ago?", "10,000", "11,000", "12,000", "10,500", 1],

    ["6. The average of 40 students is 50. When teacher is added, average becomes 51. Teacher’s weight is:", "70 kg", "80 kg", "90 kg", "91 kg", 3],

    ["7. A man sold 2 watches at ₹300 each. On one he gained 20%, on the other he lost 20%. Find net result.", "Gain ₹12", "Loss ₹12", "Gain ₹20", "Loss ₹20", 2],

    ["8. If 5x – 2y = 14 and 3x + y = 17, find x : y.", "2 : 1", "3 : 2", "4 : 1", "5 : 2", 1],

    ["9. A sum becomes ₹2,000 in 2 years and ₹2,400 in 4 years at compound interest. Find rate.", "10%", "20%", "25%", "30%", 2],

    ["10. The LCM of two numbers is 240, HCF is 12. If one number is 48, other is:", "60", "72", "80", "90", 1],

    ["11. All engineers are intelligent. Some intelligent people are not doctors.\nConclusions:\n(i) Some doctors are engineers.\n(ii) Some intelligent people are engineers.", "Only (i) follows", "Only (ii) follows", "Both follow", "None follows", 2],

    ["12. Arrange the words logically: (a) Seed, (b) Fruit, (c) Plant, (d) Tree, (e) Flower.", "a → c → e → d → b", "a → b → c → d → e", "a → d → e → c → b", "a → c → d → e → b", 1],

    ["13. In a code, CAT = 24, DOG = 26. What is BAT = ?", "22", "23", "24", "25", 2],

    ["14. A cube is painted on all 6 faces, then cut into 64 small cubes. How many have exactly 2 faces painted?", "12", "24", "36", "48", 2],

    ["15. A is taller than B, B is taller than C, C is taller than D. Who is second tallest?", "A", "B", "C", "D", 2],

    ["16. If ‘+’ = ×, ‘–’ = ÷, ‘×’ = +, ‘÷’ = –. Find 12 + 6 – 3 ÷ 2 × 5.", "20", "22", "24", "26", 3],

    ["17. A clock shows 4:30. The angle between hour & minute hand is:", "45°", "60°", "75°", "90°", 3],

    ["18. Find odd one out: Apple, Mango, Grapes, Potato, Orange.", "Apple", "Potato", "Mango", "Orange", 2],

    ["19. Jan 1, 2024 was Monday. What day was Jan 1, 2025?", "Tuesday", "Wednesday", "Thursday", "Friday", 1],

    ["20. Some books are pens, all pens are pencils.\nConclusions:\n(i) Some books are pencils.\n(ii) Some pencils are books.", "Only (i) follows", "Only (ii) follows", "Both follow", "Neither follows", 3],

    ["21. His ideas are too ______ to be understood by beginners.", "Simple", "Easy", "Complex", "Ordinary", 3],

    ["22. Correct spelling is:", "Acknowledgement", "Aknowledgement", "Acknoledgement", "Acknowlegement", 1],
    
    ["23. Antonym of \"Reluctant\":", "Hesitant", "Willing", "Afraid", "Unsure", 2],

    ["24. Passive voice: “The engineer designed the machine.”", "The machine designed the engineer.", "The machine was designed by the engineer.", "The machine is designed by the engineer.", "The engineer was designed by the machine.", 2],

    ["25. Rearrange: \"in / India / IT / industry / booming / is.\"", "IT industry is booming in India.", "In India booming IT industry is.", "Booming in India IT industry is.", "India booming IT industry.", 1],

    ["26. Synonym of \"Adverse\":", "Harmful", "Favorable", "Useful", "Supportive", 1],

    ["27. She bought ___ orange from the market.", "a", "an", "the", "none", 2],

    ["28. Spot error:", "He don’t like playing cricket.", "He doesn’t like playing cricket.", "He isn’t like playing cricket.", "He not like playing cricket.", 2],

    ["29. If I ______ you, I would apply for that job.", "Was", "Were", "Am", "Be", 2],

    ["30. One-word substitution: \"One who knows everything.\"", "Scholar", "Omnipotent", "Omniscient", "Intelligent", 3],
]


def run_timed_test():
    TEST_DURATION = 30 * 60
    start_time = time.time()
    output_div = document.querySelector("#textarea")
    output_div.innerHTML = ""
    score = 0
    attempted = 0

    for i, question in enumerate(questions):
        elapsed_time = time.time() - start_time
        remaining_time = TEST_DURATION - elapsed_time
        if remaining_time <= 0:
            output_div.innerHTML += "<p>TIME'S UP! Test completed.</p>"
            break

        minutes_left = int(remaining_time // 60)
        seconds_left = int(remaining_time % 60)
        output_div.innerHTML += f"<p>Time Remaining: {minutes_left:02d}:{seconds_left:02d}</p>"
        output_div.innerHTML += f"<p>Question {i+1}/30:</p>"
        output_div.innerHTML += f"<p>{question[0]}</p>"
        output_div.innerHTML += f"<p>A. {question[1]}</p>"
        output_div.innerHTML += f"<p>B. {question[2]}</p>"
        output_div.innerHTML += f"<p>C. {question[3]}</p>"
        output_div.innerHTML += f"<p>D. {question[4]}</p>"

        # Get user input
        ans = document.querySelector("#answer-input").value.strip().upper()

        if ans == 'SKIP':
            output_div.innerHTML += "<p>Question skipped.</p>"
            continue

        attempted += 1
        if ans in ['A', 'B', 'C', 'D']:
            answer_index = ord(ans) - ord('A') + 1
            if question[5] == answer_index:
                output_div.innerHTML += "<p>Correct!</p>"
                score += 1
            else:
                correct_option = ['A', 'B', 'C', 'D'][question-1]
                output_div.innerHTML += f"<p>Incorrect. The correct answer is {correct_option}</p>"
        else:
            output_div.innerHTML += "<p>Invalid input. Question marked as incorrect.</p>"

    elapsed_time = time.time() - start_time
    minutes_taken = int(elapsed_time // 60)
    seconds_taken = int(elapsed_time % 60)
    output_div.innerHTML += f"<p>Time Taken: {minutes_taken:02d}:{seconds_taken:02d}</p>"
    output_div.innerHTML += f"<p>Questions Attempted: {attempted}/30</p>"
    output_div.innerHTML += f"<p>Correct Answers: {score}</p>"
    output_div.innerHTML += f"<p>Accuracy: {(score/attempted*100):.1f}%</p>"

run_timed_test()
