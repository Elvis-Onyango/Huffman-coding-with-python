import numpy as np

# Define symbols and probabilities
symbols = [1, 2, 3, 4, 5]
probabilities = [0.4, 0.3, 0.15, 0.10, 0.05]

# Create a dictionary to store Huffman codes
codes = {}

def huffman_encoding(symbols, probabilities):
  """
  Constructs the Huffman code for a given set of symbols and probabilities.

  Args:
      symbols: A list of symbols.
      probabilities: A list of probabilities corresponding to the symbols.

  Returns:
      A dictionary mapping symbols to their Huffman codes.
  """
  # Node class for Huffman tree nodes
  class Node:
    def __init__(self, symbol, probability):
      self.symbol = symbol
      self.probability = probability
      self.left = None
      self.right = None

  # Create nodes for each symbol-probability pair
  nodes = [Node(symbol, probability) for symbol, probability in zip(symbols, probabilities)]

  # Build the Huffman tree using a priority queue
  while len(nodes) > 1:
    nodes.sort(key=lambda node: node.probability)
    left, right = nodes[0], nodes[1]
    parent = Node(None, left.probability + right.probability)
    parent.left = left
    parent.right = right
    nodes = nodes[2:] + [parent]

  # Assign Huffman codes using a recursive function
  def assign_codes(node, code):
    if node is None:
      return
    if node.symbol is not None:
      codes[node.symbol] = code
    assign_codes(node.left, code + '0')
    assign_codes(node.right, code + '1')

  assign_codes(nodes[0], '')

  return codes

# Generate Huffman codes
codes = huffman_encoding(symbols, probabilities)

# Calculate average code length
average_length = 0
for symbol, code in codes.items():
  average_length += len(code) * probabilities[symbols.index(symbol)]

# Print Huffman codes and average length
print("Huffman Codes:")
for symbol, code in codes.items():
  print(f"{symbol}: {code}")

print(f"\nAverage Code Length: {average_length:.2f}")
