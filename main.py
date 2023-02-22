from flask import Flask
import utils

app = Flask(__name__)

@app.route('/')
def page_index():
     str_candidate = "<pre>"
     candidates = utils.data_candidates()
     for candidate in candidates.values():
         str_candidate += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
     str_candidate += "</pre>"
     return str_candidate

@app.route('/candidates/<int:id>')
def candidates(id):
     candidates = utils.data_candidates()
     candidate = candidates[id]
     str_candidate = f" <img src={candidate['name']} </img> <br><br>{candidate['position']} <br>{candidate['skills']}<br><br>"
     return str_candidate


@app.route('/skill/<skill>')
def skills(skill):
     str_skills = "<pre>"
     candidates = utils.data_candidates()
     for candidate in candidates.values():
         list_skill = candidate['skills'].split(", ")
         list_skill = [x.lower() for x in list_skill]
         if skill in list_skill:
             str_skills += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
     str_skills += "</pre>"
     return str_skills

