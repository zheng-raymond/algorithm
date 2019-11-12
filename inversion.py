

def merge_and_count(n):
	''' n is a list of number'''
	global depth, count
	l = len(n)

	if l <= 10:
		for i in range(l):
			for j in range(i+1,l):
				if n[i] > n[j]:
					count += 1
		n.sort()
		return n
	else:
		print "length", l
		l1 = merge_and_count(n[:l//2])
		l2 = merge_and_count(n[l//2:])

		i = 0
		j = 0
		result_list = []
		for k in range(l):
			if i == len(l1):
				result_list += l2[j:]
				break
			elif j == len(l2):
				result_list += l1[i:]
				break

			if l1[i] < l2[j]:
				result_list.append(l1[i])
				i+=1
			else:
				result_list.append(l2[j])
				j+=1
				count += len(l1) - i 
			# except IndexError:
			# 	print "i", i , "j", j 
			# 	return [-1]
			# except TypeError as e:
			# 	print e, l1, l2
			# 	return [-1]

		return result_list


if __name__ == "__main__":
	# name = raw_input("please enter the path of the file:\n")
	name = "/Users/siyuanzheng/desktop/algorithm/inversion.txt"
	#/Users/siyuanzheng/desktop/algorithm/inversion.txt
	with open(name) as f:
		content = f.readlines()

	numbers = [int(x) for x in content]


	depth = 0
	count = 0


	merge_and_count(numbers)

	print count 


	#2407905288








