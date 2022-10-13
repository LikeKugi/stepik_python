d = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

print('z' in d[2])

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Social Sciences': 2870}

print(len(recipients))

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Social Sciences': 2870}

print(recipients.get('Math'))