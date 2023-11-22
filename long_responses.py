import random

R_ATING = "I am a bot obviously I can't age!!"
R_DESC = "Alvin Adams is a wonderful being and sweet soul"
R_ADVC= "If you are having difficulties, kindly seek help"
R_KENYA= "Kenya has a president called Zakayo, for more info, you can google more about Kenya"
R_MORINGA = "Moringa school is well-known for its advanced resources that give an outline and foundation of  learning technology"
def unknown():
    response = ["Could you please rephrase that?",
                "What do you mean?",
                "That sounds right",
                "..."][random.randrange(4)]
    return response