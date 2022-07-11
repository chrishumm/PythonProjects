from urllib.request import urlopen
import urllib
import json

try:
            question_data = []
            url = "https://opentdb.com/api.php?type=boolean&encode=url3986&category=18&amount=15"
            page_open = urlopen(url)
            html_read = page_open.read()
            decodedPage = html_read.decode("utf-8")

            jsonDict = json.loads(decodedPage)

            for i in jsonDict["results"]:
                temp_dict = {
                    "question": urllib.parse.unquote(i["question"]), # replace the %s 
                    "correct_answer": urllib.parse.unquote(i["correct_answer"])
                }
                question_data.append(temp_dict)

except:
            question_data = [
                {"text": "A slug's blood is green.", "answer": "True"},
                {"text": "The loudest animal is the African Elephant.", "answer": "False"},
                {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
                {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
                {
                    "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it "
                            "home to eat.",
                    "answer": "True"},
                {
                    "text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
                    "answer": "False"},
                {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
                {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
                {"text": "Google was originally called 'Backrub'.", "answer": "True"},
                {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
                {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
                {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
            ]