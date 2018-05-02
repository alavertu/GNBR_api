import hashlib

class Property():
    def __init__(self, fields=[], header=[]):
    	self._idx = [header.index(field) for field in fields]

    def fetch(self, line):
        return [line[i] for i in self._idx]


class Label( Property ):
	def __init__(self, labels, header):
		super().__init__(labels, header)

	def fetch_label(self, line):
		return ''.join( sorted( self.fetch(line) ) )


class Identifier( Property ):
	def __init__(self, ids, header):
		super().__init__(ids, header)

	def fetch_id(self, line, label=''):
		id_string = ''.join( self.fetch(line) + [label] )
		return hashlib.md5( id_string.encode() ).hexdigest()

class Entity(Property):
	def __init__(self, ids, labels, props, header):
		super().__init__(props, header)
		self._label = Label(labels, header)
		self._uid = Identifier(ids, header)
		self._data = set()

	def fetch_properties(self, line):
		return self.fetch(line)

	def fetch_label(self, line):
		return self._label.fetch_label(line)

	def fetch_id(self, line):
		label = self._label.fetch_label(line)
		return self._uid.fetch_id(line, label)

	def update(self, line):
		self._data.add( self.fetch_id(line) )

	def duplicated(self, line):
		return self.fetch_id in self._data

	def fetch_entity(self, line):
		uid = self.fetch_id(line)
		label = self.fetch_label(line)
		props = self.fetch_properties(line)
		self.update(uid) 
		return [uid, label] + props


class Relation(Property):
	def __init__(self, enty1, enty2, props, header):
		super().__init__(props, header)
		self._start = enty1
		self._end = enty2
		self._data = set()

	def fetch_properties(self, line):
		return self.fetch(line)

	def fetch_label(self, line):
		start_label = self._start.fetch_label(line)
		end_label = self._end.fetch_label(line)
		return ''.join( [start_label, end_label] )

	def fetch_id(self, line):
		start_id = self._start.fetch_id(line)
		end_id = self._end.fetch_id(line)
		return (start_id, end_id)

	def update(self, line):
		self._data.add( self.fetch_id(line) )

	def duplicated(self, line):
		key = self.fetch_id(line)
		return key in self._data

	def fetch_relation(self, line):
		start_id, end_id = self.fetch_id(line)
		label = self.fetch_label(line)
		props = self.fetch_properties(line)
		self.update( line )
		return [start_id, end_id, label] + props

