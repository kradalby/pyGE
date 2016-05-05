from pyGE import GE
import pickle

ge = GE(
    party='pp25',
    user='pp25',
    password='SECRET'
)

old = pickle.load(open('crewdump.pickle', 'rb'))
now = ge.get_crew()

for member in now.keys():
    if member not in old.keys():
        print('Name: {} {}'.format(
            now[member]['first_name'],
            now[member]['last_name']
        ))
        print('Crew: {}'.format(now[member]['crew']))
        print('Photo: {})'.format(now[member]['profile_image']))

pickle.dump(now, open('crewdump.pickle', 'wb'))
