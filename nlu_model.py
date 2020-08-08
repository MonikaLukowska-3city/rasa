from rasa.nlu.model import Interpreter

def run_nlu():
    interpreter = Interpreter.load('./models/nlu-20200808-171227/nlu') ## this should be an extracted model
   
    print("start - provide input text .... /stop exit program") 
    while(True):
        text = str(input("-> ")) 
        if(text == "/stop"):
            break

        result = interpreter.parse(text)
        #print(result)

        print("Bot:\n\nIntent:")
        print("name:{}\tconfidence{}".format(result["intent"]["name"], result["intent"]["confidence"]))

        print("\nEntities:")
        for rec in result["entities"]:
            print("entity: {}\tvalue:{}\textractor:{}\tstart:{}\tend:{}".format(rec["entity"], rec["value"], rec["extractor"], rec["start"], rec["end"]))


        print("\nRanking:")
        index = 1
        for rec in result["intent_ranking"]:
            print("index:{}\tname:{}\tconfidence{}".format(index, rec["name"], rec["confidence"]))
            index = index + 1

    print("exit") 
      

if __name__ == '__main__':
    run_nlu()

 