from mrjob.job import MRJob


class HitCount(MRJob):
	def mapper(self, _, line):
		data = line.strip().split("GET ")
		if len(data) > 1:
			filename = data[1].split()[0]
			yield(filename, 1)

	def reducer(self, filename, counts):
		yield(filename, sum(counts))


if __name__ == '__main__':
	HitCount.run()
