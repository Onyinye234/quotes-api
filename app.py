from flask import Flask, render_template, request,jsonify
import json
import os

app = Flask(__name__)

def readquotes():
  if not os.path.exists('quotes.json'):
        # Create an empty list and write it to the file
        with open('quotes.json', 'w') as f:
            json.dump([], f)
        return []
  with open ('quotes.json') as f:
   return json.load(f)
  
def writequotes(quotes):
    with open ('quotes.json','wt') as f:
        return json.dump(quotes, f, indent= 2)


@app.route('/quotes', methods= ['GET', 'POST'])
def quote():
  quotes = readquotes()
  if request.method =='GET':

    return jsonify(quotes), 200

  else: 
     data = request.get_json()
     new_id = max([q['id'] for q in quotes] ,default=0) + 1
     new ={
        "id" : new_id,
        "quote" : data.get('quote'),
        "author": data.get("author")

     }
     quotes.append(new)
     writequotes(quotes)
     return jsonify(new), 201
  

@app.route('/quotes/<int:id>', methods=['DELETE'])
def delete (id):
   quotes = readquotes()
   for q in quotes:
      if q['id'] == id:
         quotes.remove(q)
         writequotes(quotes)
         return jsonify({"message":f"Quote with id {id} deleted"}), 200
        
   else:
      return jsonify({"error":"Quote not found"})  , 404 
     

if __name__ =="__main__":
    app.run() 
