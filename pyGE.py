import requests


class GE:

    def __init__(self, party, user, password):
        self.BASEURL = 'https://www.geekevents.org'
        self.party = party
        self.user = user
        self.password = password

    def get(self, endpoint):
        url = '{}/{}/{}/'.format(
            self.BASEURL,
            self.party,
            endpoint
        )
        resp = requests.get(url, auth=(self.user, self.password))
        return resp.json()

    def get_crew(self):
        return self.get('crew/api/crew-list')
