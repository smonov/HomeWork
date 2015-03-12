#Week1 task 3.4 "A.I."

a = input("Tell me something: ")

if "Hello" in a or "hello" in a:
	print("Hello there, good stranger!")
elif "how are you" in a or "How are you" in a:
	print("I am fine, thanks. How are you?")
elif "feel" in a or "Feel" in a:
	print("I am a machine. I have no feelings")
elif "Age" in a or "age" in a or "old" in a or "Old" in a:
	print("I have no age. Only current timestamps")
else:
	print("I can't understand your question. In General 42 is the answer of everything, otherwise check your spelling and try again.")  
	
