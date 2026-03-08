from tokenizers import Tokenizer
from tokenizers.models import BPE
#from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()

#trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
#dataset = ["data/training_dataset.txt"]
#tokenizer.train(dataset, trainer)

tokenizer.from_file("data/tokenizer.json")

output = tokenizer.encode("Hello, how are you?")
print(output.tokens)

#tokenizer.save("data/tokenizer.json")