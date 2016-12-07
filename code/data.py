data = {
		'Belgium'		 : {
								'languages' : ['NL', 'DE', 'FR'],
								'continent' : 'Europe'
						   },
		'France'		: {
								'languages' : ['FR'],
								'continent' : 'Europe'
						  },
		'New Zealand'	: {
								'languages' : ['EN', 'MI'],
								'continent' : 'Oceania'
						  }
	   }


print([key for key in data if data[key]['continent'] == 'Europe'])