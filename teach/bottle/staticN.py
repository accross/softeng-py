from bottle import static_file,route,run

@route('/staticfiles/tets.html')
def server_static(filename):
	    return static_file('filename, root=~./staticfiles')

run(host='localhost', port=8080, debug=True)
