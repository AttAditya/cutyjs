class Content:
  def __init__(self, content: str):
    self.original = content
    self.content = content
    self.compactions = {}
    self.issues = []

  def formatted(self) -> bool:
    return self.content != self.original

