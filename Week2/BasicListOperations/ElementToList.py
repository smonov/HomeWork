#Week2 Task1_2 ElementToList

languages = ["Python", "Ruby"]

languages = languages + ["C++", "Java", "C#"]

languages = ["Haskell"] + languages + ["Go"]

languages[0]

languages[1]

languages[4]

languages[5] = "F#"

a = len(languages) - 1
languages[a]

if "Haskell" in languages:
	print("yes")

if "Ruby" in languages:
	print("yes")
	
if "Go" in languages:
	print("yes")	

if "Rust" in languages:
	print("yes")	
else:
	print("Rust doesn't exist")
	
	


