#Challenge One
# the hash function with n as a large prime is better as the one with many factors will have more collisions
#i.e. 350, if x is 7, or 14 or 35 you will get 0 as a result, whereas if n is 293, every value of x under 293 will hash to be different
#Challenge b
#yes that is a pretty good hash function as 599 is a fairly large prime number, so it ought to be a pretty good hash function
#Challenge III
#It takes the hash of the object and sets it sign bit to zero, then takes that number % length of table to find the proper index.
#
#
#
#
import hashlib
class HashTable():
	def __init__(self, cap):
		self.arr = [None]*cap
		self.cap = cap
	def hashCode(self, str):
		return int(str)%599%self.cap
	def put(self, str, key):
		newKey = self.hashCode(key)
		if(self.arr[newKey]==None):
			self.arr[newKey] = str
			return True
		else:
			return False
	def get(self, key):
		return arr[key]
def main():
	table = HashTable(50)
	table.put(2, "hello")
	table.put(4, "hey")
	table.put(23, "hello there")
	table.put(1, "hi")

if __name__ == '__main__':
	main()


	
