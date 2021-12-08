class bubbleSort:
	def __init__(self, angka):
		self.angka = angka
		self.panjang = len(angka)

	def __str__(self):
		return " ".join([str(x)
						for x in self.angka])

	def bubbleSortRecursive(self, n = None):
		if n is None:
			n = self.panjang

		if n == 1:
			return

		for i in range(n - 1):
			if self.angka[i] > self.angka[i + 1]:
				self.angka[i], self.angka[i + 1] = self.angka[i + 1], self.angka[i]

		self.bubbleSortRecursive(n - 1)

def main():
	angka = [400, 24, 40, 5, 12, 50, 200,(-30)]
	sort = bubbleSort(angka)
	sort.bubbleSortRecursive()
	print("Sesudah di sorting :\n", sort)

if __name__ == "__main__":
	main()
