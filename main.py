
from deepface import DeepFace
from until import *

if __name__ == '__main__':
    test_url = "face-whiteman.png"
    result = Analyze.analyze_emotion(test_url)
    JsonStringOperations.print_formatted_result(result)

