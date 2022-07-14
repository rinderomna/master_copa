class Figurinha:
    def __init__(self, page_index, fig_index):
        self.page_index = page_index
        self.fig_index = fig_index
        self.amount = 1

    def __eq__(self, other) -> bool:
        return self.page_index == other.page_index and self.fig_index == other.fig_index