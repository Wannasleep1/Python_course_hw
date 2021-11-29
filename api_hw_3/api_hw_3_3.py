import datetime as dt
import json
from pprint import pprint
import requests as req


def get_questions_by_days_and_tags(days_qty, tags):
	url = 'https://api.stackexchange.com/questions'
	date_current = dt.datetime.now().date()
	date_days_ago = date_current - dt.timedelta(days=days_qty)
	date_from = dt.datetime.combine(date_days_ago, dt.datetime.min.time())
	date_to = dt.datetime.combine(date_current, dt.datetime.min.time())
	params = {
		'site': 'stackoverflow',
		'tagged': ';'.join(tags),
		'todate': int(dt.datetime.timestamp(date_to)),
		'datefrom': int(dt.datetime.timestamp(date_from)),
		'sort': 'creation'
	}
	questions = req.get(url, params=params).text
	# Предотвращение появления ошибки UnicodeEncodeError
	# (через utf-8 не работало).
	qsts_modified = questions.encode('ascii', 'ignore').decode()
	return json.loads(qsts_modified)['items']


if __name__ == '__main__':
	days_qty = 2
	tags = ['python']
	questions = get_questions_by_days_and_tags(days_qty, tags)
	pprint(questions)