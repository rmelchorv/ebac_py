import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords

# Función para leer un archivo y devolverlo como una cadena de texto
def get_text(path_and_file):
    with open(path_and_file, 'r') as file:
        text = file.read()
    return text

def process_text(text):
    
    # Tokenización de oraciones
    sentences = sent_tokenize(text)
    print("Oraciones:", sentences)

    # Tokenización de palabras
    tokens = word_tokenize(text)
    print("Tokens:", tokens)

    # Etiquetado gramatical
    tagged = pos_tag(tokens)
    print("Etiquetas gramaticales:", tagged)

    # Reconocimiento de entidades nombradas
    named_entities = ne_chunk(tagged)
    print("Entidades nombradas:", named_entities)

    # Eliminación de palabras vacías (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_words = [token for token in tokens if token.lower() not in stop_words]
    print("Palabras filtradas:", filtered_words)

# Texto de ejemplo
texto_ejemplo = get_text('texto.txt')

# Procesar el texto
process_text(texto_ejemplo)