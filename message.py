import sublime


def alert(msg):
	sublime.status_message('Accessbility: %s' % msg)
