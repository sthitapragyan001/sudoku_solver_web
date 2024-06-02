from flask import Flask,render_template,request
import solver
import copy
app= Flask(__name__)

emgrid=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]  

@app.route('/',methods=['GET','POST']) #home page
def home():
    def chnge(a):
        if a in [4,8]:
            return None
        elif a>8:return a-3
        elif a>4:return a-2
        else:return a-1
        
    grid=copy.deepcopy(emgrid)
    if request.method=="POST":
        for i in range(1,12):
            for j in range(1,12):
                r,c=chnge(i),chnge(j)
                if r!=None and c!=None:
                    key=str(i)+str(j)
                    txt=request.form[key]
                    if txt!='':
                        grid[r][c]=int(txt)
                    else:grid[r][c]=0
        if grid!=copy.deepcopy(emgrid): 
            pre_ans_grid=solver.main(grid)
            if pre_ans_grid=='wrong':
                pre_ans_grid=copy.deepcopy(emgrid)
                return render_template("homepage.html",ans_grid='wrong')

        else:pre_ans_grid=copy.deepcopy(emgrid)
    else:
        grid=copy.deepcopy(emgrid)
        pre_ans_grid=grid
    ans_grid={}
    for i in range(1,12):
        for j in range(1,12):
            r,c=chnge(i),chnge(j)
            if r!=None and c!=None:
                t=pre_ans_grid[r][c]
                if t==0: t=''
                ans_grid[(i,j)]= str(t)
            else:
                ans_grid[(i,j)]=''
    return render_template("homepage.html",ans_grid=ans_grid)
if __name__ == "__main__":
    app.run(debug=False)
