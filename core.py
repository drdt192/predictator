from tokenizers import Tokenizer
from tokenizers.models import BPE
#from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()
#trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
#dataset = ["data/training_dataset.txt"]
#tokenizer.train(dataset, trainer)

tokenizer = tokenizer.from_file("data/tokenizer.json")
input = input("yo give text\n")
output = tokenizer.encode(input)
print(output.tokens)

#tokenizer.save("data/tokenizer.json")