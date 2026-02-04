import tiktoken

# enc = tiktoken.encoding_for_model("gpt-4o")
enc = tiktoken.get_encoding("cl100k_base")


text = "hey There! My name is Bhardwaz"

tokens = enc.encode(text)

print ("Tokens", tokens)

# Tokens [36661, 2684, 0, 3092, 836, 374, 426, 19221, 86, 1394]

decoded = enc.decode([36661, 2684, 0, 3092, 836, 374, 426, 19221, 86, 1394])

print("Decoded", decoded)