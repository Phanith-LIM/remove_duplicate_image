import os
from difPy import dif

search = dif("/Users/limphanith/Documents/Python/pythonProject/image")
locations = search.result.values()
with open('result.txt', 'w') as f:
    f.write('Duplicated files: ' + str(len(locations)) + "\n")
for location in locations:
    print('Location: ' + location['location'].replace('/Users/limphanith/Documents/Python/pythonProject/image/', ''))
    match = location['matches'].values()

    with open('result.txt', 'a') as f:
        f.write('Location: ' + location['location'].replace('/Users/limphanith/Documents/Python/pythonProject/image/', '') + '\n')

    for m in match:
        print("Delete: " + m['location'].replace('/Users/limphanith/Documents/Python/pythonProject/', ''))
        os.remove(m['location'])
        with open('result.txt', 'a') as f:
            f.write('Delete: ' + m['location'].replace('/Users/limphanith/Documents/Python/pythonProject/image/', '') + '\n\n')
        print('\n')
print("Done")
