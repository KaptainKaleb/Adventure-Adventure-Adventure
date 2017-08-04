"""
	Everything related to the Chapter Management
"""

class Chappie():
	def __init__(self, gameState):
		"""

		:param gameState: An object that represents the game's state(current player, chapter, stats, world...)
		"""
		self.state=gameState

	def startChapter(self, chapter):
		"""
			Would just switch to a chapter, by doing everything that is needed(initialising stuff in the chapter, closing old one)
		:param chapter: Representation of a chapter
		:return:
		"""
		self.state.exitCurrentChapter()
		self.state.chapter=chapter

	def nextChapter(self):
		"""
		Goes to the next chapter in the tree, depending on the game's state
		:return:
		"""

	def updateState(self, **kwargs):
		self.state.update(**kwargs)
