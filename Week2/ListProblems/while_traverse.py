#Week2 Task2_1_file2 while_traverse.py

books = ["Learn You a Haskell", 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]

index = 0		 
end = len(books) - 1

while index <= end:
    print(books[index])
    index += 1
