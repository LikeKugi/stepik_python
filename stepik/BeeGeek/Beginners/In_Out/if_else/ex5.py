s1, s2, s3 = int(input()), int(input()), int(input())

if s1 == s2 == s3:
    print('Равносторонний')
elif s1 == s2 or s1 == s3 or s2 == s3:
    print('Равнобедренный')
else:
    print('Разносторонний')

max_number = max(s1, s2, s3)
min_number = min(s1, s2, s3)
print(s1 if (s1 != max_number and s1 != min_number) else (s2 if (s2 != max_number and s2!=min_number) else s3))