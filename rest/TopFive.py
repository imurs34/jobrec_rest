from django.forms.models import model_to_dict
from .models import Job
import random
'''
    input: list of interests, objects, num of choices
'''

def TopFive(interests, jlist, n_choice):

        #print(jlist)

        # Build jobs_dict
        jobs_dict = dict()
        for job in jlist:
            if job['category'] in jobs_dict:
                jobs_dict[job['category']].append(job['title'])
            else:
                jobs_dict[job['category']] = [job['title']]

        rankings = list()

        # Based on 2 interests of a user, select 4 jobs
        secure_random = random.SystemRandom()
        for i in range(4):
            sel = secure_random.choice(jobs_dict.get(interests[i%n_choice]))
            rankings.append(sel)
            jobs_dict.get(interests[i%n_choice]).remove(sel)

        # Remove already chosen categories
        for i in range(n_choice):
            jobs_dict.pop(interests[i])

        # Select 1 random job
        secure_random = random.SystemRandom()
        random_category = secure_random.choice(list(jobs_dict))
        random_job = secure_random.choice(jobs_dict.get(random_category))
        rankings.append(random_job)

        return rankings
