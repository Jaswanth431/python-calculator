from tkinter import *
root = Tk()
root.title("Calculator")
root.iconbitmap('favicon.ico')

#input feild
input = Entry(root, width=50, borderwidth=5)
input.grid(row=0,column=0, columnspan=4, pady=10, ipady=7)

stack = []

def get_priority(e):
		if(e == "+" or e == "-"):
			return 0
		elif(e == "%" or e == "*" or e == "/" ):
			return 1
			
def peek():
	return stack[len(stack)-1]

def parathesis_checker(infix):
	checker = []
	for i in infix:
		if(i=="("):
			checker.append("(")
		elif(i==")"):
			try:
				if(checker[len(checker)-1] == "("):
					checker.pop()
			except:
				return 0
	if(len(checker) == 0):
		return 1;
	else:
		return 0

def infix_to_postfix(infix):
	stack.append("(")
	infix+=")"
	postfix = ""
	temp = ""
	i=0
	while(i<len(infix)):
		if(infix[i].isdigit() or infix[i].isalpha() or infix[i]==")" or infix[i]=="(" or infix[i] == "+" or infix[i] == "-"  or infix[i] == "*" or infix[i] == "/" ):
			while(infix[i].isdigit()):
				temp+=infix[i]
				i+=1
			if(infix[i]==")" or infix[i]=="(" or infix[i] == "+" or infix[i] == "-"  or infix[i] == "*" or infix[i] == "/"):
				postfix+=temp
				if(temp!=""):
					postfix+="?"
				temp=""

		if(infix[i] == "+" or infix[i] == "-" or infix[i] == "%" or infix[i] == "*" or infix[i] == "/" ):
			while(len(stack) and peek() !="(" and get_priority(peek()) >= get_priority(infix[i])):
				postfix+=stack.pop()
			stack.append(infix[i])
			i+=1

		elif(infix[i] == "("):
			stack.append(infix[i])
			i+=1
		
		elif(infix[i] == ")"):
			while(peek()!="(" and len(stack)):
				postfix+=stack.pop()
			if(len(stack) == 0):
				return "Error"
			if(peek() == "("):
				stack.pop()
			i+=1
		
		else:
			return "Error"
	return postfix

def postfix_evaluation(postfix):
		operand_stack = []
		i=0
		temp = ""
		if(postfix =="Error"):
			return "Error"
		while(i<len(postfix)):
		
			if(postfix[i].isdigit()):
				while(postfix[i] != "?"):
					temp +=postfix[i]
					i+=1
				if(postfix[i] == "?"):
					i+=1
				# print(operand_stack)
				# print(temp)
				operand_stack.append(temp)
				temp=""
			elif(postfix[i] == "+" or postfix[i] == "-" or postfix[i] == "*" or postfix[i] == "/"):
				try:
					var1 = operand_stack.pop()
					var2 = operand_stack.pop()
				except:
					return "Error"
				if(postfix[i] == "+"):
					operand_stack.append(float(var2)+float(var1))
				elif(postfix[i] == "-"):
					operand_stack.append(float(var2)-float(var1))
				elif(postfix[i] == "*"):
					operand_stack.append(float(var2)*float(var1))
				elif(postfix[i] == "/"):
					operand_stack.append(float(var2)/float(var1))
				i+=1
		try:
			return operand_stack.pop()
		except:
			return "Error"

def button_click(val):
	pre_data = input.get()
	pre_data+=val
	input.delete(0,END)
	input.insert(0,pre_data)

def clear():
	input.delete(0,END)
	stack = ["("]

def equal():
	if(parathesis_checker(input.get())):
			postfix = infix_to_postfix(input.get())
			if(postfix!="Error"):
				postfix = postfix_evaluation(postfix)
	else:
		postfix = "Error"

	input.delete(0,END)
	input.insert(0,postfix)

#buttons
but_1 = Button(root,text="1",width=10,pady=5, command=lambda: button_click("1"))
but_1.grid(row=1,column = 0)

but_2 = Button(root,text="2",width=10,pady=5, command=lambda: button_click("2"))
but_2.grid(row=1,column = 1)

but_3 = Button(root,text="3",width=10,pady=5, command=lambda: button_click("3"))
but_3.grid(row=1,column = 2)

but_4 = Button(root,text="4",width=10,pady=5, command=lambda: button_click("4"))
but_4.grid(row=2,column = 0)

but_5 = Button(root,text="5",width=10,pady=5, command=lambda: button_click("5"))
but_5.grid(row=2,column = 1)

but_6 = Button(root,text="6",width=10,pady=5, command=lambda: button_click("6"))
but_6.grid(row=2,column = 2)

but_7 = Button(root,text="7",width=10,pady=5, command=lambda: button_click("7"))
but_7.grid(row=3,column = 0)

but_8= Button(root,text="8",width=10,pady=5, command=lambda: button_click("8"))
but_8.grid(row=3,column = 1)

but_9 = Button(root,text="9",width=10,pady=5, command=lambda: button_click("9"))
but_9.grid(row=3,column = 2)

but_0 = Button(root,text="0",width=10,pady=5, command=lambda: button_click("0"))
but_0.grid(row=4,column = 1)

but_c = Button(root,text="C",width=10,pady=5, command=clear)
but_c.grid(row=4,column = 0)

but_eq = Button(root,text="=",width=10,pady=5, command=equal)
but_eq.grid(row=4,column = 2)

but_plus = Button(root,text="+",width=10,pady=5, command=lambda: button_click("+"))
but_plus.grid(row=1,column = 3)

but_minus = Button(root,text="-",width=10,pady=5, command=lambda: button_click("-"))
but_minus.grid(row=2,column = 3)

but_into = Button(root,text="*",width=10,pady=5, command=lambda: button_click("*"))
but_into.grid(row=3,column = 3)

but_divide = Button(root,text="/",width=10,pady=5, command=lambda: button_click("/"))
but_divide.grid(row=4,column = 3)


root.mainloop()




