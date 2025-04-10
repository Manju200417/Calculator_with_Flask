from flask import Flask,request,render_template

app = Flask(__name__)

def cal(op,num1,num2):
    try:
        if op == 'add':
            ans = num1 + num2
        
        elif op == 'sub':
            ans = num1 - num2
        
        elif op == 'mul':
            ans = num1 * num2
        
        elif op == 'div':
            if num2 != 0:
                ans = num1 / num2
            else:
                ans = "Cannot divide by zero!"

        else:
            return 'Invalid input'
    
    except Exception as e:
        return str(e)
       
    return ans

@app.route('/', methods = ['GET','POST'])
def calc():
    ans = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            op = request.form['op']
            ans = cal(op,num1,num2)
        except ValueError:
            ans = "Invalid Input"
    else :
        ans = None
    return render_template('index.html',ans = ans)


if __name__ == '__main__':
    app.run(debug=False)
