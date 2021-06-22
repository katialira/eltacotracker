# calculate Percentage of each team
def calculatePercentage(tacos):
	return round( (100 * tacos) / 2021 );

devs = {
	'tacos': 84,
	'percent': 0
}
grows = {
	'tacos': 21,
	'percent': 0
}
ops = {
	'tacos': 24,
	'percent': 0
}
total = {
	'tacos': devs['tacos'] + grows['tacos'] + ops['tacos'],
	'percent': 0
}

ops['percent'] = calculatePercentage(ops['tacos'])
devs['percent'] = calculatePercentage(devs['tacos'])
grows['percent'] = calculatePercentage(grows['tacos'])
total['percent'] = calculatePercentage(total['tacos'])

print(ops, devs, grows, total)