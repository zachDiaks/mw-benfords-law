'''
Plotter: Utility class to handle all plotting activities
'''
import matplotlib.pyplot as plt
import numpy as np
import string

class Plotter:
    
    def plotNumberDistribution(self, nums, numCounts):
        plt.title("Number distribution")
        plt.xlabel("Number")
        plt.ylabel("Count")
        plt.bar(nums, numCounts)

    def plotDigitDistribution(self, digitCounts, sorted=False):
        digits = np.linspace(1, 9, 9)
        digits = [str(int(x)) for x in digits]

        # Sort digits by frequency
        if sorted:
            [digitCounts, digits] = self.sortLists(digitCounts, digits)

        plt.title("First digit distribution")
        plt.xlabel("Digit")
        plt.ylabel("Count")
        plt.bar(digits, digitCounts)

    def plotWordDistribution(self, wordCounts, numWords="All", asBar=True):
        # Sort word counts
        wordCounts.sort(reverse=True)

        # Truncate to top number of hts if requested
        if numWords != "All":
            wordCounts = wordCounts[0:numWords+1]
        
        rank = list(range(1, len(wordCounts) + 1)) #np.linspace(1.0, len(wordCounts), len(wordCounts))

        # Make plot
        plt.title("Word distribution")
        plt.xlabel("Word rank")
        if asBar:
            plt.bar(rank, wordCounts)
            plt.ylim((0, max(wordCounts)))
        else:
            plt.plot(rank, wordCounts)
            plt.xscale('log')
            plt.yscale('log')


    def plotLetterDistribution(self, letterCounts, sorted=False):
        # Sort letters by letter count
        letters = list(string.ascii_lowercase)
        if sorted:
            [sortedCounts, sortedLetters] = self.sortLists(letterCounts, letters)
        else:
            sortedCounts = letterCounts
            sortedLetters = letters
        # Make plot
        plt.title("First letter distribution")
        plt.xlabel("Letter")
        plt.ylabel("Count")
        plt.bar(sortedLetters, sortedCounts)

    def sortLists(self, itemA, itemB):
        # Sorts itemA and itemB based on the contents of itemA
        idx = list(np.argsort(itemA))
        idx.reverse()

        sortedA = [itemA[x] for x in idx]
        sortedB = [itemB[x] for x in idx]

        return [sortedA, sortedB]
