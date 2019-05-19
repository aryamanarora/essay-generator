from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('input.txt', num_epochs=4)
textgen.generate_to_file('output.txt', n=5)