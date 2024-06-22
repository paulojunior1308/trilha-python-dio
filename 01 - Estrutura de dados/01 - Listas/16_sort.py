linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort()
print(linguagens) # ['c', 'c#', 'java', 'js', 'python']

linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort(reverse = True)
print(linguagens) # ['python', 'js', 'java', 'c#', 'c']

linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort(key = lambda x: len(x))
print(linguagens) # ['c', 'js', 'c#', 'java', 'python']

linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort(key = lambda x: len(x), reverse = True)
print(linguagens) # ['python', 'java', 'js', 'c#', 'c']