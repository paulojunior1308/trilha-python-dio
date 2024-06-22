linguagens = ["python", "js", "c", "java", "c#"]

print(sorted(linguagens, key = lambda x: len(x))) # ['c', 'js', 'c#', 'java', 'python']

print(sorted(linguagens, key = lambda x: len(x), reverse = True)) # ['python', 'java', 'js', 'c#', 'c']