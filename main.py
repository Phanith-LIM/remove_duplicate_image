import os
from difPy import dif

search = dif("/image")
locations = search.result.values()
with open('result.txt', 'w') as f:
    f.write('Duplicated files: ' + str(len(locations)) + "\n")
for location in locations:
    print('Location: ' + location['location'].replace('/image/', ''))
    match = location['matches'].values()

    with open('result.txt', 'a') as f:
        f.write('Location: ' + location['location'].replace('/image/', '') + '\n')

    for m in match:
        print("Delete: " + m['location'].replace('/', ''))
        os.remove(m['location'])
        with open('result.txt', 'a') as f:
            f.write('Delete: ' + m['location'].replace('/image/', '') + '\n\n')
        print('\n')
print("Done")
