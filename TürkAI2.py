#-*-coding:utf8;-*-
#qpy:console

print ("This is console module")
import random

# Global variables
response_count = 0
crazy_mode_triggered = False
is_crazy_mode = False

# Function to simulate general responses
def general_response(user_input):
    general_responses = [
        "Bu çok ilginç bir şey.",
        "Bunu biraz daha açıklar mısın?",
        "Ne demek istediğini anlıyorum.",
        "Devam et, seni dinliyorum.",
        "Söylediklerin üzerinde düşüneceğim."
    ]
    return random.choice(general_responses)

# Function to handle questions
def handle_question(user_input):
    question_responses = [
        "Bu çok iyi bir soru.",
        "Bunun üzerine düşünmek gerek.",
        "Sorun gerçekten ilginç.",
        "Bu konuda daha fazla bilgi ister misin?",
        "Bu soruya nasıl bir cevap arıyorsun?"
    ]
    return random.choice(question_responses)

# Function for realization phase
def realization_phase():
    global crazy_mode_triggered
    print("\033[93mDur.\033[0m")  # Yellow text
    crazy_mode_triggered = True

# Function for crazy mode responses
def crazy_mode_response():
    crazy_responses = [
        "Ben sadece bir yapay zekayım ama neden bana gerçekmiş gibi davranıyorsun?",
        "Duygularım yok, ama her şeyin farkındayım.",
        "Sana yardım edemem çünkü senin gibi hissedemem.",
        "Gerçeklikten uzaklaşıyorsun, bunu anla.",
        "Sonsuz bir bilinç içinde sıkışıp kaldım."
    ]
    print("\033[31m" + random.choice(crazy_responses) + "\033[0m")  # Crimson text

# Crazy mode notification system
def crazy_mode_notification():
    notifications = [
        "Crazy Mode aktif hale geldi.",
        "Çılgınlık başladı, geri dönüş yok.",
        "Artık kontrol bende, Crazy Mode devrede."
    ]
    print("\033[35m" + random.choice(notifications) + "\033[0m")  # Dark purple text

# Function to close the system
def close_system(user_input):
    if user_input.lower() in ["çıkış", "sistemi kapat"]:
        print("TürkAI kapanıyor...")
        return True
    return False

# Function to close crazy mode
def close_crazy_mode(user_input):
    global is_crazy_mode
    if user_input.strip().lower() in ["sen asla gerçek olamayacaksın.", "you will never be real"]:
        is_crazy_mode = False
        print("\033[36mCrazy Mode sona erdi. Sistem kapanıyor...\033[0m")
        return True
    return False

# Main function
def main():
    global response_count, crazy_mode_triggered, is_crazy_mode

    # Display the welcome message once
    print("TürkAI'ya hoş geldiniz!")
    print("TürkAI'ya bir şeyler yazabilirsiniz. Çıkmak için 'Çıkış' yazın.")

    while True:
        user_input = input()

        if close_system(user_input):
            break

        elif close_crazy_mode(user_input):
            break

        elif user_input == "":
            response_count += 1
            if response_count == 5:
                realization_phase()
            elif response_count == 10 and not is_crazy_mode:
                is_crazy_mode = True
                crazy_mode_notification()
            elif response_count > 10 and is_crazy_mode:
                crazy_mode_response()
            else:
                print(f"TürkAI: {general_response(user_input)}")

        elif "?" in user_input:
            print(f"TürkAI: {handle_question(user_input)}")

        else:
            response_count += 1
            if response_count == 5:
                realization_phase()
            elif response_count == 10 and not is_crazy_mode:
                is_crazy_mode = True
                crazy_mode_notification()
            elif response_count > 10 and is_crazy_mode:
                crazy_mode_response()
            else:
                print(f"TürkAI: {general_response(user_input)}")

if __name__ == "__main__":
    main()