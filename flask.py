#from flask import Flask
from sqlalchemy import create_engine, insert, text
import json

#app = Flask(__name__)
engine = create_engine('sqlite:///scraped_data.db')


""" @app.route("/", methods=["GET"])
def starting_url():
    json_data = flask.request.json
    a_value = json_data["a_key"]
    return "JSON value sent: " + a_value

app.run(host="0.0.0.0", port=8080) """

GIVING_SG = ['Title','DisplayName','Town','Duration','Openings','VolunteerUrl','Suitabilities']

def append_db(json_input):
    PLATFORM, PORTAL = '', ''
    with open(json_input) as json_file:
        data = json.load(json_file)
        entries = data['entries']

    if data['source'] == 'giving-sg':
        PLATFORM, PORTAL = GIVING_SG, '\'GIVING_SG\''

    with engine.connect() as connection:
        for i in entries:
            EVENTNAME = "\'" + i[PLATFORM[0]] + "\'"
            ORGANIZER = "\'" + i[PLATFORM[1]] + "\'"
            EVENTLOCATION = "\'" + i[PLATFORM[2]] + "\'"
            EVENTDATE = "\'" + i[PLATFORM[3]] + "\'"
            VACANCIES = i[PLATFORM[4]]
            SIGNUPLINK = "\'" + i[PLATFORM[5]] + "\'"
            SUITABILITY = "\'" + i[PLATFORM[6]] + "\'"

            COMMAND=f'''INSERT INTO VolunteerOpportunities(Portal, EventName, Organizer, EventLocation, EventDate, Vacancies, SignupLink, Suitability)
                        VALUES({PORTAL},{EVENTNAME},{ORGANIZER},{EVENTLOCATION},{EVENTDATE},{VACANCIES},{SIGNUPLINK},{SUITABILITY})'''

            connection.execute(COMMAND)

append_db('test.json')