# overcommented and code repeats for sake of marking. for karmakar-karp see
# method G (line 242)

import random


# A
# divide the set into two partitions by splitting it in the middle
def methodA(S):
	# initialise the arrays for the partitions and their totals. these need to
	# be reset to empty on every method call
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	# get the number of values in the set to be used for setting the second
	# partition's loop range
	setLen = len(S)
	# find the middle value's position in the set (half of the number of values)
	# to also set the loop's range
	setMid = int((setLen / 2))
	# setting the values of the first partition; loop through the set until its
	# middle point, placing those values into the first partition
	for i in range(setMid):
		S1.append(S[i])
		S1sum = S1sum + S[i]
	# setting the values of the second partition; loop through the set,
	# beginning at it's middle element and ending at the last element. place
	# those values into the second partition
	for i in range(setMid, setLen):
		S2.append(S[i])
		S2sum = S2sum + S[i]
	# this results in the first half of S's values in partition 1 and the second
	# half in partition 2. find the absolute difference between those partitions
	# to evaluate the method's effectiveness
	diff = abs(S1sum - S2sum)
	return diff


# B
# place the even values of the set into one partition and the odd values into
# another
def methodB(S):
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	# get the number of values in the set to be used for setting the set's loop
	# range
	setLen = len(S)
	# visit every value in the set and, if it can be divided by two with a
	# remainder of zero (is even) add it to partition 1. otherwise, add it to
	# partition 2 because it is odd
	for i in range(setLen):
		if (S[i] % 2) == 0:
			S1.append(S[i])
			S1sum = S1sum + S[i]
		else:
			S2.append(S[i])
			S2sum = S2sum + S[i]
	diff = abs(S1sum - S2sum)
	return diff


# C
# place the first value in the set in partition 1 and the second value in
# partition 2. iterate through the remaining values, adding the one currently
# being visited to the partition which at that point has the lowest sum
def methodC(S):
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	# add first value of S to first partition, update the sum
	S1.append(S[0])
	S1sum = S1sum + S[0]
	# do the same for partition 2 and the second value
	S2.append(S[1])
	S2sum = S2sum + S[1]
	setLen = len(S)
	# loop thorugh the rest of the values, starting at the 3rd since those have
	# already been redistributed
	for i in range (2, setLen):
		# if the sum of partition 1 is less than partition 2, add the value to
		# partition 1 and update the sum
		if S1sum < S2sum:
			S1.append(S[i])
			S1sum = S1sum + S[i]
		# otherwise add to partition 2 and update that sum
		else:
			S2.append(S[i])
			S2sum = S2sum + S[i]
	diff = abs(S1sum - S2sum)
	return diff


# D
# calculate the average value of an element in the set. place values less than
# or equal to this average into a temporay partition, 1 and values greater into
# a second temporary partition, 2. then place value 1 of temp partition 2 into
# the permanent partition 1 and value 2 into permanent partition 2. iterate
# through the rest of temp part 2, add the value to whichever perm part
# currently has the smallest sum. then iterate through temp part and add the
# value to whichever perm part currently has the smallest sum
def methodD(S):
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	# initialise the arrays for the temporary partitions
	P1 = []
	P2 = []
	# initialise the variable to count the sum of the values in the starting set
	total = 0
	setLen = len(S)
	# calculate the average value of the starting set
	for i in S:
		total += i
	avg = total / setLen
	# visit every value in the set and if the value if less than or equal to the
	# average, place it in temp partition 1
	for i in range(setLen):
		if (S[i] <= avg):
			P1.append(S[i])
		# otherwise place it in temp partition 2
		else:
			P2.append(S[i])
	# calculate the number of values in the temporary partitions
	p1Len = len(P1)
	p2Len = len(P2)
	# add the first value of the second temp partition to partition 1
	S1.append(P2[0])
	S1sum = S1sum + P2[0]
	# do the same for the second value and partition 2
	S2.append(P2[1])
	S2sum = S2sum + P2[1]
	# loop through temp part 2, beginning from value 3 as in the previous method
	# if partition 1 has a smaller sum than partition 2, add the value to it and
	# update the sum
	for i in range(2, p2Len):
		if S1sum < S2sum:
			S1.append(P2[i])
			S1sum = S1sum + P2[i]
		# otherwise add it to partition 2
		else:
			S2.append(P2[i])
			S2sum = S2sum + P2[i]
	# loop through temp partition 1 and do the same
	for i in range(p1Len):
		if S1sum < S2sum:
			S1.append(P1[i])
			S1sum = S1sum + P1[i]
		else:
			S2.append(P1[i])
			S2sum = S2sum + P1[i]
	diff = abs(S1sum - S2sum)
	return diff


# E
# sort S into ascending order then place even values into one partition and odd
# into another
def methodE(S):
	# sort the set using a built in python method
	S.sort()
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	setLen = len(S)
	# the same procedure as the previous even-odd partitioning method
	for i in range(setLen):
		if (S[i] % 2) == 0:
			S1.append(S[i])
			S1sum = S1sum + S[i]
		else:
			S2.append(S[i])
			S2sum = S2sum + S[i]
	diff = abs(S1sum - S2sum)
	return diff


# F
# sort S into descending order then place the first value into partiton 1,
# second into partition 2. iterate through the remaining values, adding to
# whichever partition currently has the smaller sum
def methodF(S):
	# sort the set using a built in python method, argument specifies descending
	# order
	S.sort(reverse = True)
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	S1.append(S[0])
	S1sum = S1sum + S[0]
	S2.append(S[1])
	S2sum = S2sum + S[1]
	setLen = len(S)
	# same procedure as used in previous method
	for i in range (2, setLen):
		if S1sum < S2sum:
			S1.append(S[i])
			S1sum = S1sum + S[i]
		else:
			S2.append(S[i])
			S2sum = S2sum + S[i]
	diff = abs(S1sum - S2sum)
	return diff


# G - karmarkar karp algorithm
# sort the values of S in descending order. calculate the difference between
# values 1 and 2. place value 1 into a temporary partition, P2, value 2 into a
# second temporary partition, P1. in S, replace the two values with a single
# value in S - the difference between them. resort the values of S in descending
# order. keep doing this until you are left with one value in S. this value is
# the heuristic difference between the two partitions. beginning from that
# heuristic value, place it into the permanent partition S2, begin the loop: if
# S2 holds the difference between the last value in P2 and the last value in P1,
# replace that difference with the last value in P2. then append S1 with the
# last value in P1. or, if S1 holds the difference between the last value in P2
# and the last value in P1, relpace that difference with thealst value in P2.
# then append S2 with the last value in P1. once that decision is made, remove
# the last values in P1/P2. stop once the temporary partitions are empty. sum up
# S1 and S2 and find their difference, since we started from the heuristic
# difference, it should be equal to it.
#
# b  a  b-a s1          s2
# 30 27 3   ()          (0)
# 16 15 1   (0)         (0)
# 9  6  3   (1)         (0,1)
# 3  3  0   (2)         (0,1,1)
# 2  1  1   (2,3)       (3,1,1)
# 1  1  0   (2,9)       (3,1,1,6)
# 0  0      (2,9,15)    (3,16,1,6)
# 0 = diff  (2,9,15,27) (30,16,1,6)
# from the bottom up:
# 1 - place the difference into s2
# 2 - place b into whichever set holds value b-a and replace that value with b,
# add a to the other set
def methodG(S):
	setLen = len(S)
	P1 = []
	P2 = []
	S1 = []
	S1sum = 0
	S2 = []
	S2sum = 0
	# while there are still two values in the set, two is needed to find the
	# difference
	while setLen > 1:
		# sort the set in descending order
		S.sort(reverse = True)
		# calculate the difference between the largest and 2nd largest set
		# values
		diff = abs(S[0] - S[1])
		# append the largest value to temp partition 2
		P2.append(S[0])
		# remove that value from the original set
		S.pop(0)
		# append the 2nd largest value to temp partition 1
		P1.append(S[0])
		# remove that value from the original set
		S.pop(0)
		# append the difference, calculated earlier to the original set
		S.append(diff)
		# decrement the calculated length of the original set
		setLen = setLen - 1
	# calculate the number of values in the temp partitions
	p1Len = len(P1)
	p2Len = len(P2)
	# add the final difference between the two largest values in the original
	# set, the heuristic value, to partition 2
	S2.append(diff)
	while p1Len > 0 and p2Len > 0:
		# calculate the difference between the first values in temp part 2 and 1
		diff = P2[p2Len - 1] - P1[p1Len - 1]
		# if that value is in partition 2
		if diff in S2:
			# replace the instance of that value with the largest value in temp
			# part 2
			diffIndex = S2.index(diff)
			S2[diffIndex] = P2[p2Len - 1]
			# append the largest value in temp part 1 to partition 1
			S1.append(P1[p1Len - 1])
		# if that value is in partition 1
		elif diff in S1:
			# replace the instance of that value with the largest value in temp
			# part 2
			diffIndex = S1.index(diff)
			S1[diffIndex] = P2[p2Len - 1]
			# append the largest value in temp part 1 to partition 2
			S2.append(P1[p1Len - 1])
		# remove the largest values in temp parts 1 and 2
		P2.pop(p2Len - 1)
		P1.pop(p1Len - 1)
		# as such, decrement the lengths of the temp parts
		p1Len = p1Len - 1
		p2Len = p2Len - 1
	# iterate through the partitions and sum up their totals
	for val in S1:
		S1sum += val
	for val in S2:
		S2sum += val
	# calculate the actual difference between the two final partitions - this
	# will be equal to the difference calculated by the heuristic
	diff = abs(S1sum - S2sum)
	return diff


def runner(numSets, card):
	# initialises empty arrays to hold the partition differences for each method
	diffsA = []
	diffsB = []
	diffsC = []
	diffsD = []
	diffsE = []
	diffsF = []
	diffsG = []
	# initialises variables to hold the average partition differences
	avgA = avgB = avgC = avgD = avgE = avgF = avgG = 0
	# generates x number of sets of y cardinality, where x and y are determined
	# in the method call
	ranSet = []
	for i in range(numSets):
		for i in range(card):
			# appends a random value to the set between 1 and 10 * the set's
			# cardinality
			ranSet.append(random.randrange(1, 10 * card))
		# each new random set is run by each method and the resulting partition
		# differences of those methods is added to an array for storage
		diffsA.append(methodA(ranSet))
		diffsB.append(methodB(ranSet))
		diffsC.append(methodC(ranSet))
		diffsD.append(methodD(ranSet))
		diffsE.append(methodE(ranSet))
		diffsF.append(methodF(ranSet))
		diffsG.append(methodG(ranSet))
	# calculates the total for each of the arrays holding differences
	for i in range(numSets):
		avgA = avgA + diffsA[i]
		avgB = avgB + diffsB[i]
		avgC = avgC + diffsC[i]
		avgD = avgD + diffsD[i]
		avgE = avgE + diffsE[i]
		avgF = avgF + diffsF[i]
		avgG = avgG + diffsG[i]
	# calculates the average for each of the arrays holding differences
	avgA = avgA / numSets
	avgB = avgB / numSets
	avgC = avgC / numSets
	avgD = avgD / numSets
	avgE = avgE / numSets
	avgF = avgF / numSets
	avgG = avgG / numSets
	# writes both all of the partition differences and their average to a text
	# file. describes the values by cardinality and method used
	res = open("results.txt", "a")
	res.write("Cardinality: "+str(card)+"\n")
	res.write("Method A Partition Differences: "+str(diffsA)+"\n")
	res.write("Method A Average Partition Difference: "+str(round(avgA))+"\n")
	res.write("Method B Partition Differences: "+str(diffsB)+"\n")
	res.write("Method B Average Partition Difference: "+str(round(avgB))+"\n")
	res.write("Method C Partition Differences: "+str(diffsC)+"\n")
	res.write("Method C Average Partition Difference: "+str(round(avgC))+"\n")
	res.write("Method D Partition Differences: "+str(diffsD)+"\n")
	res.write("Method D Average Partition Difference: "+str(round(avgD))+"\n")
	res.write("Method E Partition Differences: "+str(diffsE)+"\n")
	res.write("Method E Average Partition Difference: "+str(round(avgE))+"\n")
	res.write("Method F Partition Differences: "+str(diffsF)+"\n")
	res.write("Method F Average Partition Difference: "+str(round(avgF))+"\n")
	res.write("Method G Partition Differences: "+str(diffsG)+"\n")
	res.write("Method G Average Partition Difference: "+str(round(avgG))+"\n\n")
	res.close()


def main():
	# each of these methods creates 12 sets of specified cardinality then
	# performs each method once on each generated set the partition differences
	# and average partition differences are written to a text file
	runner(12, 32)
	runner(12, 64)
	runner(12, 128)
	runner(12, 256)
	runner(12, 512)
	runner(12, 1024)

# run
main()
