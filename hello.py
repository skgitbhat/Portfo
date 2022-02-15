from flask import Flask, render_template, request
import sm
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('index.html')

@app.route('/<a>')
def others(a):
   return render_template(f'{a}')

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
      data=request.form.to_dict()
      if not data['email']:
         return render_template('reenter.html')
        
      else:
         em=data['email']
         sub=data['subject']
         con=data['message']+f" \n \n from:{em}"
         sm.sender(em,sub,con)
         return render_template('thanks.html')


