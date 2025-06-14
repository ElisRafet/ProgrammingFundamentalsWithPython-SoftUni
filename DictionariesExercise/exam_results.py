points = {}
submissions = {}
while True:
    result = input().split('-')
    if len(result) == 1:
        break
    elif len(result) == 2:
        banned_name = result[0]
        del points[banned_name]
    else:
        name, lang, upoints = result[0], result[1], int(result[2])
        if name not in points:
            points[name] = 0
        if points[name] < upoints:
            points[name] = upoints
        if lang not in submissions:
            submissions[lang] = 0
        submissions[lang] += 1

print('Results:')
for key, value in points.items():
    print(f'{key} | {value}')
print('Submissions:')
for key,value in submissions.items():
    print(f'{key} - {value}')



