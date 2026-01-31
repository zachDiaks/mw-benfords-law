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

    def plotDigitDistribution(self, digitCounts, expDistribution, sorted=False):
        digits = np.linspace(1, 9, 9)
        digits = [str(int(x)) for x in digits]

        # Sort digits by frequency
        if sorted:
            [digitCounts, digits] = self.sortLists(digitCounts, digits)

        # Compute expected frequency
        expFrequency = expDistribution / 100 * np.sum(digitCounts)

        plt.title("First digit distribution")
        plt.xlabel("Digit")
        plt.ylabel("Count")
        plt.bar(digits, digitCounts, label="Actual Digit Count")
        plt.plot(digits, expFrequency, label="Expected Digit Count", color="orange", marker="o")

        plt.legend()
    def plotWordDistribution(self, wordCounts, wordRange="All", asBar=True):
        # Sort word counts
        wordCounts.sort(reverse=True)

        # Truncate to top number of hts if requested
        if wordRange != "All":
            wordCounts = wordCounts[wordRange[0]-1:wordRange[1]]
            rank = np.linspace(wordRange[0], wordRange[1], wordRange[1] - wordRange[0] + 1)
        else:
            rank = list(range(1, len(wordCounts) + 1)) #np.linspace(1.0, len(wordCounts), len(wordCounts))

        # Make plot
        plt.title("Word distribution")
        plt.xlabel("Word rank")
        plt.ylabel("Word frequency")
        if asBar:
            plt.bar(rank, wordCounts)
            plt.ylim((0, max(wordCounts)))
            return 0
        else:
            # Plot word count distribution
            plt.plot(rank, wordCounts, label="Word frequency")

            # Fit word log of word frequency to a line
            logCounts = np.log10(wordCounts)
            logRank = np.log10(rank)
            fit = np.polyfit(logRank, logCounts, 1)
            fitX = rank
            fitY = pow(fitX, fit[0]) * pow(10, fit[1])
            plt.plot(fitX, fitY, label="Zipfian Fit")
            plt.xscale('log')
            plt.yscale('log')
            plt.legend()
            return fit


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
