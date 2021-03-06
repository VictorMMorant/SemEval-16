"""SkipGram Module"""


from nltk import word_tokenize



def generateSkipGramDict( tweets, n):
	
	"""	
	Create an skipgram dictionary.

	Parameters: a list of tweets from training set
				a number n that representss the gap of the skipGram: 
	
	Return: a dictionary of skipgrams with the following structure:
	
		(str1,str2) ->[[frequency],[tweetIndex],[skipGramIndex]]
	"""
	
	skipGramDict = dict();

	for k,tweet in enumerate(tweets):

		tokens = tweet.strip().split(' ');
		#skipGramList.append(dict());
		
		i = 0;
		while i < len(tokens) - (n +1) :
			currentSkipGram = (tokens[i],tokens[i+n+1]);

			#Add an ocurrence to the skip-gram in the current tweet k
			if currentSkipGram in skipGramDict :
				flag = True;
				for j,skipList in enumerate(skipGramDict[currentSkipGram]):
					#Check out whether the skipGram is already in the current tweet
					if skipList[1] == k :

						skipGramDict[currentSkipGram][j][0] = skipList[0] + 1;
						flag = False;
				#Add a new ocurrence of the skipgram
				if flag :
					skipGramDict[currentSkipGram].append([1,k,skipGramDict[currentSkipGram][0][2]]);
					#print(currentSkipGram);
					#print(skipGramDict[currentSkipGram]);
			#Add a new skipgram to the dictionary
			else :
				skipGramDict[currentSkipGram] = [];
				skipGramDict[currentSkipGram].append([1,k,len(skipGramDict)-1]);
				

			i += 1;

	return skipGramDict;



def generateSkipGramMatrix(amount, skipGramDict) :	
	
	"""
	Generates a matrix from  
	Parameters: an integer representing the amount of tweets
				a dictionary of skipgrams with the following structure:
		
				(str1,str2) ->[[frequency],[tweetIndex],[skipGramIndex]]
	Return a matrix of size (len(tweets),len(skipGramDic)) filled with the ocurrences of the skipGrams in the tweets
	"""

	result = [[0]*len(skipGramDict.keys()) for i in range(amount)];

	for skip in skipGramDict:
		for j,skipList in enumerate(skipGramDict[skip]):
			if result[skipGramDict[skip][j][1]][skipGramDict[skip][j][2]] != 0 :
				result[skipGramDict[skip][j][1]][skipGramDict[skip][j][2]] += skipGramDict[skip][j][0];
			else :
				result[skipGramDict[skip][j][1]][skipGramDict[skip][j][2]] = skipGramDict[skip][j][0];
	return result;


def generateSkipGramTestDict(test,skipGramDict, n):

	"""
		Parameters: a list of tweets from testing set
					the skipGramDict generated from the training set
					a number n that represents the gap of the skipGram

		Return: a Matrix with size (len(test),len(skipGramDict)) filled with the ocurrences of the skipGrams that appears in the test set.

	"""
	#print("Bef.",skipGramDict);
	skipGramTestDict = copyDictOnlyKeys(skipGramDict);
	#print("Aft.",skipGramDict);
	#print("skipGramTestDict",skipGramTestDict);
	for k,tweet in enumerate(test):

		tokens = tweet.strip().split(' ');
		#skipGramList.append(dict());
		#print(tokens);
		i = 0;
		while i < len(tokens) - (n +1) :

			currentSkipGram = (tokens[i],tokens[i+n]);

			if currentSkipGram in skipGramDict:
				#print("I'm in the skipGramDict", currentSkipGram);
				flag = True;
				for j,skipList in enumerate(skipGramTestDict[currentSkipGram]):
					#print("SkipList", skipList);
					#Check out whether the skipGram is already in the current tweet
					if skipList[1] == k :

						skipGramTestDict[currentSkipGram][j][0] = skipList[0] + 1;
						flag = False;

				#Add a new ocurrence of the skipgram
				if flag :
					# skipGramDict[currentSkipGram][0][2] ------> get the column of the skipgram in the matrix
					#print(skipGramDict);
					#print(skipGramDict[currentSkipGram]);
					if skipGramDict[currentSkipGram] != []:
						skipGramTestDict[currentSkipGram].append([1,k,skipGramDict[currentSkipGram][0][2]]);

			i += 1;

	return skipGramTestDict;


def copyDictOnlyKeys(skipGramDict) :

	"""
		Creates a copy of a dictionary deleting the values.
		Parameters: a dictionary to copy
		Return: a dictionary with copied keys but no values.

	"""

	result = dict();

	for i in skipGramDict:
		result[i] = [];
	return result;

def getKMostFrequentSkipGrams(skipGramDict) :
	result = dict()

	sortedSkipGramList = sorted(((sum(v[0] for v in skipGramDict[k]),k) for k in skipGramDict.keys()),reverse=True);
	#print(sortedSkipGramList[:100]);
	for i,skip in enumerate(sortedSkipGramList[:100]) :
		result[skip[1]] = skipGramDict[skip[1]];
		for v in result[skip[1]]:
			v[2] = i;
	
	#print(result)
	return result;
